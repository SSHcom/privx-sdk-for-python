from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class VaultAPI(BasePrivXAPI):
    def get_vault_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.VAULT.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_secret(self, secret_params: dict) -> PrivXAPIResponse:
        """
        Create a secret.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.VAULT.SECRETS,
            body=secret_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_secrets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PrivXAPIResponse:
        """
        Get secrets client has access.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(offset=offset, limit=limit)
        response_status, data = self._http_get(
            UrlEnum.VAULT.SECRETS, query_params=search_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_secret(self, name: str) -> PrivXAPIResponse:
        """
        get a secret.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.VAULT.SECRET, path_params={"name": name}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_secret(self, name: str, secret_params: dict) -> PrivXAPIResponse:
        """
        Update a secret.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.VAULT.SECRET,
            path_params={"name": name},
            body=secret_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_secret(self, name: str) -> PrivXAPIResponse:
        """
        Delete a secret.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.VAULT.SECRET,
            path_params={"name": name},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_secret_metadata(self, name: str) -> PrivXAPIResponse:
        """
        Get a secret's metadata.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.VAULT.METADATA, path_params={"name": name}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_secrets(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for secrets.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_post(
            UrlEnum.VAULT.SEARCH,
            query_params=search_params,
            body=search_payload or {},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_vault_schemas(self) -> PrivXAPIResponse:
        """
        Returns the defined schemas.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.VAULT.SCHEMAS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
