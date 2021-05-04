from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class SettingsServiceAPI(BasePrivXAPI):
    def get_settings_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.SETTINGS.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_scope_settings(
        self, scope: str, merge: Optional[bool] = None
    ) -> PrivXAPIResponse:
        """
        Get settings for the scope.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SETTINGS.SCOPE,
            path_params={"scope": scope},
            query_params=self._get_search_params(merge=merge),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_scope_settings(self, scope: str, scope_params: dict) -> PrivXAPIResponse:
        """
        Update settings for a scope.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SETTINGS.SCOPE,
            path_params={"scope": scope},
            body=scope_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_scope_section_settings(self, scope: str, section: str) -> PrivXAPIResponse:
        """
        Get settings for the scope section.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SETTINGS.SCOPE_SECTION,
            path_params={"scope": scope, "section": section},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_scope_section_settings(
        self, scope: str, section: str, section_params: dict
    ) -> PrivXAPIResponse:
        """
        Update settings for a scope and section combination.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SETTINGS.SCOPE_SECTION,
            path_params={"scope": scope, "section": section},
            body=section_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_scope_schema(self, scope: str) -> PrivXAPIResponse:
        """
        Get schema for the scope.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SETTINGS.SCOPE_SCHEMA,
            path_params={"scope": scope},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_scope_section_schema(self, scope: str, section: str) -> PrivXAPIResponse:
        """
        Get schema for the scope section.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SETTINGS.SCOPE_SECTION_SCHEMA,
            path_params={"scope": scope, "section": section},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
