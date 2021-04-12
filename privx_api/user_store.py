from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum


class UserStoreAPI(BasePrivXAPI):
    """
    User store API.
    """

    def create_local_user(self, user: dict) -> PrivXAPIResponse:
        """
        Create a user, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response, data = self._http_post(UrlEnum.USER_STORE.USERS, body=user)
        return PrivXAPIResponse(response, 201, data)

    def get_local_users(
        self,
        username=None,
        user_id=None,
        offset: int = None,
        limit: int = None,
    ) -> PrivXAPIResponse:
        """
        Get users.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, username=username, id=user_id
        )

        response, data = self._http_get(
            UrlEnum.USER_STORE.USERS, query_params=search_params
        )
        return PrivXAPIResponse(response, 200, data)

    def delete_local_user(self, user_id: str) -> PrivXAPIResponse:
        """
        Delete a local user, required field user_id.

        Returns:
            PrivXAPIResponse
        """
        response, data = self._http_delete(
            UrlEnum.USER_STORE.USER, path_params={"user_id": user_id}
        )
        return PrivXAPIResponse(response, 200, data)
