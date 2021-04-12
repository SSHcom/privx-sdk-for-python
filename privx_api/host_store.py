from http import HTTPStatus

from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum


class HostStoreAPI(BasePrivXAPI):
    """
    Host store API.
    """

    def create_host(self, host: dict) -> PrivXAPIResponse:
        """
        Create a host, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.HOST_STORE.HOSTS, body=host)
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def update_host(self, host_id: str, host: dict) -> PrivXAPIResponse:
        """
        Update a host, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.HOST_STORE.HOST, path_params={"host_id": host_id}, body=host
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_hosts(self) -> PrivXAPIResponse:
        """
        Get hosts.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.HOST_STORE.HOSTS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_hosts(
        self,
        offset: int = None,
        limit: int = None,
        sortkey: str = None,
        sortdir: str = None,
        filter_param: str = None,
        **kw
    ) -> PrivXAPIResponse:

        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sortkey,
            sortdir=sortdir,
            filter=filter_param,
        )

        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.SEARCH, query_params=search_params, body=kw
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_host(self, host_id: str) -> PrivXAPIResponse:
        """
        Delete host record, required field host_id.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.HOST_STORE.HOST, path_params={"host_id": host_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
