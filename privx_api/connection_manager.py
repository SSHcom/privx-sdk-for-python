from http import HTTPStatus

from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum


class ConnectionManagerAPI(BasePrivXAPI):
    """
    Connection manager API.
    """

    def search_connections(
        self,
        offset: int = None,
        limit: int = None,
        sortkey: str = None,
        sortdir: str = None,
        **kw
    ) -> PrivXAPIResponse:

        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sortkey, sortdir=sortdir
        )

        response_status, data = self._http_post(
            UrlEnum.CONNECTION_MANAGER.SEARCH,
            query_params=search_params,
            body=kw,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
