from http import HTTPStatus

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class DbProxyAPI(BasePrivXAPI):
    """
    PrivX Database Proxy API
    """

    def get_db_proxy_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.DB_PROXY.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_db_proxy_conf(self) -> PrivXAPIResponse:
        """
        Get DB proxy configuration.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.DB_PROXY.CONF)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
