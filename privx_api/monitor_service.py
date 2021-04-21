from http import HTTPStatus

from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum


class MonitorServiceAPI(BasePrivXAPI):
    def get_monitor_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.MONITOR.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_privx_components_status(self) -> PrivXAPIResponse:
        """
        Get all the deployed privx components status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.MONITOR.COMPONENTS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_privx_component_status(self, hostname: str) -> PrivXAPIResponse:
        """
        Get all the deployed privx components status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.MONITOR.COMPONENT, path_params={"hostname": hostname}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_audit_events(
        self,
        offset: int = None,
        limit: int = None,
        query: str = None,
        sortdir: str = None,
        fuzzycount: bool = None,
        audit_event_params: dict = None,
    ) -> PrivXAPIResponse:
        """
        Search for audit events.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            query=query,
            sortdir=sortdir,
            fuzzycount=fuzzycount,
        )
        response_status, data = self._http_post(
            UrlEnum.MONITOR.SEARCH_AUDIT_EVENTS,
            query_params=search_params,
            body=audit_event_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_audit_events(
        self,
        offset: int = None,
        limit: int = None,
        query: str = None,
        sortdir: str = None,
        fuzzycount: bool = None,
    ) -> PrivXAPIResponse:
        """
        Get all audit events.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            query=query,
            sortdir=sortdir,
            fuzzycount=fuzzycount,
        )
        response_status, data = self._http_get(
            UrlEnum.MONITOR.AUDIT_EVENTS, query_params=search_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_audit_event_codes(self) -> PrivXAPIResponse:
        """
        Get audit event codes.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.MONITOR.AUDIT_EVENT_CODES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_instance_status(self) -> PrivXAPIResponse:
        """
        Status of the whole instance.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.MONITOR.INSTANCE_STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def terminate_privx_instances(self) -> PrivXAPIResponse:
        """
        Terminate PrivX instances.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.MONITOR.TERMINATE_INSTANCES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
