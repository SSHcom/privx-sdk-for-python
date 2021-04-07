from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum


class VaultAPI(BasePrivXAPI):
    def get_secret(self, name: str) -> PrivXAPIResponse:
        response = self._http_get(UrlEnum.VAULT.SECRET, path_params={"name": name})
        return PrivXAPIResponse(response, 200)
