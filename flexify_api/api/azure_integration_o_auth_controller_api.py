# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class AzureIntegrationOAuthControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_azure_integration(self, request, **kwargs):  # noqa: E501
        """Add new Azure integration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_azure_integration(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FinishOAuthParams request: request (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_azure_integration_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.add_azure_integration_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def add_azure_integration_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add new Azure integration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_azure_integration_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FinishOAuthParams request: request (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_azure_integration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `add_azure_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def auth_storage(self, auth_params, azure_integration_id, **kwargs):  # noqa: E501
        """Authenticate Azure integration storage access  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_storage(auth_params, azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FinishOAuthParams auth_params: authParams (required)
        :param int azure_integration_id: azure-integration-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.auth_storage_with_http_info(auth_params, azure_integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.auth_storage_with_http_info(auth_params, azure_integration_id, **kwargs)  # noqa: E501
            return data

    def auth_storage_with_http_info(self, auth_params, azure_integration_id, **kwargs):  # noqa: E501
        """Authenticate Azure integration storage access  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_storage_with_http_info(auth_params, azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FinishOAuthParams auth_params: authParams (required)
        :param int azure_integration_id: azure-integration-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_params', 'azure_integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_storage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_params' is set
        if self.api_client.client_side_validation and ('auth_params' not in params or
                                                       params['auth_params'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `auth_params` when calling `auth_storage`")  # noqa: E501
        # verify the required parameter 'azure_integration_id' is set
        if self.api_client.client_side_validation and ('azure_integration_id' not in params or
                                                       params['azure_integration_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `azure_integration_id` when calling `auth_storage`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'azure_integration_id' in params:
            path_params['azure-integration-id'] = params['azure_integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'auth_params' in params:
            body_params = params['auth_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/{azure-integration-id}/actions/auth-storage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_azure_integration(self, azure_integration_id, **kwargs):  # noqa: E501
        """Deletes (hides) Azure integration by Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_azure_integration(azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_integration_id: azure-integration-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_azure_integration_with_http_info(azure_integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_azure_integration_with_http_info(azure_integration_id, **kwargs)  # noqa: E501
            return data

    def delete_azure_integration_with_http_info(self, azure_integration_id, **kwargs):  # noqa: E501
        """Deletes (hides) Azure integration by Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_azure_integration_with_http_info(azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_integration_id: azure-integration-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_azure_integration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_integration_id' is set
        if self.api_client.client_side_validation and ('azure_integration_id' not in params or
                                                       params['azure_integration_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `azure_integration_id` when calling `delete_azure_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'azure_integration_id' in params:
            path_params['azure-integration-id'] = params['azure_integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/{azure-integration-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_azure_integrations(self, **kwargs):  # noqa: E501
        """Get Azure integration by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_azure_integrations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AzureIntegration]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_azure_integrations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_azure_integrations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_azure_integrations_with_http_info(self, **kwargs):  # noqa: E501
        """Get Azure integration by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_azure_integrations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AzureIntegration]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_azure_integrations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AzureIntegration]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_config_for_azure_integration(self, **kwargs):  # noqa: E501
        """Get OAuth configuration to authorize Azure integration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_for_azure_integration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MicrosoftOAuthConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_config_for_azure_integration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_config_for_azure_integration_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_config_for_azure_integration_with_http_info(self, **kwargs):  # noqa: E501
        """Get OAuth configuration to authorize Azure integration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_for_azure_integration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MicrosoftOAuthConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config_for_azure_integration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/oauth/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MicrosoftOAuthConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_code_for_azure_integration_management(self, **kwargs):  # noqa: E501
        """Request device code to authorize Azure integration with device code flow (management access)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_code_for_azure_integration_management(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: OAuth2DeviceCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_code_for_azure_integration_management_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_device_code_for_azure_integration_management_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_device_code_for_azure_integration_management_with_http_info(self, **kwargs):  # noqa: E501
        """Request device code to authorize Azure integration with device code flow (management access)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_code_for_azure_integration_management_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: OAuth2DeviceCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_code_for_azure_integration_management" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/oauth/device-code/management', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OAuth2DeviceCodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_code_for_azure_integration_storage(self, **kwargs):  # noqa: E501
        """Request device code to authorize Azure integration with device code flow (storage access)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_code_for_azure_integration_storage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: OAuth2DeviceCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_code_for_azure_integration_storage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_device_code_for_azure_integration_storage_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_device_code_for_azure_integration_storage_with_http_info(self, **kwargs):  # noqa: E501
        """Request device code to authorize Azure integration with device code flow (storage access)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_code_for_azure_integration_storage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: OAuth2DeviceCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_code_for_azure_integration_storage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/oauth/device-code/storage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OAuth2DeviceCodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_storage_accounts_from_azure(self, azure_integration_id, **kwargs):  # noqa: E501
        """Use Azure integration to get list of storage accounts from Azure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_accounts_from_azure(azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_integration_id: azure-integration-id (required)
        :return: list[AzureSubscriptionInfoWithStorages]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_storage_accounts_from_azure_with_http_info(azure_integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_storage_accounts_from_azure_with_http_info(azure_integration_id, **kwargs)  # noqa: E501
            return data

    def get_storage_accounts_from_azure_with_http_info(self, azure_integration_id, **kwargs):  # noqa: E501
        """Use Azure integration to get list of storage accounts from Azure  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_accounts_from_azure_with_http_info(azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_integration_id: azure-integration-id (required)
        :return: list[AzureSubscriptionInfoWithStorages]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_storage_accounts_from_azure" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_integration_id' is set
        if self.api_client.client_side_validation and ('azure_integration_id' not in params or
                                                       params['azure_integration_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `azure_integration_id` when calling `get_storage_accounts_from_azure`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'azure_integration_id' in params:
            path_params['azure-integration-id'] = params['azure_integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/{azure-integration-id}/storage-accounts-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AzureSubscriptionInfoWithStorages]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reauth_azure_integration(self, auth_params, azure_integration_id, **kwargs):  # noqa: E501
        """Reauthenticate Azure integration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reauth_azure_integration(auth_params, azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FinishOAuthParams auth_params: authParams (required)
        :param int azure_integration_id: azure-integration-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reauth_azure_integration_with_http_info(auth_params, azure_integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reauth_azure_integration_with_http_info(auth_params, azure_integration_id, **kwargs)  # noqa: E501
            return data

    def reauth_azure_integration_with_http_info(self, auth_params, azure_integration_id, **kwargs):  # noqa: E501
        """Reauthenticate Azure integration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reauth_azure_integration_with_http_info(auth_params, azure_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FinishOAuthParams auth_params: authParams (required)
        :param int azure_integration_id: azure-integration-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auth_params', 'azure_integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reauth_azure_integration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auth_params' is set
        if self.api_client.client_side_validation and ('auth_params' not in params or
                                                       params['auth_params'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `auth_params` when calling `reauth_azure_integration`")  # noqa: E501
        # verify the required parameter 'azure_integration_id' is set
        if self.api_client.client_side_validation and ('azure_integration_id' not in params or
                                                       params['azure_integration_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `azure_integration_id` when calling `reauth_azure_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'azure_integration_id' in params:
            path_params['azure-integration-id'] = params['azure_integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'auth_params' in params:
            body_params = params['auth_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/azure-integration/{azure-integration-id}/actions/reauth', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
