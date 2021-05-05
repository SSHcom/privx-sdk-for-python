# PrivX URLs.

from typing import Union

from privx_api.exceptions import InternalAPIException


class AuthEnum:
    AUTHORIZE = "AUTH.AUTHORIZE"
    TOKEN = "AUTH.TOKEN"
    STATUS = "AUTH.STATUS"

    urls = {
        AUTHORIZE: "/auth/api/v1/oauth/authorize",
        TOKEN: "/auth/api/v1/oauth/token",
        STATUS: "/auth/api/v1/status",
    }


class HostStoreEnum:
    DEPLOY = "HOST_STORE.DEPLOY"
    DEPLOYABLE = "HOST_STORE.DEPLOYABLE"
    DISABLE = "HOST_STORE.DISABLE"
    HOST = "HOST_STORE.HOST"
    HOSTS = "HOST_STORE.HOSTS"
    REALM = "HOST_STORE.REALM"
    RESOLVE = "HOST_STORE.RESOLVE"
    SEARCH = "HOST_STORE.SEARCH"
    SETTINGS = "HOST_STORE.SETTINGS"
    STATUS = "HOST_STORE.STATUS"
    TAGS = "HOST_STORE.TAGS"

    urls = {
        DEPLOY: "/host-store/api/v1/hosts/deploy",
        DEPLOYABLE: "/host-store/api/v1/hosts/{host_id}/deployable",
        DISABLE: "/host-store/api/v1/hosts/{host_id}/disabled",
        HOST: "/host-store/api/v1/hosts/{host_id}",
        HOSTS: "/host-store/api/v1/hosts",
        REALM: "/host-store/api/v1/realm/resolve",
        RESOLVE: "/host-store/api/v1/hosts/resolve",
        SEARCH: "/host-store/api/v1/hosts/search",
        SETTINGS: "/host-store/api/v1/settings/default_service_options",
        STATUS: "/host-store/api/v1/status",
        TAGS: "/host-store/api/v1/hosts/tags",
    }


class RoleStoreEnum:
    ALL_AUTHORIZED_KEYS = "ROLE_STORE.ALL_AUTHORIZED_KEYS"
    AWS_ROLE = "ROLE_STORE.AWS_ROLE"
    AWS_ROLES = "ROLE_STORE.AWS_ROLES"
    AWS_ROLE_PRIVX_ROLES = "ROLE_STORE.AWS_ROLE_PRIVX_ROLES"
    AWS_TOKEN = "ROLE_STORE.AWS_TOKEN"
    CURRENT_AWS_ROLES = "ROLE_STORE.CURRENT_AWS_ROLES"
    DISABLE_MFA = "ROLE_STORE.DISABLE_MFA"
    ENABLE_MFA = "ROLE_STORE.ENABLE_MFA"
    EVALUATE = "ROLE_STORE.EVALUATE"
    EXTERNAL_SEARCH = "ROLE_STORE.EXTERNAL_SEARCH"
    GENERATE_PRINCIPAL_KEY = "ROLE_STORE.GENERATE_PRINCIPAL_KEY"
    IMPORT_PRINCIPAL_KEY = "ROLE_STORE.IMPORT_PRINCIPAL_KEY"
    LOG_CONF_COLLECTOR = "ROLE_STORE.LOG_CONF_COLLECTOR"
    LOG_CONF_COLLECTORS = "ROLE_STORE.LOG_CONF_COLLECTORS"
    MEMBERS = "ROLE_STORE.MEMBERS"
    PRINCIPAL_KEY = "ROLE_STORE.PRINCIPAL_KEY"
    PRINCIPAL_KEYS = "ROLE_STORE.PRINCIPAL_KEYS"
    REFRESH_SOURCES = "ROLE_STORE.REFRESH_SOURCES"
    RESET_MFA = "ROLE_STORE.RESET_MFA"
    RESOLVE = "ROLE_STORE.RESOLVE"
    RESOLVE_AUTHORIZED_KEYS = "ROLE_STORE.RESOLVE_AUTHORIZED_KEYS"
    RESOLVE_USER = "ROLE_STORE.RESOLVE_USER"
    ROLE = "ROLE_STORE.ROLE"
    ROLES = "ROLE_STORE.ROLES"
    SEARCH_USERS = "ROLE_STORE.SEARCH_USERS"
    SOURCE = "ROLE_STORE.SOURCE"
    SOURCES = "ROLE_STORE.SOURCES"
    STATUS = "ROLE_STORE.STATUS"
    USERS = "ROLE_STORE.USERS"
    USER_AUTHORIZED_KEYS = "ROLE_STORE.USER_AUTHORIZED_KEYS"
    USER_AUTHORIZED_KEY_ID = "ROLE_STORE.USER_AUTHORIZED_KEY_ID"
    USER_ROLES = "ROLE_STORE.USER_ROLES"
    USER_SETTINGS = "ROLE_STORE.USER_SETTINGS"

    urls = {
        ALL_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys",
        AWS_ROLE: "/role-store/api/v1/awsroles/{awsrole_id}",
        AWS_ROLES: "/role-store/api/v1/awsroles",
        AWS_ROLE_PRIVX_ROLES: "/role-store/api/v1/awsroles/{awsrole_id}/roles",
        AWS_TOKEN: "/role-store/api/v1/roles/{awsrole_id}/awstoken",
        CURRENT_AWS_ROLES: "/role-store/api/v1/users/current/awsroles",
        DISABLE_MFA: "/role-store/api/v1/users/mfa/disable",
        ENABLE_MFA: "/role-store/api/v1/users/mfa/enable",
        EVALUATE: "/role-store/api/v1/roles/evaluate",
        EXTERNAL_SEARCH: "/role-store/api/v1/users/search/external",
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/generate",
        IMPORT_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/import",
        LOG_CONF_COLLECTOR: "/role-store/api/v1/logconf/collectors/{collector_id}",
        LOG_CONF_COLLECTORS: "/role-store/api/v1/logconf/collectors",
        MEMBERS: "/role-store/api/v1/roles/{role_id}/members",
        PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/{key_id}",
        PRINCIPAL_KEYS: "/role-store/api/v1/roles/{role_id}/principalkeys",
        REFRESH_SOURCES: "/role-store/api/v1/sources/refresh",
        RESET_MFA: "/role-store/api/v1/users/mfa/reset",
        RESOLVE: "/role-store/api/v1/roles/resolve",
        RESOLVE_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys/resolve",
        RESOLVE_USER: "/role-store/api/v1/users/{user_id}/resolve",
        ROLE: "/role-store/api/v1/roles/{role_id}",
        ROLES: "/role-store/api/v1/roles",
        SEARCH_USERS: "/role-store/api/v1/users/search",
        SOURCE: "/role-store/api/v1/sources/{source_id}",
        SOURCES: "/role-store/api/v1/sources",
        STATUS: "/role-store/api/v1/status",
        USERS: "/role-store/api/v1/users/{user_id}",
        USER_AUTHORIZED_KEYS: "/role-store/api/v1/users/{user_id}/authorizedkeys",
        USER_AUTHORIZED_KEY_ID: "/role-store/api/v1/users/{user_id}/authorizedkeys/{key_id}",
        USER_ROLES: "/role-store/api/v1/users/{user_id}/roles",
        USER_SETTINGS: "/role-store/api/v1/users/{user_id}/settings",
    }


class UserStoreEnum:
    API_CLIENT = "USER_STORE.API_CLIENT"
    API_CLIENTS = "USER_STORE.API_CLIENTS"
    EXTENDING_CLIENTS = "USER_STORE.EXTENDING_CLIENTS"
    STATUS = "USER_STORE.STATUS"
    TRUSTED_CLIENT = "USER_STORE.TRUSTED_CLIENT"
    TRUSTED_CLIENTS = "USER_STORE.TRUSTED_CLIENTS"
    USER = "USER_STORE.USER"
    USERS = "USER_STORE.USERS"
    USER_PASSWORD = "USER_STORE.USER_PASSWORD"
    USER_TAGS = "USER_STORE.USER_TAGS"

    urls = {
        API_CLIENT: "/local-user-store/api/v1/api-clients/{api_client_id}",
        API_CLIENTS: "/local-user-store/api/v1/api-clients",
        EXTENDING_CLIENTS: "/local-user-store/api/v1/extender-clients",
        STATUS: "/local-user-store/api/v1/status",
        TRUSTED_CLIENT: "/local-user-store/api/v1/trusted-clients/{trusted_client_id}",
        TRUSTED_CLIENTS: "/local-user-store/api/v1/trusted-clients",
        USER: "/local-user-store/api/v1/users/{user_id}",
        USERS: "/local-user-store/api/v1/users",
        USER_PASSWORD: "/local-user-store/api/v1/users/{user_id}/password",
        USER_TAGS: "/local-user-store/api/v1/users/tags",
    }


class ConnectionManagerEnum:
    ACCESS_ROLE = "CONNECTION_MANAGER.ACCESS_ROLE"
    CONNECTION = "CONNECTION_MANAGER.CONNECTION"
    CONNECTIONS = "CONNECTION_MANAGER.CONNECTIONS"
    CONNECTION_ACCESS_ROLE = "CONNECTION_MANAGER.CONNECTION_ACCESS_ROLE"
    CONNECTION_ACCESS_ROLES = "CONNECTION_MANAGER.CONNECTION_ACCESS_ROLES"
    SEARCH = "CONNECTION_MANAGER.SEARCH"
    STATUS = "CONNECTION_MANAGER.STATUS"
    TERMINATE_CONNECTION_ID = "CONNECTION_MANAGER.TERMINATE_CONNECTION_ID"
    TERMINATE_HOST_ID = "CONNECTION_MANAGER.TERMINATE_HOST_ID"
    TERMINATE_USER_ID = "CONNECTION_MANAGER.TERMINATE_USER_ID"
    TRAIL = "CONNECTION_MANAGER.TRAIL"
    TRAIL_LOG = "CONNECTION_MANAGER.TRAIL_LOG"
    TRAIL_LOG_SESSION_ID = "CONNECTION_MANAGER.TRAIL_LOG_SESSION_ID"
    TRAIL_SESSION_ID = "CONNECTION_MANAGER.TRAIL_SESSION_ID"

    urls = {
        ACCESS_ROLE: "/connection-manager/api/v1/connections/access_roles/{role_id}",
        CONNECTION: "/connection-manager/api/v1/connections/{connection_id}",
        CONNECTIONS: "/connection-manager/api/v1/connections",
        CONNECTION_ACCESS_ROLE: "/connection-manager/api/v1/connections/{connection_id}"
        "/access_roles/{role_id}",
        CONNECTION_ACCESS_ROLES: "/connection-manager/api/v1/connections/{connection_id}"
        "/access_roles",
        SEARCH: "/connection-manager/api/v1/connections/search",
        STATUS: "/connection-manager/api/v1/status",
        TERMINATE_CONNECTION_ID: "/connection-manager/api/v1/terminate/connection/{connection_id}",
        TERMINATE_HOST_ID: "/connection-manager/api/v1/terminate/host/{host_id}",
        TERMINATE_USER_ID: "/connection-manager/api/v1/terminate/user/{user_id}",
        TRAIL: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/file/{file_id}/{session_id}",
        TRAIL_LOG: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/log",
        TRAIL_LOG_SESSION_ID: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/log/{session_id}",
        TRAIL_SESSION_ID: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/file/{file_id}",
    }


class VaultEnum:
    METADATA = "VAULT.METADATA"
    SCHEMAS = "VAULT.SCHEMAS"
    SEARCH = "VAULT.SEARCH"
    SECRET = "VAULT.SECRET"
    SECRETS = "VAULT.SECRETS"
    STATUS = "VAULT.STATUS"

    urls = {
        METADATA: "/vault/api/v1/metadata/secrets/{name}",
        SCHEMAS: "/vault/api/v1/schemas",
        SEARCH: "/vault/api/v1/search/secrets",
        SECRET: "/vault/api/v1/secrets/{name}",
        SECRETS: "/vault/api/v1/secrets",
        STATUS: "/vault/api/v1/status",
    }


class LicenseManagerEnum:
    STATUS = "LICENSE_MANAGER.STATUS"
    LICENSE = "LICENSE_MANAGER.LICENSE"
    REFRESH = "LICENSE_MANAGER.REFRESH"
    OPT_IN = "LICENSE_MANAGER.OPT_IN"
    DEACTIVATE = "LICENSE_MANAGER.DEACTIVATE"

    urls = {
        STATUS: "/license-manager/api/v1/status",
        LICENSE: "/license-manager/api/v1/license",
        REFRESH: "/license-manager/api/v1/license/refresh",
        OPT_IN: "/license-manager/api/v1/license/optin",
        DEACTIVATE: "/license-manager/api/v1/license/deactivate",
    }


class MonitorServiceEnum:
    STATUS = "MONITOR.STATUS"
    COMPONENTS = "MONITOR.COMPONENTS"
    COMPONENT = "MONITOR.COMPONENT"
    SEARCH_AUDIT_EVENTS = "MONITOR.SEARCH_AUDIT_EVENTS"
    AUDIT_EVENTS = "MONITOR.AUDIT_EVENTS"
    AUDIT_EVENT_CODES = "MONITOR.AUDIT_EVENT_CODES"
    INSTANCE_STATUS = "MONITOR.INSTANCE_STATUS"
    TERMINATE_INSTANCES = "MONITOR.TERMINATE_INSTANCES"

    urls = {
        STATUS: "/monitor-service/api/v1/status",
        COMPONENTS: "/monitor-service/api/v1/components",
        COMPONENT: "/monitor-service/api/v1/components/{hostname}",
        SEARCH_AUDIT_EVENTS: "/monitor-service/api/v1/auditevents/search",
        AUDIT_EVENTS: "/monitor-service/api/v1/auditevents",
        AUDIT_EVENT_CODES: "/monitor-service/api/v1/auditevents/codes",
        INSTANCE_STATUS: "/monitor-service/api/v1/instance/status",
        TERMINATE_INSTANCES: "/monitor-service/api/v1/instance/exit",
    }


class PrivXSettingsEnum:
    SCOPE = "SETTINGS.SCOPE"
    SCOPE_SCHEMA = "SETTINGS.SCOPE_SCHEMA"
    SCOPE_SECTION = "SETTINGS.SCOPE_SECTION"
    SCOPE_SECTION_SCHEMA = "SETTINGS.SCOPE_SECTION_SCHEMA"
    STATUS = "SETTINGS.STATUS"

    urls = {
        SCOPE: "/settings/api/v1/settings/{scope}",
        SCOPE_SCHEMA: "/settings/api/v1/schema/{scope}",
        SCOPE_SECTION: "/settings/api/v1/settings/{scope}/{section}",
        SCOPE_SECTION_SCHEMA: "/settings/api/v1/schema/{scope}/{section}",
        STATUS: "/settings/api/v1/status",
    }


class WokFlowEngineEnum:
    STATUS = "WORKFLOW_ENGINE.STATUS"
    WORKFLOWS = "WORKFLOW_ENGINE.WORKFLOWS"
    WORKFLOW = "WORKFLOW_ENGINE.WORKFLOW"
    REQUESTS = "WORKFLOW_ENGINE.REQUESTS"
    REQUEST = "WORKFLOW_ENGINE.REQUEST"
    DECISION = "WORKFLOW_ENGINE.DECISION"
    SEARCH_REQUESTS = "WORKFLOW_ENGINE.SEARCH_REQUESTS"
    SETTINGS = "WORKFLOW_ENGINE.SEARCH_REQUESTS"
    TEST_SETTINGS = "WORKFLOW_ENGINE.TEST_SETTINGS"

    urls = {
        STATUS: "/workflow-engine/api/v1/status",
        WORKFLOWS: "/workflow-engine/api/v1/workflows",
        WORKFLOW: "/workflow-engine/api/v1/workflows/{workflow_id}",
        REQUESTS: "/workflow-engine/api/v1/requests",
        REQUEST: "/workflow-engine/api/v1/requests/{request_id}",
        DECISION: "/workflow-engine/api/v1/requests/{request_id}/decision",
        SEARCH_REQUESTS: "/workflow-engine/api/v1/requests/search",
        SETTINGS: "/workflow-engine/api/v1/settings",
        TEST_SETTINGS: "/workflow-engine/api/v1/testsmtp",
    }


class UrlEnum:
    AUTH = AuthEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    HOST_STORE = HostStoreEnum
    LICENSE = LicenseManagerEnum
    MONITOR = MonitorServiceEnum
    ROLE_STORE = RoleStoreEnum
    SETTINGS = PrivXSettingsEnum
    USER_STORE = UserStoreEnum
    VAULT = VaultEnum
    WORKFLOW_ENGINE = WokFlowEngineEnum

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
        if len(list_urls) != 1:
            raise InternalAPIException
        return list_urls[0].urls.get(url_name)
