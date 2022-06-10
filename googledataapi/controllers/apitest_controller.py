# -*- coding: utf-8 -*-

"""
googledataapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from googledataapi.api_helper import APIHelper
from googledataapi.configuration import Server
from googledataapi.controllers.base_controller import BaseController
from googledataapi.exceptions.api_exception import APIException


class APITESTController(BaseController):

    """A Controller to access Endpoints in the googledataapi API."""
    def __init__(self, config, auth_managers):
        super(APITESTController, self).__init__(config, auth_managers)

    def google_search_api(self,
                          part,
                          max_results,
                          q,
                          key,
                          mtype):
        """Does a GET request to /youtube/v3/search.

        TODO: type endpoint description here.

        Args:
            part (string): description of part
            max_results (string): Limit of Max Results
            q (string): NA
            key (string): Value for api key
            mtype (string): Type of resource

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/youtube/v3/search'
        _query_builder = self.config.get_base_uri(Server.DEFAULT)
        _query_builder += _url_path
        _query_parameters = {
            'part': part,
            'maxResults': max_results,
            'q': q,
            'key': key,
            'type': mtype
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 403:
            raise APIException('quotaExceeded', _response)
        elif _response.status_code == 404:
            raise APIException('not found', _response)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded