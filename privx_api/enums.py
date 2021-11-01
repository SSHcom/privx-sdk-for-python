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
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys"
        "/generate",
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
        USER_AUTHORIZED_KEY_ID: "/role-store/api/v1/users/{user_id}/authorizedkeys"
        "/{key_id}",
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
        CONNECTION_ACCESS_ROLES: "/connection-manager/api/v1/connections"
        "/{connection_id}"
        "/access_roles",
        SEARCH: "/connection-manager/api/v1/connections/search",
        STATUS: "/connection-manager/api/v1/status",
        TERMINATE_CONNECTION_ID: "/connection-manager/api/v1/terminate/connection"
        "/{connection_id}",
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
    USER_SECRETS = "VAULT.USER_SECRETS"
    USER_SECRET = "VAULT.USER_SECRET"
    USER_SECRET_METADATA = "VAULT.USER_SECRET_METADATA"

    urls = {
        METADATA: "/vault/api/v1/metadata/secrets/{name}",
        SCHEMAS: "/vault/api/v1/schemas",
        SEARCH: "/vault/api/v1/search/secrets",
        SECRET: "/vault/api/v1/secrets/{name}",
        SECRETS: "/vault/api/v1/secrets",
        STATUS: "/vault/api/v1/status",
        USER_SECRETS: "/vault/api/v1/user/{user_id}/secrets",
        USER_SECRET: "/vault/api/v1/user/{user_id}/secrets/{name}",
        USER_SECRET_METADATA: "/vault/api/v1/user/{user_id}/metadata/secrets/{name}",
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
    AUDIT_EVENTS = "MONITOR.AUDIT_EVENTS"
    AUDIT_EVENT_CODES = "MONITOR.AUDIT_EVENT_CODES"
    COMPONENT = "MONITOR.COMPONENT"
    COMPONENTS = "MONITOR.COMPONENTS"
    INSTANCE_STATUS = "MONITOR.INSTANCE_STATUS"
    SEARCH_AUDIT_EVENTS = "MONITOR.SEARCH_AUDIT_EVENTS"
    STATUS = "MONITOR.STATUS"
    TERMINATE_INSTANCES = "MONITOR.TERMINATE_INSTANCES"

    urls = {
        AUDIT_EVENTS: "/monitor-service/api/v1/auditevents",
        AUDIT_EVENT_CODES: "/monitor-service/api/v1/auditevents/codes",
        COMPONENT: "/monitor-service/api/v1/components/{hostname}",
        COMPONENTS: "/monitor-service/api/v1/components",
        INSTANCE_STATUS: "/monitor-service/api/v1/instance/status",
        SEARCH_AUDIT_EVENTS: "/monitor-service/api/v1/auditevents/search",
        STATUS: "/monitor-service/api/v1/status",
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
    DECISION = "WORKFLOW_ENGINE.DECISION"
    REQUEST = "WORKFLOW_ENGINE.REQUEST"
    REQUESTS = "WORKFLOW_ENGINE.REQUESTS"
    SEARCH_REQUESTS = "WORKFLOW_ENGINE.SEARCH_REQUESTS"
    SETTINGS = "WORKFLOW_ENGINE.SETTINGS"
    STATUS = "WORKFLOW_ENGINE.STATUS"
    TEST_SETTINGS = "WORKFLOW_ENGINE.TEST_SETTINGS"
    WORKFLOW = "WORKFLOW_ENGINE.WORKFLOW"
    WORKFLOWS = "WORKFLOW_ENGINE.WORKFLOWS"

    urls = {
        DECISION: "/workflow-engine/api/v1/requests/{request_id}/decision",
        REQUEST: "/workflow-engine/api/v1/requests/{request_id}",
        REQUESTS: "/workflow-engine/api/v1/requests",
        SEARCH_REQUESTS: "/workflow-engine/api/v1/requests/search",
        SETTINGS: "/workflow-engine/api/v1/settings",
        STATUS: "/workflow-engine/api/v1/status",
        TEST_SETTINGS: "/workflow-engine/api/v1/testsmtp",
        WORKFLOW: "/workflow-engine/api/v1/workflows/{workflow_id}",
        WORKFLOWS: "/workflow-engine/api/v1/workflows",
    }


class TrailIndexEnum:
    CONNECTION_INDEXING_STATUS = "TRAIL_INDEX.CONNECTION_INDEXING_STATUS"
    CONNECTIONS_INDEXING_STATUSES = "TRAIL_INDEX.CONNECTIONS_INDEXING_STATUSES"
    SEARCH = "TRAIL_INDEX.SEARCH"
    START_INDEXING = "TRAIL_INDEX.START_INDEXING"
    STATUS = "TRAIL_INDEX.STATUS"

    urls = {
        CONNECTION_INDEXING_STATUS: "/trail-index/api/v1/index/{connection_id}/status",
        CONNECTIONS_INDEXING_STATUSES: "/trail-index/api/v1/index/status",
        SEARCH: "/trail-index/api/v1/index/search",
        START_INDEXING: "/trail-index/api/v1/index/start",
        STATUS: "/trail-index/api/v1/status",
    }


class AuthorizerEnum:
    ACCESS_GROUP = "AUTHORIZER.ACCESS_GROUP"
    ACCESS_GROUPS = "AUTHORIZER.ACCESS_GROUPS"
    AUTHORIZER_CERT = "AUTHORIZER.AUTHORIZER_CERT"
    AUTHORIZER_CERT_ID = "AUTHORIZER.AUTHORIZER_CERT_ID"
    CARRIER_CONFIG_SESSION_ID = "AUTHORIZER.CARRIER_CONFIG_SESSION_ID"
    CERT_AUTH_TEMPLATES = "AUTHORIZER.CERT_AUTH_TEMPLATES"
    CERT_REVOCATION_LIST = "AUTHORIZER.CERT_REVOCATION_LIST"
    COMPONENT_CERT = "AUTHORIZER.COMPONENT_CERT"
    COMPONENT_CERTS = "AUTHORIZER.COMPONENT_CERTS"
    COMPONENT_CERT_REVOCATION_LIST = "AUTHORIZER.COMPONENT_CERT_REVOCATION_LIST"
    CREATE_GROUP_PRINCIPAL_KEY = "AUTHORIZER.CREATE_GROUP_PRINCIPAL_KEY"
    DEPLOYMENT_SCRIPT_SESSION_ID = "AUTHORIZER.DEPLOYMENT_SCRIPT_SESSION_ID"
    DOWNLOAD_CARRIER_CONFIG = "AUTHORIZER.DOWNLOAD_CARRIER_CONFIG"
    DOWNLOAD_COMMAND_SCRIPT = "AUTHORIZER.DOWNLOAD_COMMAND_SCRIPT"
    DOWNLOAD_DEPLOYMENT_SCRIPT = "AUTHORIZER.DOWNLOAD_DEPLOYMENT_SCRIPT"
    DOWNLOAD_WEB_PROXY_CONFIG = "AUTHORIZER.DOWNLOAD_WEB_PROXY_CONFIG"
    EXTENDER_CONFIG = "AUTHORIZER.EXTENDER_CONFIG"
    EXTENDER_CONFIG_SESSION_ID = "AUTHORIZER.EXTENDER_CONFIG_SESSION_ID"
    EXTENDER_TRUST_ANCHOR = "AUTHORIZER.EXTENDER_TRUST_ANCHOR"
    GROUP_PRINCIPAL_KEY = "AUTHORIZER.GROUP_PRINCIPAL_KEY"
    IMPORT_GROUP_PRINCIPAL_KEY = "AUTHORIZER.IMPORT_GROUP_PRINCIPAL_KEY"
    PRINCIPALS = "AUTHORIZER.PRINCIPALS"
    SEARCH_ACCESS_GROUPS = "AUTHORIZER.SEARCH_ACCESS_GROUPS"
    SEARCH_CERTS = "AUTHORIZER.SEARCH_CERTS"
    SIGN_GROUP_PRINCIPAL_KEY = "AUTHORIZER.SIGN_GROUP_PRINCIPAL_KEY"
    SSL_TRUST_ANCHOR = "AUTHORIZER.SSL_TRUST_ANCHOR"
    STATUS = "AUTHORIZER.STATUS"
    TARGET_HOST = "AUTHORIZER.TARGET_HOST"
    WEB_PROXY_CONFIG_SESSION_ID = "AUTHORIZER.WEB_PROXY_CONFIG_SESSION_ID"

    urls = {
        ACCESS_GROUP: "/authorizer/api/v1/accessgroups/{id}",
        ACCESS_GROUPS: "/authorizer/api/v1/accessgroups",
        AUTHORIZER_CERT: "/authorizer/api/v1/cas",
        AUTHORIZER_CERT_ID: "/authorizer/api/v1/cas/{id}",
        CARRIER_CONFIG_SESSION_ID: "/authorizer/api/v1/carrier/conf"
        "/{trusted_client_id}",
        CERT_AUTH_TEMPLATES: "/authorizer/api/v1/cert/templates",
        CERT_REVOCATION_LIST: "/authorizer/api/v1/cas/{id}/crl",
        COMPONENT_CERT: "/authorizer/api/v1/{ca_type}/cas/{id}",
        COMPONENT_CERTS: "/authorizer/api/v1/{ca_type}/cas",
        COMPONENT_CERT_REVOCATION_LIST: "/authorizer/api/v1/{ca_type}/cas/{id}/crl",
        CREATE_GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}/create",
        DEPLOYMENT_SCRIPT_SESSION_ID: "/authorizer/api/v1/deploy/{trusted_client_id}",
        DOWNLOAD_CARRIER_CONFIG: "/authorizer/api/v1/carrier/conf/{trusted_client_id}"
        "/{session_id}",
        DOWNLOAD_COMMAND_SCRIPT: "/authorizer/api/v1/deploy/principals_command.sh",
        DOWNLOAD_DEPLOYMENT_SCRIPT: "/authorizer/api/v1/deploy/{trusted_client_id}/{"
        "session_id}",
        DOWNLOAD_WEB_PROXY_CONFIG: "/authorizer/api/v1/icap/conf/{trusted_client_id}"
        "/{session_id}",
        EXTENDER_CONFIG: "/authorizer/api/v1/extender/conf/{trusted_client_id}"
        "/{session_id}",
        EXTENDER_CONFIG_SESSION_ID: "/authorizer/api/v1/extender/conf"
        "/{trusted_client_id}",
        EXTENDER_TRUST_ANCHOR: "/authorizer/api/v1/extender-trust-anchor",
        GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}",
        IMPORT_GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}/import",
        PRINCIPALS: "/authorizer/api/v1/principals",
        SEARCH_ACCESS_GROUPS: "/authorizer/api/v1/accessgroups/search",
        SEARCH_CERTS: "/authorizer/api/v1/cert/search",
        SIGN_GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}/sign",
        SSL_TRUST_ANCHOR: "/authorizer/api/v1/ssl-trust-anchor",
        STATUS: "/authorizer/api/v1/status",
        TARGET_HOST: "/authorizer/api/v1/ca/authorize",
        WEB_PROXY_CONFIG_SESSION_ID: "/authorizer/api/v1/icap/conf/{trusted_client_id}",
    }


class UrlEnum:
    AUTH = AuthEnum
    AUTHORIZER = AuthorizerEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    HOST_STORE = HostStoreEnum
    LICENSE = LicenseManagerEnum
    MONITOR = MonitorServiceEnum
    ROLE_STORE = RoleStoreEnum
    SETTINGS = PrivXSettingsEnum
    TRAIL_INDEX = TrailIndexEnum
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
                cls.to_dict().values(),
            )
        )
        if len(list_urls) != 1:
            raise InternalAPIException
        return list_urls[0].urls.get(url_name)

    @classmethod
    def to_dict(cls) -> dict:
        return {
            key: val
            for key, val in cls.__dict__.items()
            if key == key.upper() and not key.startswith("__")
        }
