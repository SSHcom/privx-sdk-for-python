from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class UserStoreAPI(BasePrivXAPI):
    def get_user_store_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.STATUS, auth_required=False
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_users(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PrivXAPIResponse:
        """
        Get users.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, username=username, id=user_id
        )

        response_status, data = self._http_get(
            UrlEnum.USER_STORE.USERS, query_params=search_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_user(self, user: dict) -> PrivXAPIResponse:
        """
        Create a user, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.USER_STORE.USERS, body=user)
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_user(self, user_id: str) -> PrivXAPIResponse:
        """
        Get a user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.USER,
            path_params={"user_id": user_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_user(self, user_id: str, user_params: dict) -> PrivXAPIResponse:
        """
        Update a new user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.USER_STORE.USER,
            path_params={"user_id": user_id},
            body=user_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_user(self, user_id: str) -> PrivXAPIResponse:
        """
        Delete a local user, required field user_id.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.USER_STORE.USER, path_params={"user_id": user_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_user_password(self, user_id: str, user_password: dict) -> PrivXAPIResponse:
        """
        Set user's password.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.USER_STORE.USER_PASSWORD,
            path_params={"user_id": user_id},
            body=user_password,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_tags(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        query: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get list of host's tags.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, query=query, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.USER_TAGS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_trusted_clients(self) -> PrivXAPIResponse:
        """
        Gets trusted clients.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.TRUSTED_CLIENTS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_trusted_client(self, client_params: dict) -> PrivXAPIResponse:
        """
        Create a new trusted client. ID, client_secret, author,
        created, updated, and updated_by fields are automatically populated
        by the server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.USER_STORE.TRUSTED_CLIENTS,
            body=client_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_trusted_client(self, client_id: str) -> PrivXAPIResponse:
        """
        Gets trusted client object by id.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.TRUSTED_CLIENT,
            path_params={"trusted_client_id": client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_trusted_client(self, client_id: str) -> PrivXAPIResponse:
        """
        Delete a trusted client by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.USER_STORE.TRUSTED_CLIENT,
            path_params={"trusted_client_id": client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_trusted_client(
        self, client_id: str, client_params: dict
    ) -> PrivXAPIResponse:
        """
        Update a trusted client.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.USER_STORE.TRUSTED_CLIENT,
            path_params={"trusted_client_id": client_id},
            body=client_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_extending_clients(self) -> PrivXAPIResponse:
        """
        Gets a list of extender client names.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.EXTENDING_CLIENTS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_api_clients(self) -> PrivXAPIResponse:
        """
        Gets API clients.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.API_CLIENTS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_api_client(self, api_client_params: dict) -> PrivXAPIResponse:
        """
        Create a new API client.
        ID, client_secret, author, created, updated,
        and updated_by fields are automatically populated by the server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.USER_STORE.API_CLIENTS,
            body=api_client_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_api_client(self, api_client_id: str) -> PrivXAPIResponse:
        """
        Gets API client object by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.USER_STORE.API_CLIENT,
            path_params={"api_client_id": api_client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_api_client(self, api_client_id: str) -> PrivXAPIResponse:
        """
        Delete an API client by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.USER_STORE.API_CLIENT,
            path_params={"api_client_id": api_client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_api_client(
        self, api_client_id: str, api_client_params: dict
    ) -> PrivXAPIResponse:
        """
        Update an API client.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.USER_STORE.API_CLIENT,
            path_params={"api_client_id": api_client_id},
            body=api_client_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
