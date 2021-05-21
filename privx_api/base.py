import base64
import http.client
import json
import ssl
import urllib.parse
import urllib.request
from http.client import HTTPException, HTTPResponse
from typing import Optional, Tuple, Union

from privx_api.enums import UrlEnum
from privx_api.exceptions import InternalAPIException


def format_path_components(format_str: str, **kw) -> str:
    components = {k: urllib.parse.quote(v, safe="") for k, v in kw.items()}
    return format_str.format(**components)


class Connection:
    def __init__(self, connection_info) -> None:
        self.host = connection_info["host"]
        self.port = connection_info["port"]
        self.ca_cert = connection_info["ca_cert"]
        self._connection = None

    def __enter__(self) -> http.client.HTTPSConnection:
        self._connection = self.connect()
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._connection.close()

    def connect(self) -> http.client.HTTPSConnection:
        return http.client.HTTPSConnection(
            self.host, port=self.port, context=self.get_context()
        )

    def get_context(self) -> ssl.SSLContext:
        return ssl.create_default_context(cadata=self.ca_cert)


class BasePrivXAPI:
    """
    Base class of PrivXAPI.
    """

    def __init__(
        self, hostname, hostport, ca_cert, oauth_client_id, oauth_client_secret
    ) -> None:
        self._access_token = ""
        self._oauth_client_id = oauth_client_id
        self._oauth_client_secret = oauth_client_secret
        self._connection_info = {
            "host": hostname,
            "port": hostport,
            "ca_cert": ca_cert,
        }

    def _authenticate(self, username: str, password: str) -> None:
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

    def _build_request(
        self,
        method: str,
        url_name: str,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
        body: Optional[Union[dict, str, list]] = None,
    ) -> dict:

        path_params = path_params or {}
        query_params = query_params or {}
        headers = self._get_headers()
        url = self._build_url(url_name, path_params, query_params)
        request_dict = dict(method=method, url=url, headers=headers)
        if body is not None:
            request_dict["body"] = self._make_body_params(body)
        return request_dict

    def _build_url(
        self,
        name: str,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> str:
        path_params = path_params or {}
        query_params = query_params or {}

        url = self._get_url(name)
        if path_params:
            url = format_path_components(url, **path_params)
        if query_params:
            params = urllib.parse.urlencode(query_params)
            url = "{}?{}".format(url, params)

        return url

    def _get_headers(self) -> dict:
        return {
            "Content-type": "application/json",
            "Authorization": "Bearer {}".format(self._access_token),
        }

    def _get_search_params(self, **kwargs: Union[str, int]) -> dict:
        params = {key: val for key, val in kwargs.items() if val is not None}
        return params if any(params) else {}

    def _get_url(self, name: str) -> str:
        url = UrlEnum.get(name)
        if not url:
            raise InternalAPIException("URL missing: ", name)
        return url

    def _http_get(
        self,
        url_name: str,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> Tuple:

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    **self._build_request(
                        "GET",
                        url_name,
                        path_params,
                        query_params,
                    )
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_get_no_auth(self, url_name: str) -> Tuple:
        request = self._build_request("GET", url_name)
        headers = request["headers"]
        del headers["Authorization"]

        with Connection(self._connection_info) as conn:
            try:
                conn.request(**request)
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_post(
        self,
        url_name: str,
        body: Optional[Union[dict, str, list]] = None,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> Tuple:

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    **self._build_request(
                        "POST",
                        url_name,
                        path_params,
                        query_params,
                        body=body,
                    )
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_put(
        self,
        url_name: str,
        body: Optional[Union[dict, str, list]] = None,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> Tuple:

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    **self._build_request(
                        "PUT",
                        url_name,
                        path_params,
                        query_params,
                        body=body,
                    )
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_delete(
        self,
        url_name: str,
        body: Optional[dict] = None,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> Tuple:

        with Connection(self._connection_info) as conn:
            try:
                conn.request(
                    **self._build_request(
                        "DELETE",
                        url_name,
                        path_params,
                        query_params,
                        body=body,
                    )
                )
            except (OSError, HTTPException) as e:
                raise InternalAPIException(str(e))
            response = conn.getresponse()
            return response.status, response.read()

    def _http_stream(
        self,
        url_name: str,
        body: Optional[dict] = None,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ) -> HTTPResponse:
        conn = Connection(self._connection_info).connect()
        try:
            conn.request(
                **self._build_request(
                    "GET",
                    url_name,
                    path_params,
                    query_params,
                    body=body,
                )
            )
        except (OSError, HTTPException) as e:
            raise InternalAPIException(str(e))
        return conn.getresponse()

    def _make_body_params(self, data: Union[dict, str]) -> str:
        return data if isinstance(data, str) else json.dumps(data)
