# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.14
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class UserControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_current_user(self, **kwargs):  # noqa: E501
        """Get details of user corresponding to provided auth token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context_path:
        :param str locale_country:
        :param str locale_display_country:
        :param str locale_display_language:
        :param str locale_display_name:
        :param str locale_display_script:
        :param str locale_display_variant:
        :param list[str] locale_extension_keys:
        :param str locale_iso3_country:
        :param str locale_iso3_language:
        :param str locale_language:
        :param str locale_script:
        :param list[str] locale_unicode_locale_attributes:
        :param list[str] locale_unicode_locale_keys:
        :param str locale_variant:
        :param str remote_user:
        :param bool secure:
        :param str user_principal_name:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get details of user corresponding to provided auth token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str context_path:
        :param str locale_country:
        :param str locale_display_country:
        :param str locale_display_language:
        :param str locale_display_name:
        :param str locale_display_script:
        :param str locale_display_variant:
        :param list[str] locale_extension_keys:
        :param str locale_iso3_country:
        :param str locale_iso3_language:
        :param str locale_language:
        :param str locale_script:
        :param list[str] locale_unicode_locale_attributes:
        :param list[str] locale_unicode_locale_keys:
        :param str locale_variant:
        :param str remote_user:
        :param bool secure:
        :param str user_principal_name:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['context_path', 'locale_country', 'locale_display_country', 'locale_display_language', 'locale_display_name', 'locale_display_script', 'locale_display_variant', 'locale_extension_keys', 'locale_iso3_country', 'locale_iso3_language', 'locale_language', 'locale_script', 'locale_unicode_locale_attributes', 'locale_unicode_locale_keys', 'locale_variant', 'remote_user', 'secure', 'user_principal_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'context_path' in params:
            query_params.append(('contextPath', params['context_path']))  # noqa: E501
        if 'locale_country' in params:
            query_params.append(('locale.country', params['locale_country']))  # noqa: E501
        if 'locale_display_country' in params:
            query_params.append(('locale.displayCountry', params['locale_display_country']))  # noqa: E501
        if 'locale_display_language' in params:
            query_params.append(('locale.displayLanguage', params['locale_display_language']))  # noqa: E501
        if 'locale_display_name' in params:
            query_params.append(('locale.displayName', params['locale_display_name']))  # noqa: E501
        if 'locale_display_script' in params:
            query_params.append(('locale.displayScript', params['locale_display_script']))  # noqa: E501
        if 'locale_display_variant' in params:
            query_params.append(('locale.displayVariant', params['locale_display_variant']))  # noqa: E501
        if 'locale_extension_keys' in params:
            query_params.append(('locale.extensionKeys', params['locale_extension_keys']))  # noqa: E501
            collection_formats['locale.extensionKeys'] = 'multi'  # noqa: E501
        if 'locale_iso3_country' in params:
            query_params.append(('locale.ISO3Country', params['locale_iso3_country']))  # noqa: E501
        if 'locale_iso3_language' in params:
            query_params.append(('locale.ISO3Language', params['locale_iso3_language']))  # noqa: E501
        if 'locale_language' in params:
            query_params.append(('locale.language', params['locale_language']))  # noqa: E501
        if 'locale_script' in params:
            query_params.append(('locale.script', params['locale_script']))  # noqa: E501
        if 'locale_unicode_locale_attributes' in params:
            query_params.append(('locale.unicodeLocaleAttributes', params['locale_unicode_locale_attributes']))  # noqa: E501
            collection_formats['locale.unicodeLocaleAttributes'] = 'multi'  # noqa: E501
        if 'locale_unicode_locale_keys' in params:
            query_params.append(('locale.unicodeLocaleKeys', params['locale_unicode_locale_keys']))  # noqa: E501
            collection_formats['locale.unicodeLocaleKeys'] = 'multi'  # noqa: E501
        if 'locale_variant' in params:
            query_params.append(('locale.variant', params['locale_variant']))  # noqa: E501
        if 'remote_user' in params:
            query_params.append(('remoteUser', params['remote_user']))  # noqa: E501
        if 'secure' in params:
            query_params.append(('secure', params['secure']))  # noqa: E501
        if 'user_principal_name' in params:
            query_params.append(('userPrincipal.name', params['user_principal_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/user/current', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_delete(self, **kwargs):  # noqa: E501
        """requestDelete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.request_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def request_delete_with_http_info(self, **kwargs):  # noqa: E501
        """requestDelete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method request_delete" % key
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
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/user/request-delete', 'POST',
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

    def request_reset_password(self, request, **kwargs):  # noqa: E501
        """requestResetPassword  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_reset_password(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResetPasswordRequest request: request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_reset_password_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.request_reset_password_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def request_reset_password_with_http_info(self, request, **kwargs):  # noqa: E501
        """requestResetPassword  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_reset_password_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestResetPasswordRequest request: request (required)
        :return: None
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
                    " to method request_reset_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `request_reset_password`")  # noqa: E501

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
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/user/request-reset-password', 'POST',
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
