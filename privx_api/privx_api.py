#
# Copyright (c) 2019 SSH Communications Security Corp.
#
# See the LICENSE file for the details on licensing.
#


# Requires Python 3.6+

# https://docs.python.org/3/library/urllib.html
# https://docs.python.org/3/library/ssl.html
# https://docs.python.org/3/library/http.html
# https://docs.python.org/3/library/base64.html
# https://docs.python.org/3/library/json.html

import urllib.parse
import urllib.request
import ssl
import http.client
import base64
import json


# Privx URLs.
URLS = {
    "auth.authorize": "/auth/api/v1/oauth/authorize",
    "auth.token": "/auth/api/v1/oauth/token",

    "hoststore.hosts": "/host-store/api/v1/hosts",
    "hoststore.host": "/host-store/api/v1/hosts/{host_id}",
    "hoststore.hosts.search": "/host-store/api/v1/hosts/search",

    "rolestore.roles": "/role-store/api/v1/roles",
    "rolestore.sources": "/role-store/api/v1/sources",
    "rolestore.roles.members": "/role-store/api/v1/roles/{role_id}/members",
    "rolestore.role": "/role-store/api/v1/roles/{role_id}",

    "userstore.status": "/local-user-store/api/v1/status",
    "userstore.users": "/local-user-store/api/v1/users",
    "userstore.user": "/local-user-store/api/v1/users/{user_id}",

    "connection.manager.search":
        "/connection-manager/api/v1/connections/search",
}


#
# Exceptions.
#
class InternalAPIException(Exception):
    """
    Internal API exception.
    """
    pass


#
# PrivX API lib response.
#
class PrivXAPIResponse(object):
    """
    Response object for PrivX API library.

    Args:
        response: The response object to handle.
        expstatus: The expected response status.
    """
    def __init__(self, response: http.client.HTTPResponse, expstatus: int):
        if expstatus == response.status:
            self._ok = True
            self._data = {}

            content = response.read().strip()
            if len(content):
                self._data = json.loads(content)
        else:
            self._ok = False
            data = {
                "status": response.status,
                "details": {},
            }
            self._data = data

            content = response.read().strip()
            if len(content.strip()):
                data["details"] = json.loads(content)

    def ok(self) -> bool:
        """
        Returns:
            Boolean wheter the call was successful or not
        """
        return self._ok

    def data(self) -> dict:
        """
        Returns:
            The response data
        """
        return self._data


def format_path_components(format_str: str, **kw) -> str:
    components = {k: urllib.parse.quote(v, safe='')
                  for k, v in kw.items()}
    return format_str.format(**components)


#
# Privx API.
#
class PrivXAPI(object):
    """
    Instance for Privx API library.
    """
    def __init__(self, hostname, hostport, ca_cert, oauth_client_id,
                 oauth_client_secret):
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
        url = URLS.get(name)
        if not url:
            raise InternalAPIException("URL missing: ", name)
        return url

    @classmethod
    def _build_url(cls, name: str,
                   path_params: dict = {},
                   query_params: dict = {}) -> str:

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
            self._hostname, port=self._hostport, context=self._get_context())

    def _authenticate(self, username: str, password: str):
        conn = self._get_connection()
        token_request = {
            'grant_type': 'password',
            'username': username,
            'password': password,
        }
        basic_auth = base64.b64encode(
            "{}:{}".format(self._oauth_client_id,
                           self._oauth_client_secret).encode('utf-8'))

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(basic_auth.decode('utf-8')),
        }
        conn.request(
            "POST",
            self._get_url("auth.token"),
            body=urllib.parse.urlencode(token_request),
            headers=headers,
        )
        response = conn.getresponse()
        if response.status != 200:
            raise InternalAPIException(
                "Invalid response: ", response.status)

        data = response.read()
        self._access_token = json.loads(data).get('access_token')
        if self._access_token == "":
            raise InternalAPIException("Failed to get access token")

        conn.close()

    def _get_headers(self) -> dict:
        return {
            "Content-type": "application/json",
            "Authorization": "Bearer {}".format(self._access_token),
        }

    def _http_get(self, urlname: str,
                  path_params: dict = {},
                  query_params: dict = {}) -> http.client.HTTPResponse:

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

    def _http_post(self,
                   urlname: str,
                   body: dict = {},
                   path_params: dict = {},
                   query_params: dict = {}) -> http.client.HTTPResponse:

        conn = self._get_connection()

        conn.request(
            "POST",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
            body=json.dumps(body),
        )

        return conn.getresponse()

    def _http_put(self, urlname: str,
                  body: dict = {},
                  path_params: dict = {},
                  query_params: dict = {}) -> http.client.HTTPResponse:

        conn = self._get_connection()
        conn.request(
            "PUT",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
            body=json.dumps(body),
        )

        return conn.getresponse()

    def _http_delete(self, urlname: str,
                  body: dict = {},
                  path_params: dict = {},
                  query_params: dict = {}) -> http.client.HTTPResponse:

        conn = self._get_connection()
        conn.request(
            "DELETE",
            self._build_url(urlname, path_params, query_params),
            headers=self._get_headers(),
            body=json.dumps(body),
        )

        return conn.getresponse()

    #
    # Public functions.
    #
    def authenticate(self, username: str, password: str):
        """
        Login api client to the API.

        Raises:
            An InternalAPIException on failure
        """
        # TODO: should return PrivXAPIResponse
        self._authenticate(username, password)

    #
    # Host store API.
    #
    def create_host(self, host: dict) -> PrivXAPIResponse:
        """
        Create a host, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post("hoststore.hosts", body=host)
        return PrivXAPIResponse(response, 201)

    def update_host(self, host_id: str, host: dict) -> PrivXAPIResponse:
        """
        Update a host, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_put("hoststore.host",
                                  path_params={'host_id': host_id}, body=host)
        return PrivXAPIResponse(response, 200)

    def get_hosts(self) -> PrivXAPIResponse:
        """
        Get hosts.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get("hoststore.hosts")
        return PrivXAPIResponse(response, 200)

    def search_hosts(self, offset: int = None, limit: int = None,
                     sortkey: str = None, sortdir: str = None,
                     filter: str = None, **kw) -> PrivXAPIResponse:

        search_params = {}
        if offset is not None:
            search_params['offset'] = offset
        if limit is not None:
            search_params['limit'] = limit
        if sortkey is not None:
            search_params['sortkey'] = sortkey
        if sortdir is not None:
            search_params['sortdir'] = sortdir
        if filter is not None:
            search_params['filter'] = filter

        response = self._http_post("hoststore.hosts.search",
                                   query_params=search_params,
                                   body=kw)
        return PrivXAPIResponse(response, 200)

    #
    # Role store API.
    #
    def create_role(self, role: dict) -> PrivXAPIResponse:
        """
        Create a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post("rolestore.roles", body=role)
        return PrivXAPIResponse(response, 201)

    def get_roles(self) -> PrivXAPIResponse:
        """
        Get roles.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get("rolestore.roles")
        return PrivXAPIResponse(response, 200)

    def get_sources(self) -> PrivXAPIResponse:
        """
        Get sources.

        Returns:
            PrivxAPIResponse
        """
        response = self._http_get("rolestore.sources")
        return PrivXAPIResponse(response, 200)

    def get_role_members(self, role_id: str) -> PrivXAPIResponse:
        """
        Get Role Members.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get("rolestore.roles.members",
                                  path_params={'role_id': role_id})
        return PrivXAPIResponse(response, 200)

    def update_role(self, role_id: str, role: dict) -> PrivXAPIResponse:
        """
        Update a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_put("rolestore.role",
                                  path_params={'role_id': role_id}, body=role)
        return PrivXAPIResponse(response, 200)

    #
    # User store API.
    #
    def create_user(self, user: dict) -> PrivXAPIResponse:
        """
        Create a user, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post("userstore.users", body=user)
        return PrivXAPIResponse(response, 201)

    def get_local_users(self) -> PrivXAPIResponse:
        """
        Get users.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get("userstore.users")
        return PrivXAPIResponse(response, 200)

    def delete_user(self, user_id: str) -> PrivXAPIResponse:
        """
        Delete a local user, required field user_id.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_delete("userstore.user",
                                     path_params={'user_id': user_id})
        return PrivXAPIResponse(response, 200)

    #
    # Connection manager API.
    #
    def search_connections(self, offset: int = None, limit: int = None,
                           sortkey: str = None,
                           sortdir: str = None, **kw) -> PrivXAPIResponse:

        search_params = {}
        if offset is not None:
            search_params['offset'] = offset
        if limit is not None:
            search_params['limit'] = limit
        if sortkey is not None:
            search_params['sortkey'] = sortkey
        if sortdir is not None:
            search_params['sortdir'] = sortdir

        response = self._http_post("connection.manager.search",
                                   query_params=search_params,
                                   body=kw)
        return PrivXAPIResponse(response, 200)
