import base64
import http.client
import json
import ssl
import urllib.parse
import urllib.request
from typing import Union

from privx_api.exceptions import InternalAPIException
from privx_api.enums import UrlEnum


def format_path_components(format_str: str, **kw) -> str:
    components = {k: urllib.parse.quote(v, safe="") for k, v in kw.items()}
    return format_str.format(**components)


class BasePrivXAPI:
    """
    Base class of PrivXAPI.
    """

    def __init__(
        self, hostname, hostport, ca_cert, oauth_client_id, oauth_client_secret
    ):
        self._hostname = hostname
        self._hostport = hostport
        self._access_token = ""
        self._ca_cert = ca_cert
        self._oauth_client_id = oauth_client_id
        self._oauth_client_secret = oauth_client_secret

    #
    # Internal functions.
    #
    @classmethod
    def _get_url(cls, name: str) -> str:
        url = UrlEnum.get(name)
        if not url:
            raise InternalAPIException("URL missing: ", name)
        return url

    @classmethod
    def _build_url(cls, name: str, path_params=None, query_params=None) -> str:
        path_params = path_params or {}
        query_params = query_params or {}

        url = cls._get_url(name)
        if path_params:
            url = format_path_components(url, **path_params)
        if query_params:
            params = urllib.parse.urlencode(query_params)
            url = "{}?{}".format(url, params)

        return url

    def _get_context(self) -> ssl.SSLContext:
        return ssl.create_default_context(cadata=self._ca_cert)

    def _get_connection(self) -> http.client.HTTPSConnection:
        return http.client.HTTPSConnection(
            self._hostname, port=self._hostport, context=self._get_context()
        )

    def _authenticate(self, username: str, password: str):
        conn = self._get_connection()
        token_request = {
            "grant_type": "password",
            "username": username,
            "password": password,
        }
        basic_auth = base64.b64encode(
            "{}:{}".format(self._oauth_client_id, self._oauth_client_secret).encode(
                "utf-8"
            )
        )

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(basic_auth.decode("utf-8")),
        }
        conn.request(
            "POST",
            self._get_url(UrlEnum.AUTH.TOKEN),
            body=urllib.parse.urlencode(token_request),
            headers=headers,
        )
        response = conn.getresponse()
        if response.status != 200:
            raise InternalAPIException("Invalid response: ", response.status)

        data = response.read()
        self._access_token = json.loads(data).get("access_token")
        if self._access_token == "":
            raise InternalAPIException("Failed to get access token")

        conn.close()

    def _get_headers(self) -> dict:
        return {
            "Content-type": "application/json",
            "Authorization": "Bearer {}".format(self._access_token),
        }

    def _get_search_params(self, **kwargs: Union[str, int]) -> dict:
        params = {key: val for key, val in kwargs.items() if val}
        return params if any(params) else {}

    def _http_get(
        self, urlname: str, path_params=None, query_params=None
    ) -> http.client.HTTPResponse:
        path_params = path_params or {}
        query_params = query_params or {}

        conn = self._get_connection()

        conn.request(
            "GET",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
        )

        return conn.getresponse()

    def _http_get_no_auth(self, urlname: str) -> http.client.HTTPResponse:
        headers = self._get_headers()
        del headers["Authorization"]

        conn = self._get_connection()
        conn.request(
            "GET",
            self._build_url(urlname),
            headers=headers,
        )

        return conn.getresponse()

    def _http_post(
        self, urlname: str, body=None, path_params=None, query_params=None
    ) -> http.client.HTTPResponse:
        body = body or {}
        path_params = path_params or {}
        query_params = query_params or {}

        conn = self._get_connection()

        conn.request(
            "POST",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
            body=json.dumps(body),
        )

        return conn.getresponse()

    def _http_put(
        self, urlname: str, body=None, path_params=None, query_params=None
    ) -> http.client.HTTPResponse:
        body = body or {}
        path_params = path_params or {}
        query_params = query_params or {}

        conn = self._get_connection()
        conn.request(
            "PUT",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
            body=json.dumps(body),
        )

        return conn.getresponse()

    def _http_delete(
        self, urlname: str, body=None, path_params=None, query_params=None
    ) -> http.client.HTTPResponse:
        body = body or {}
        path_params = path_params or {}
        query_params = query_params or {}

        conn = self._get_connection()
        conn.request(
            "DELETE",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
            body=json.dumps(body),
        )

        return conn.getresponse()
