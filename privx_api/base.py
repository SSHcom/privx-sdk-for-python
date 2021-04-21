import base64
import http.client
import json
import ssl
import urllib.parse
import urllib.request
from typing import Union
from http.client import HTTPException

from privx_api.exceptions import InternalAPIException
from privx_api.enums import UrlEnum


def format_path_components(format_str: str, **kw) -> str:
    components = {k: urllib.parse.quote(v, safe="") for k, v in kw.items()}
    return format_str.format(**components)


class Connection:
    def __init__(self, connection_info):
        self.host = connection_info["host"]
        self.port = connection_info["port"]
        self.ca_cert = connection_info["ca_cert"]
        self._connection = None

    def __enter__(self):
        self._connection = http.client.HTTPSConnection(
            self.host, port=self.port, context=self.get_context()
        )
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def get_context(self) -> ssl.SSLContext:
        return ssl.create_default_context(cadata=self.ca_cert)


class BasePrivXAPI:
    """
    Base class of PrivXAPI.
    """

    def __init__(
        self, hostname, hostport, ca_cert, oauth_client_id, oauth_client_secret
    ):
        self._access_token = ""
        self._oauth_client_id = oauth_client_id
        self._oauth_client_secret = oauth_client_secret
        self._connection_info = {
            "host": hostname,
            "port": hostport,
            "ca_cert": ca_cert,
        }

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

    def _authenticate(self, username: str, password: str):
        with Connection(self._connection_info) as conn:
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
            try:
                conn.request(
                    "POST",
                    self._get_url(UrlEnum.AUTH.TOKEN),
                    body=urllib.parse.urlencode(token_request),
                    headers=headers,
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            if response.status != 200:
                raise InternalAPIException("Invalid response: ", response.status)

            data = response.read()
            self._access_token = json.loads(data).get("access_token")
            if self._access_token == "":
                raise InternalAPIException("Failed to get access token")

    def _get_headers(self) -> dict:
        return {
            "Content-type": "application/json",
            "Authorization": "Bearer {}".format(self._access_token),
        }

    def _get_search_params(self, **kwargs: Union[str, int]) -> dict:
        params = {key: val for key, val in kwargs.items() if val}
        return params if any(params) else {}

    def _http_get(self, urlname: str, path_params=None, query_params=None) -> tuple:
        path_params = path_params or {}
        query_params = query_params or {}

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    "GET",
                    self._build_url(urlname, path_params, query_params),
                    headers=self._get_headers(),
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_get_no_auth(self, urlname: str) -> tuple:
        headers = self._get_headers()
        del headers["Authorization"]

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    "GET",
                    self._build_url(urlname),
                    headers=headers,
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_post(
        self, urlname: str, body=None, path_params=None, query_params=None
    ) -> tuple:
        body = body or {}
        path_params = path_params or {}
        query_params = query_params or {}

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    "POST",
                    self._build_url(urlname, path_params, query_params),
                    headers=self._get_headers(),
                    body=self._make_body_params(body),
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_put(
        self, urlname: str, body=None, path_params=None, query_params=None
    ) -> tuple:
        body = body or {}
        path_params = path_params or {}
        query_params = query_params or {}

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    "PUT",
                    self._build_url(urlname, path_params, query_params),
                    headers=self._get_headers(),
                    body=self._make_body_params(body),
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_delete(
        self, urlname: str, body=None, path_params=None, query_params=None
    ) -> tuple:
        body = body or {}
        path_params = path_params or {}
        query_params = query_params or {}

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    "DELETE",
                    self._build_url(urlname, path_params, query_params),
                    headers=self._get_headers(),
                    body=self._make_body_params(body),
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    @staticmethod
    def _make_body_params(data: Union[dict, str]) -> str:
        return data if isinstance(data, str) else json.dumps(data)
