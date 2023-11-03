# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.20-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class AuthSsoControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_config(self, oauth_provider_id, **kwargs):  # noqa: E501
        """getConfig  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config(oauth_provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str oauth_provider_id: oauth-provider-id (required)
        :return: MicrosoftOAuthConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_config_with_http_info(oauth_provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_config_with_http_info(oauth_provider_id, **kwargs)  # noqa: E501
            return data

    def get_config_with_http_info(self, oauth_provider_id, **kwargs):  # noqa: E501
        """getConfig  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_with_http_info(oauth_provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str oauth_provider_id: oauth-provider-id (required)
        :return: MicrosoftOAuthConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oauth_provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'oauth_provider_id' is set
        if self.api_client.client_side_validation and ('oauth_provider_id' not in params or
                                                       params['oauth_provider_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `oauth_provider_id` when calling `get_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'oauth_provider_id' in params:
            query_params.append(('oauth-provider-id', params['oauth_provider_id']))  # noqa: E501

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
            '/backend/rest/auth/sso/config', 'GET',
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

    def get_device_code(self, oauth_provider_id, **kwargs):  # noqa: E501
        """getDeviceCode  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_code(oauth_provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str oauth_provider_id: oauth-provider-id (required)
        :return: OAuth2DeviceCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_code_with_http_info(oauth_provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_code_with_http_info(oauth_provider_id, **kwargs)  # noqa: E501
            return data

    def get_device_code_with_http_info(self, oauth_provider_id, **kwargs):  # noqa: E501
        """getDeviceCode  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_code_with_http_info(oauth_provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str oauth_provider_id: oauth-provider-id (required)
        :return: OAuth2DeviceCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oauth_provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'oauth_provider_id' is set
        if self.api_client.client_side_validation and ('oauth_provider_id' not in params or
                                                       params['oauth_provider_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `oauth_provider_id` when calling `get_device_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'oauth_provider_id' in params:
            query_params.append(('oauth-provider-id', params['oauth_provider_id']))  # noqa: E501

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
            '/backend/rest/auth/sso/device-code', 'GET',
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

    def get_token_by_device_code(self, request, **kwargs):  # noqa: E501
        """getTokenByDeviceCode  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_by_device_code(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenByDeviceCodeRequest request: request (required)
        :return: OAuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_by_device_code_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_by_device_code_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_token_by_device_code_with_http_info(self, request, **kwargs):  # noqa: E501
        """getTokenByDeviceCode  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_by_device_code_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenByDeviceCodeRequest request: request (required)
        :return: OAuthToken
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
                    " to method get_token_by_device_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `get_token_by_device_code`")  # noqa: E501

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
            '/backend/rest/auth/sso/token-by-device-code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OAuthToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_token_for_device_code_flow(self, request, **kwargs):  # noqa: E501
        """refreshTokenForDeviceCodeFlow  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_token_for_device_code_flow(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshTokenRequest request: request (required)
        :return: OAuthToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_token_for_device_code_flow_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_token_for_device_code_flow_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def refresh_token_for_device_code_flow_with_http_info(self, request, **kwargs):  # noqa: E501
        """refreshTokenForDeviceCodeFlow  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_token_for_device_code_flow_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshTokenRequest request: request (required)
        :return: OAuthToken
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
                    " to method refresh_token_for_device_code_flow" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `refresh_token_for_device_code_flow`")  # noqa: E501

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
            '/backend/rest/auth/sso/token-refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OAuthToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
