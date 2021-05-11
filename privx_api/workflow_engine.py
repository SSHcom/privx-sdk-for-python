from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class WorkFlowEngineAPI(BasePrivXAPI):
    def get_workflow_engine_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.WORKFLOW_ENGINE.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_workflows(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PrivXAPIResponse:
        """
        Get workflow objects.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
        )
        response_status, data = self._http_get(
            UrlEnum.WORKFLOW_ENGINE.WORKFLOWS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_workflow(self, workflow_params: dict) -> PrivXAPIResponse:
        """
        Create a new workflow.
        ID, author, created, and updated fields are automatically populated by the server..

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.WORKFLOW_ENGINE.WORKFLOWS,
            body=workflow_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_workflow(self, workflow_id: str) -> PrivXAPIResponse:
        """
        Get workflow object by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.WORKFLOW_ENGINE.WORKFLOW, path_params={"workflow_id": workflow_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_workflow(self, workflow_id: str) -> PrivXAPIResponse:
        """
        Deletes workflow by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.WORKFLOW_ENGINE.WORKFLOW, path_params={"workflow_id": workflow_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_workflow(
        self, workflow_id: str, workflow_params: dict
    ) -> PrivXAPIResponse:
        """
        Update a workflow.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.WORKFLOW_ENGINE.WORKFLOW,
            path_params={"workflow_id": workflow_id},
            body=workflow_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_requests(
        self,
        filter_param: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> PrivXAPIResponse:
        """
        Get the request queue for the user.
        filter param could be one of the following values:
        requests, active_approvals, approvals, active_requests, all.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            filter=filter_param,
            offset=offset,
            limit=limit,
        )
        response_status, data = self._http_get(
            UrlEnum.WORKFLOW_ENGINE.REQUESTS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_request(
        self,
        request_params: dict,
    ) -> PrivXAPIResponse:
        """
        Add a workflow to the request queue.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.WORKFLOW_ENGINE.REQUESTS,
            body=request_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_request(self, request_id: str) -> PrivXAPIResponse:
        """
        Gets a request object by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.WORKFLOW_ENGINE.REQUEST,
            path_params={"request_id": request_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_request(self, request_id: str) -> PrivXAPIResponse:
        """
        Delete Request item by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.WORKFLOW_ENGINE.REQUEST,
            path_params={"request_id": request_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_request_decision(
        self, request_id: str, decision_params: dict
    ) -> PrivXAPIResponse:
        """
        Update a request in queue.
        Only users with matching role are permitted
        to change the status of a step requiring such role..

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.WORKFLOW_ENGINE.DECISION,
            path_params={"request_id": request_id},
            body=decision_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_requests(
        self,
        filter_param: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        request_param: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search access requests.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )
        response_status, data = self._http_post(
            UrlEnum.WORKFLOW_ENGINE.SEARCH_REQUESTS,
            query_params=search_params,
            body=request_param,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_workflow_engine_settings(self) -> PrivXAPIResponse:
        """
        Get settings for the microservice.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.WORKFLOW_ENGINE.SETTINGS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_workflow_engine_settings(self, settings_param: dict) -> PrivXAPIResponse:
        """
        Store microservice settings.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.WORKFLOW_ENGINE.SETTINGS, body=settings_param
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def test_workflow_engine_settings(self, settings_param: dict) -> PrivXAPIResponse:
        """
        Test the email settings.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.WORKFLOW_ENGINE.TEST_SETTINGS, body=settings_param
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
