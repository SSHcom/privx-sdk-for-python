from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI


class RoleStoreAPI(BasePrivXAPI):
    """
    Role store API.
    """

    def create_role(self, role: dict) -> PrivXAPIResponse:
        """
        Create a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post(UrlEnum.ROLE_STORE.ROLES, body=role)
        return PrivXAPIResponse(response, 201)

    def delete_role(self, role_id: str) -> PrivXAPIResponse:
        """
        Delete role by ID.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_delete(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}
        )
        return PrivXAPIResponse(response, 200)

    def delete_principal_key(self, role_id: str, key_id: str) -> PrivXAPIResponse:
        """
        Delete a role's principal key object.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_delete(
            UrlEnum.ROLE_STORE.PRINCIPAL_KEY,
            path_params={"role_id": role_id, "key_id": key_id},
        )
        return PrivXAPIResponse(response, 200)

    def evaluate_role(self, role_params: dict) -> PrivXAPIResponse:
        """
        Evaluate a new role definition, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post(UrlEnum.ROLE_STORE.EVALUATE, body=role_params)
        return PrivXAPIResponse(response, 200)

    def import_principal_key(self, role_id: str, primary_key: dict) -> PrivXAPIResponse:
        """
        Import new principal key for role.

        primary_key = {"primary_key" : "----row1----\nrow2\nrow3..."}

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post(
            UrlEnum.ROLE_STORE.IMPORT_PRINCIPAL_KEY,
            path_params={"role_id": role_id},
            body=primary_key,
        )
        return PrivXAPIResponse(response, 201)

    def get_roles(self) -> PrivXAPIResponse:
        """
        Get roles.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get(UrlEnum.ROLE_STORE.ROLES)
        return PrivXAPIResponse(response, 200)

    def get_role_by_id(self, role_id: str) -> PrivXAPIResponse:
        """
        Get role object by ID.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}
        )
        return PrivXAPIResponse(response, 200)

    def get_sources(self) -> PrivXAPIResponse:
        """
        Get sources.

        Returns:
            PrivxAPIResponse
        """
        response = self._http_get(UrlEnum.ROLE_STORE.SOURCES)
        return PrivXAPIResponse(response, 200)

    def get_role_members(
        self,
        role_id: str,
        offset: int = None,
        limit: int = None,
        sortkey: str = None,
        sortdir: str = None,
    ) -> PrivXAPIResponse:
        """
        Get Role Members.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sortkey, sortdir=sortdir
        )
        response = self._http_get(
            UrlEnum.ROLE_STORE.MEMBERS,
            path_params={"role_id": role_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response, 200)

    def get_principal_keys(self, role_id: str) -> PrivXAPIResponse:
        """
        Get role's principal key objects.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get(
            UrlEnum.ROLE_STORE.PRINCIPAL_KEYS, path_params={"role_id": role_id}
        )
        return PrivXAPIResponse(response, 200)

    def get_principal_key(self, role_id: str, key_id: str) -> PrivXAPIResponse:
        """
        Get role's principal key object.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get(
            UrlEnum.ROLE_STORE.PRINCIPAL_KEY,
            path_params={"role_id": role_id, "key_id": key_id},
        )
        return PrivXAPIResponse(response, 200)

    def generate_principal_key(self, role_id: str) -> PrivXAPIResponse:
        """
        Generate new principal key for role.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post(
            UrlEnum.ROLE_STORE.GENERATE_PRINCIPAL_KEY,
            path_params={"role_id": role_id},
        )
        return PrivXAPIResponse(response, 201)

    def update_role(self, role_id: str, role: dict) -> PrivXAPIResponse:
        """
        Update a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_put(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}, body=role
        )
        return PrivXAPIResponse(response, 200)

    def search_users(
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

        response = self._http_post(
            UrlEnum.ROLE_STORE.SEARCH_USERS, query_params=search_params, body=kw
        )
        return PrivXAPIResponse(response, 200)

    def resolve_role(self, role_names: list) -> PrivXAPIResponse:
        """
        Resolve role names to role IDs.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_post(UrlEnum.ROLE_STORE.RESOLVE, body=role_names)
        return PrivXAPIResponse(response, 200)

    #
    # List accessible AWS roles.
    #

    def list_awsroles(self) -> PrivXAPIResponse:
        """
        Get AWS roles.

        Returns:
            PrivXAPIResponse
        """
        response = self._http_get(UrlEnum.ROLE_STORE.AWS_ROLES)
        return PrivXAPIResponse(response, response.status)

    # Fetch temporary AWS token for given AWS role name and TTL.
    # User needs to have the requested AWS role mapped to the available PrivX role by PrivX admin.
    # Allowed TTL values 900-3600 seconds for assume-role (configurable max 43200) and 900-129600
    # for federation token.

    def get_awstoken(
        self, awsrole_id: str, ttl: int = 900, tokencode: str = None
    ) -> PrivXAPIResponse:
        """
        Get temporary AWS token for given AWS role.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(ttl=ttl, tokencode=tokencode)
        response = self._http_get(
            UrlEnum.ROLE_STORE.AWS_TOKEN,
            path_params={"awsrole_id": awsrole_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response, 200)
