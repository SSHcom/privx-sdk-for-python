# PrivX URLs.

from typing import Union

from privx_api.exceptions import InternalAPIException


class AuthEnum:
    AUTHORIZE = "AUTHORIZE"
    TOKEN = "TOKEN"

    urls = {
        AUTHORIZE: "/auth/api/v1/oauth/authorize",
        TOKEN: "/auth/api/v1/oauth/token",
    }


class HostStoreEnum:
    HOSTS = "HOSTS"
    HOST = "HOST"
    SEARCH_HOST = "SEARCH_HOST"

    urls = {
        HOSTS: "/host-store/api/v1/hosts",
        HOST: "/host-store/api/v1/hosts/{host_id}",
        SEARCH_HOST: "/host-store/api/v1/hosts/search",
    }


class RoleStoreEnum:
    ROLES = "ROLES"
    SOURCES = "SOURCES"
    MEMBERS = "MEMBERS"
    ROLE = "ROLE"
    RESOLVE = "RESOLVE"
    EVALUATE = "EVALUATE"
    PRINCIPAL_KEYS = "PRINCIPAL_KEYS"
    PRINCIPAL_KEY = "PRINCIPAL_KEY"
    GENERATE_PRINCIPAL_KEY = "GENERATE_PRINCIPAL_KEY"
    IMPORT_PRINCIPAL_KEY = "IMPORT_PRINCIPAL_KEY"
    AWS_ROLES = "AWS_ROLES"
    AWS_TOKEN = "AWS_TOKEN"
    SEARCH_USERS = "SEARCH_USERS"

    urls = {
        ROLES: "/role-store/api/v1/roles",
        SOURCES: "/role-store/api/v1/sources",
        MEMBERS: "/role-store/api/v1/roles/{role_id}/members",
        ROLE: "/role-store/api/v1/roles/{role_id}",
        RESOLVE: "/role-store/api/v1/roles/resolve",
        EVALUATE: "/role-store/api/v1/roles/evaluate",
        PRINCIPAL_KEYS: "/role-store/api/v1/roles/{role_id}/principalkeys",
        PRINCIPAL_KEY: (
            "/role-store/api/v1/roles/{role_id}/principalkeys/{principal_key_id}"
        ),
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/generate",
        IMPORT_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/import",
        AWS_ROLES: "/role-store/api/v1/users/current/awsroles",
        AWS_TOKEN: "/role-store/api/v1/roles/{awsrole_id}/awstoken",
        SEARCH_USERS: "/role-store/api/v1/users/search",
    }


class UserStoreEnum:
    STATUS = "STATUS"
    USERS = "USERS"
    USER = "USER"

    urls = {
        STATUS: "/local-user-store/api/v1/status",
        USERS: "/local-user-store/api/v1/users",
        USER: "/local-user-store/api/v1/users/{user_id}",
    }


class ConnectionManagerEnum:
    SEARCH_CONNECTION = "SEARCH_CONNECTION"

    urls = {SEARCH_CONNECTION: "/connection-manager/api/v1/connections/search"}


class VaultEnum:
    SECRET = "SECRET"

    urls = {SECRET: "/vault/api/v1/secrets/{name}"}


class UrlEnum:
    AUTH = AuthEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    HOST_STORE = HostStoreEnum
    ROLE_STORE = RoleStoreEnum
    USER_STORE = UserStoreEnum
    VAULT = VaultEnum

    @classmethod
    def get(cls, url_name: str) -> Union[str, None]:
        """
        looking for required url name among inner enums
        Args:
            url_name: str e.g. 'TOKEN'
        Returns:
            str e.g.'/auth/api/v1/oauth/token'
            None if url name not found
        """

        list_urls = list(
            filter(
                lambda inner_enum: inner_enum.urls.get(url_name),
                (
                    val
                    for key, val in cls.__dict__.items()
                    if key == key.upper() and not key.startswith("__")
                ),
            )
        )
        if len(list_urls) != 1 and list_urls is not None:
            raise InternalAPIException
        if list_urls:
            return list_urls[0].urls.get(url_name)
