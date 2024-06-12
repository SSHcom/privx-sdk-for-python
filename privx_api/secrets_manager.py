from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.utils import get_value

class SecretsManagerAPI(BasePrivXAPI):
    def get_secrets_manager_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.SECRETS_MANAGER.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_password_policies(self) -> PrivXAPIResponse:
        """
        Get password policies.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.SECRETS_MANAGER.PASSWORD_POLICIES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_password_policy(self, source_params: dict) -> PrivXAPIResponse:
        """
        Create a new password policy.
        Id, author, created & updated are automatically populated by the PrivX server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.CREATE_PASSWORD_POLICY, body=source_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_password_policy(self, id: str) -> PrivXAPIResponse:
        """
        Get password policy by ID.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.PASSWORD_POLICY, path_params={"id": id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_password_policy(self, id: str, policy_params: dict) -> PrivXAPIResponse:
        """
        Update a password policy.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SECRETS_MANAGER.PASSWORD_POLICY,
            path_params={"id": id},
            body=policy_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_password_policy(self, id: str) -> PrivXAPIResponse:
        """
        Delete password policy by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.SECRETS_MANAGER.PASSWORD_POLICY, path_params={"id": id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def rotate_host_password(self, host_id: str, account: str) -> PrivXAPIResponse:
        """
        Rotate a host password.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.ROTATE_HOST_PASSWORD,
            path_params={"host_id": host_id, "account": account},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_script_templates(self) -> PrivXAPIResponse:
        """
        Get script templates.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.SECRETS_MANAGER.SCRIPT_TEMPLATES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_script_template(self, template_params: dict) -> PrivXAPIResponse:
        """
        Create a new script template.
        Id, author, created & updated are automatically populated by the PrivX server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.CREATE_SCRIPT_TEMPLATE, body=template_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_script_template(self, id: str) -> PrivXAPIResponse:
        """
        Get script template by ID.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.SCRIPT_TEMPLATE, path_params={"id": id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_script_template(self, id: str, template_params: dict) -> PrivXAPIResponse:
        """
        Update a script template.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SECRETS_MANAGER.SCRIPT_TEMPLATE,
            path_params={"id": id},
            body=template_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_script_template(self, id: str) -> PrivXAPIResponse:
        """
        Delete script template by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.SECRETS_MANAGER.SCRIPT_TEMPLATE, path_params={"id": id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def compile_script_template(self, template_params: dict) -> PrivXAPIResponse:
        """
        Compile script with test data.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.COMPILE_SCRIPT_TEMPLATE,
            body=template_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_target_domains(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get target domains.

        Returns:
            PrivxAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAINS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_target_domain(self, td_params: dict) -> PrivXAPIResponse:
        """
        Create a new target domain.
        Id, author, created & updated are automatically populated by the PrivX server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAINS, body=td_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def search_target_domain(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:

        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )

        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.SEARCH_TARGET_DOMAINS,
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_target_domain(self, target_domain_id: str) -> PrivXAPIResponse:
        """
        Get target domain by ID.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN, path_params={"target_domain_id": target_domain_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_target_domain(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Update a target domain.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_target_domain(self, target_domain_id: str) -> PrivXAPIResponse:
        """
        Delete target domain by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN, path_params={"target_domain_id": target_domain_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def refresh_target_domain(self, target_domain_id: str) -> PrivXAPIResponse:
        """
        Trigger target domain account scan.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN, path_params={"target_domain_id": target_domain_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_target_domain_accounts(
        self,
        target_domain_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get all accounts in target domain.

        Returns:
            PrivxAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_target_domain_accounts(
        self,
        target_domain_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search accounts in target domain.

        Returns:
            PrivxAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )

        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.SEARCH_TARGET_DOMAIN_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_target_domain_account(self, target_domain_id: str, account_id: str) -> PrivXAPIResponse:
        """
        Get target domain account.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "account_id": account_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_target_domain_account(self, target_domain_id: str, account_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Update a target domain account.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "account_id": account_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def batch_update_target_domain_account(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Update a target domain account in batch.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SECRETS_MANAGER.BATH_UPDATE_TARGET_DOMAIN_ACCOUNT,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_target_domain_managed_accounts(
        self,
        target_domain_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get all managed accounts in a target domain.

        Returns:
            PrivxAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_target_domain_managed_account(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Create a managed account.
        Id, author, created & updated are automatically populated by the PrivX server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def search_target_domain_managed_accounts(
        self,
        target_domain_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search managed accounts in a target domain.

        Returns:
            PrivxAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )

        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.SEARCH_TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_target_domain_managed_account(self, target_domain_id: str, managed_account_id: str) -> PrivXAPIResponse:
        """
        Get managed account.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_MANAGED_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "managed_account_id": managed_account_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_target_domain_managed_account(self, target_domain_id: str, managed_account_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Update a managed account.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_MANAGED_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "managed_account_id": managed_account_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_target_domain_managed_account(self, target_domain_id: str, managed_account_id: str) -> PrivXAPIResponse:
        """
        Delete a managed account by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.SECRETS_MANAGER.TARGET_DOMAIN_MANAGED_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "managed_account_id": managed_account_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def rotate_target_domain_managed_account(self, target_domain_id: str, managed_account_id: str) -> PrivXAPIResponse:
        """
        Trigger managed account password rotation.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.ROTATE_TARGET_DOMAIN_MANAGED_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "managed_account_id": managed_account_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def password_target_domain_managed_account(self, target_domain_id: str, managed_account_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Provide password for managed account.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.PASSWORD_TARGET_DOMAIN_MANAGED_ACCOUNT,
            path_params={"target_domain_id": target_domain_id, "managed_account_id": managed_account_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def batch_create_target_domain_managed_account(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Create a batch of managed accounts.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.BATCH_CREATE_TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def batch_update_target_domain_managed_account(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Update a batch of managed accounts.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.BATCH_UPDATE_TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def batch_delete_target_domain_managed_account(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Delete a batch of managed accounts.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.BATCH_DELETE_TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def batch_rotate_target_domain_managed_account(self, target_domain_id: str, td_params: dict) -> PrivXAPIResponse:
        """
        Trigger password rotation for a batch of managed accounts.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.SECRETS_MANAGER.BATCH_ROTATE_TARGET_DOMAIN_MANAGED_ACCOUNTS,
            path_params={"target_domain_id": target_domain_id},
            body=td_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
