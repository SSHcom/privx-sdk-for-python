import base64
import http.client
import json
import ssl
import time
import urllib.parse
import urllib.request
from http.client import HTTPException, HTTPResponse
from json import JSONDecodeError
from typing import Optional, Tuple, Union

from privx_api.enums import NO_AUTH_STATUS_URLS, UrlEnum
from privx_api.exceptions import InternalAPIException


def format_path_components(format_str: str, **kw) -> str:
    try:
        components = {k: urllib.parse.quote(v, safe="") for k, v in kw.items()}
    except TypeError:
        incorrect_params = {
            k: f"{type(v).__name__}"
            for k, v in kw.items()
            if isinstance(v, str) is False
        }
        error_message = (
            f"Expect argument type str but got:\n"
            f"{json.dumps(incorrect_params, indent=4)}"
        )
        raise InternalAPIException(error_message)
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
        try:
            context = ssl.create_default_context(cadata=self.ca_cert)
        except ssl.SSLError as e:
            raise InternalAPIException(e)
        return context


class BasePrivXAPI:
    """
    Base class of PrivXAPI.
    """

    def __init__(
        self,
        hostname: str,
        hostport: int,
        ca_cert: str,
        oauth_client_id: str,
        oauth_client_secret: str,
        re_auth_margin: int = 3,
    ) -> None:
        self._access_token = ""
        self._oauth_client_id = oauth_client_id
        self._oauth_client_secret = oauth_client_secret
        self._connection_info = {
            "host": hostname,
            "port": hostport,
            "ca_cert": ca_cert,
        }
        self._api_client_id = None
        self._api_client_password = None
        self._re_auth_deadline = None
        self._access_token_age = None
        self._re_auth_margin = re_auth_margin
        self._sticky_session = None

    def _authenticate(self, username: str, password: str) -> None:
        # saving the creds for the re-auth purposes
        self._initialize_api_client_credentials(username, password)
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
                raise InternalAPIException(e)
            response = conn.getresponse()
            if response.status != 200:
                raise InternalAPIException("Invalid response: ", response.status)

            try:
                data = json.loads(response.read())
            except (JSONDecodeError, TypeError) as e:
                raise InternalAPIException(e) from e

            if not self._sticky_session:
                self._sticky_session = response.getheader("Set-Cookie")

            # privx response includes access token age in seconds
            self._access_token_age = data.get("expires_in")
            self._re_auth_deadline = (
                int(time.time()) + self._access_token_age - self._re_auth_margin
            )
            self._access_token = data.get("access_token")
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
        self._reauthenticate_access_token(url_name)
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
        headers = {
            "Content-type": "application/json",
        }
        if self._access_token:
            headers["Authorization"] = "Bearer {}".format(self._access_token)
        if self._sticky_session:
            headers["Cookie"] = self._sticky_session
        return headers

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
                raise InternalAPIException(e)
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
                raise InternalAPIException(e)
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
                raise InternalAPIException(e)
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
                raise InternalAPIException(e)
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
                raise InternalAPIException(e)
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
            raise InternalAPIException(e)
        return conn.getresponse()

    def _make_body_params(self, data: Union[dict, str]) -> str:
        return data if isinstance(data, str) else json.dumps(data)

    def _reauthenticate_access_token(self, url_name: str) -> None:
        """
        _reauthenticate_access_token will attempt to reauthenticate if the access token
        is expired or there was not an initial authentication.
        """
        # do not re-authenticate if there is no initial authentication and url_name is
        # in STATUS urls set
        if url_name in NO_AUTH_STATUS_URLS and self._re_auth_deadline is None:
            return

        # checking if access token is expired and do re-auth if needed
        now = int(time.time())
        if self._re_auth_deadline is None or now >= self._re_auth_deadline:
            self._authenticate(self._api_client_id, self._api_client_password)

    def _initialize_api_client_credentials(self, username: str, password: str):
        # check if arguments are None or empty string
        if {username, password} & {None, ""}:
            raise InternalAPIException("api client credentials are not valid")
        self._api_client_id = username
        self._api_client_password = password
