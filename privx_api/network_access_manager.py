from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.utils import get_value


class NetworkAccessManagerAPI(BasePrivXAPI):
    def get_network_manager_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.NETWORK_ACCESS_MANAGER.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_network_target(
        self,
        network_target_id: str,
    ):
        response_status, data = self._http_get(
            UrlEnum.NETWORK_ACCESS_MANAGER.NETWORK_TARGET,
            path_params={"network_target_id": network_target_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_network_targets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        filter_param: Optional[str] = None,
    ):
        get_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )
        response_status, data = self._http_get(
            UrlEnum.NETWORK_ACCESS_MANAGER.NETWORK_TARGETS,
            query_params=get_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_network_target(self, network_target: dict):
        response_status, data = self._http_post(
            UrlEnum.NETWORK_ACCESS_MANAGER.NETWORK_TARGETS,
            body=network_target,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def update_network_target(self, network_target_id: str, network_target: dict):
        response_status, data = self._http_put(
            UrlEnum.NETWORK_ACCESS_MANAGER.NETWORK_TARGET,
            path_params={"network_target_id": network_target_id},
            body=network_target,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def disable_network_target(self, network_target_id: str, disabled: dict):
        response_status, data = self._http_put(
            UrlEnum.NETWORK_ACCESS_MANAGER.DISABLE_NETWORK_TARGET,
            path_params={"network_target_id": network_target_id},
            body=disabled,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_network_target(self, network_target_id: str):
        response_status, data = self._http_delete(
            UrlEnum.NETWORK_ACCESS_MANAGER.NETWORK_TARGET,
            path_params={"network_target_id": network_target_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_network_targets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        filter_param: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for network-targets

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )

        response_status, data = self._http_post(
            UrlEnum.NETWORK_ACCESS_MANAGER.SEARCH_NETWORK_TARGETS,
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
