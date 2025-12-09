from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.utils import get_value


class ApiProxyAPI(BasePrivXAPI):
    def get_api_proxy_status(self) -> PrivXAPIResponse:
        """
        Get API-Proxy microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.API_PROXY.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_api_proxy_configuration(self) -> PrivXAPIResponse:
        """
        Fetch API-Proxy configuration.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.API_PROXY.CONFIGURATION)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_api_target(self, api_target: dict) -> PrivXAPIResponse:
        """
        Create a new API target.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.API_PROXY.API_TARGETS,
            body=api_target,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_api_targets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        filter_param: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        List API targets.

        Returns:
            PrivXAPIResponse
        """
        query_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.API_TARGETS,
            query_params=query_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_api_target(self, api_target_id: str) -> PrivXAPIResponse:
        """
        Fetch a single API target by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.API_TARGET,
            path_params={"api_target_id": api_target_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_api_target(
        self,
        api_target_id: str,
        api_target: dict,
    ) -> PrivXAPIResponse:
        """
        Update an API target by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.API_PROXY.API_TARGET,
            path_params={"api_target_id": api_target_id},
            body=api_target,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_api_target(self, api_target_id: str) -> PrivXAPIResponse:
        """
        Delete an API target by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.API_PROXY.API_TARGET,
            path_params={"api_target_id": api_target_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_api_targets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        filter_param: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for API targets with optional criteria.

        Returns:
            PrivXAPIResponse
        """
        query_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )
        response_status, data = self._http_post(
            UrlEnum.API_PROXY.API_TARGET_SEARCH,
            query_params=query_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_api_target_tags(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        List tags defined for API targets.

        Returns:
            PrivXAPIResponse
        """
        query_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortdir=sort_dir,
        )
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.API_TARGET_TAGS,
            query_params=query_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_current_user_client_credential(
        self,
        credential: dict,
    ) -> PrivXAPIResponse:
        """
        Create a client credential for the current user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.API_PROXY.CURRENT_CLIENT_CREDENTIALS,
            body=credential,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_current_user_client_credentials(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        List client credentials owned by the current user.

        Returns:
            PrivXAPIResponse
        """
        query_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.CURRENT_CLIENT_CREDENTIALS,
            query_params=query_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_current_user_client_credential(
        self,
        credential_id: str,
    ) -> PrivXAPIResponse:
        """
        Fetch a current user's client credential by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.CURRENT_CLIENT_CREDENTIAL,
            path_params={"credential_id": credential_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_current_user_client_credential(
        self,
        credential_id: str,
        credential: dict,
    ) -> PrivXAPIResponse:
        """
        Update a client credential owned by the current user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.API_PROXY.CURRENT_CLIENT_CREDENTIAL,
            path_params={"credential_id": credential_id},
            body=credential,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_current_user_client_credential(
        self,
        credential_id: str,
    ) -> PrivXAPIResponse:
        """
        Delete a current user's client credential by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.API_PROXY.CURRENT_CLIENT_CREDENTIAL,
            path_params={"credential_id": credential_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_current_user_client_credential_secret(
        self,
        credential_id: str,
    ) -> PrivXAPIResponse:
        """
        Get a current user's client credential secret.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.CURRENT_CLIENT_CREDENTIAL_SECRET,
            path_params={"credential_id": credential_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_user_client_credential(
        self,
        user_id: str,
        credential: dict,
    ) -> PrivXAPIResponse:
        """
        Create a client credential for a specific user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.API_PROXY.USER_CLIENT_CREDENTIALS,
            path_params={"user_id": user_id},
            body=credential,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_user_client_credentials(
        self,
        user_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        List client credentials for a specific user.

        Returns:
            PrivXAPIResponse
        """
        query_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.USER_CLIENT_CREDENTIALS,
            path_params={"user_id": user_id},
            query_params=query_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_client_credential(
        self,
        user_id: str,
        credential_id: str,
    ) -> PrivXAPIResponse:
        """
        Fetch a client credential for a specific user by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.USER_CLIENT_CREDENTIAL,
            path_params={"user_id": user_id, "credential_id": credential_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_user_client_credential(
        self,
        user_id: str,
        credential_id: str,
        credential: dict,
    ) -> PrivXAPIResponse:
        """
        Update a user-owned client credential by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.API_PROXY.USER_CLIENT_CREDENTIAL,
            path_params={"user_id": user_id, "credential_id": credential_id},
            body=credential,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_user_client_credential(
        self,
        user_id: str,
        credential_id: str,
    ) -> PrivXAPIResponse:
        """
        Delete a user-owned client credential by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.API_PROXY.USER_CLIENT_CREDENTIAL,
            path_params={"user_id": user_id, "credential_id": credential_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_client_credential_secret(
        self,
        user_id: str,
        credential_id: str,
    ) -> PrivXAPIResponse:
        """
        Fetch a user-owned client credential secret by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.API_PROXY.USER_CLIENT_CREDENTIAL_SECRET,
            path_params={"user_id": user_id, "credential_id": credential_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
