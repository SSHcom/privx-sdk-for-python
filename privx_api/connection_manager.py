from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse, PrivXStreamResponse
from privx_api.utils import get_value


class ConnectionManagerAPI(BasePrivXAPI):
    def get_connection_manager_service_status(self):
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.CONNECTION_MANAGER.STATUS, auth_required=False
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_connections(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get connections.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.CONNECTION_MANAGER.CONNECTIONS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_connections(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        connection_params: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for connections.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )

        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.SEARCH,
            query_params=search_params,
            body=get_value(connection_params, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_connection(self, connection_id: str) -> PrivXAPIResponse:
        """
        Get a single connection.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.CONNECTION_MANAGER.CONNECTION,
            path_params={"connection_id": connection_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_trail_download_handle(
        self, connection_id: str, channel_id: str, file_id: str
    ) -> PrivXAPIResponse:
        """
        Create session ID for trail stored file download.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.TRAIL_SESSION_ID,
            path_params={
                "connection_id": connection_id,
                "channel_id": channel_id,
                "file_id": file_id,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def download_trail(
        self,
        connection_id: str,
        channel_id: str,
        file_id: str,
        session_id: str,
    ) -> PrivXStreamResponse:
        """
        Download trail stored file transferred within audited connection channel.

        use object.iter_content() for consuming the chunked response

        Returns:
            StreamResponse
        """
        response_obj = self._http_stream(
            UrlEnum.CONNECTION_MANAGER.TRAIL,
            path_params={
                "connection_id": connection_id,
                "channel_id": channel_id,
                "file_id": file_id,
                "session_id": session_id,
            },
            auth_required=False,
        )
        return PrivXStreamResponse(response_obj, HTTPStatus.OK)

    def create_trail_log_download_handle(
        self, connection_id: str, channel_id: str
    ) -> PrivXAPIResponse:
        """
        Create session ID for trail stored file download.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.TRAIL_LOG,
            path_params={
                "connection_id": connection_id,
                "channel_id": channel_id,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def download_trail_log(
        self,
        connection_id: str,
        channel_id: str,
        session_id: str,
        format_param: Optional[str] = None,
        filter_param: Optional[str] = None,
    ) -> PrivXStreamResponse:
        """
        Download trail log of audited connection channel.

        use object.iter_content() for consuming the chunked response

        Returns:
            StreamResponse
        """
        search_params = self._get_search_params(
            format=format_param, filter=filter_param
        )
        response_obj = self._http_stream(
            UrlEnum.CONNECTION_MANAGER.TRAIL_LOG_SESSION_ID,
            path_params={
                "connection_id": connection_id,
                "channel_id": channel_id,
                "session_id": session_id,
            },
            query_params=search_params,
            auth_required=False,
        )
        return PrivXStreamResponse(response_obj, HTTPStatus.OK)

    def get_connection_access_roles(self, connection_id: str) -> PrivXAPIResponse:
        """
        Get saved access roles for a connection.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.CONNECTION_MANAGER.CONNECTION_ACCESS_ROLES,
            path_params={
                "connection_id": connection_id,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def grant_access_role_to_connection(
        self,
        connection_id: str,
        role_id: str,
    ) -> PrivXAPIResponse:
        """
        Grant a permission for a role for a connection.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.CONNECTION_ACCESS_ROLE,
            path_params={
                "connection_id": connection_id,
                "role_id": role_id,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def revoke_access_role_from_connection(
        self,
        connection_id: str,
        role_id: str,
    ) -> PrivXAPIResponse:
        """
        Revoke a permission for a role from a connection.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.CONNECTION_MANAGER.CONNECTION_ACCESS_ROLE,
            path_params={
                "connection_id": connection_id,
                "role_id": role_id,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def revoke_role_permissions_from_connections(
        self,
        role_id: str,
    ) -> PrivXAPIResponse:
        """
        Revoke permissions for a role from connections.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.CONNECTION_MANAGER.ACCESS_ROLE,
            path_params={
                "role_id": role_id,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def terminate_connection(
        self,
        connection_id: str,
        termination_params: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Terminate connection by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.TERMINATE_CONNECTION_ID,
            path_params={
                "connection_id": connection_id,
            },
            body=termination_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def terminate_connection_by_host(
        self,
        host_id: str,
        termination_params: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Terminate connection by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.TERMINATE_HOST_ID,
            path_params={
                "host_id": host_id,
            },
            body=termination_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def terminate_connection_by_user(
        self,
        user_id: str,
        termination_params: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Terminate connection(s) of a user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.TERMINATE_USER_ID,
            path_params={
                "user_id": user_id,
            },
            body=termination_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
