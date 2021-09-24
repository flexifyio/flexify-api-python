# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.7
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class StorageAccountsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_storage_account(self, request, **kwargs):  # noqa: E501
        """Add Storage Account with an optional list of buckets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_storage_account(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddStorageAccountRequest request: request (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_storage_account_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.add_storage_account_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def add_storage_account_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add Storage Account with an optional list of buckets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_storage_account_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddStorageAccountRequest request: request (required)
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
                    " to method add_storage_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `add_storage_account`")  # noqa: E501

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
            '/backend/rest/storage-accounts', 'POST',
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

    def delete_storage_account(self, storage_account_id, **kwargs):  # noqa: E501
        """Deletes (hides) storage account and all its buckets/containers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_account(storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int storage_account_id: storage-account-id (required)
        :param bool force_detach: force-detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_storage_account_with_http_info(storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_storage_account_with_http_info(storage_account_id, **kwargs)  # noqa: E501
            return data

    def delete_storage_account_with_http_info(self, storage_account_id, **kwargs):  # noqa: E501
        """Deletes (hides) storage account and all its buckets/containers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_account_with_http_info(storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int storage_account_id: storage-account-id (required)
        :param bool force_detach: force-detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['storage_account_id', 'force_detach']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_storage_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_account_id' is set
        if ('storage_account_id' not in params or
                params['storage_account_id'] is None):
            raise ValueError("Missing the required parameter `storage_account_id` when calling `delete_storage_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'storage_account_id' in params:
            path_params['storage-account-id'] = params['storage_account_id']  # noqa: E501

        query_params = []
        if 'force_detach' in params:
            query_params.append(('force-detach', params['force_detach']))  # noqa: E501

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
            '/backend/rest/storage-accounts/{storage-account-id}', 'DELETE',
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

    def delete_storage_accounts(self, request, **kwargs):  # noqa: E501
        """Deletes (hides) a multiple storage accounts and all their buckets/containers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_accounts(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdsList request: request (required)
        :param bool force_detach: force-detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_storage_accounts_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_storage_accounts_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def delete_storage_accounts_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes (hides) a multiple storage accounts and all their buckets/containers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_accounts_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdsList request: request (required)
        :param bool force_detach: force-detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'force_detach']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_storage_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `delete_storage_accounts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'force_detach' in params:
            query_params.append(('force-detach', params['force_detach']))  # noqa: E501

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
            '/backend/rest/storage-accounts/actions/delete', 'POST',
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

    def get_storage_account(self, storage_account_id, **kwargs):  # noqa: E501
        """Get storage account by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_account(storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int storage_account_id: storage-account-id (required)
        :return: list[Bucket]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_storage_account_with_http_info(storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_storage_account_with_http_info(storage_account_id, **kwargs)  # noqa: E501
            return data

    def get_storage_account_with_http_info(self, storage_account_id, **kwargs):  # noqa: E501
        """Get storage account by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_account_with_http_info(storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int storage_account_id: storage-account-id (required)
        :return: list[Bucket]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['storage_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_storage_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_account_id' is set
        if ('storage_account_id' not in params or
                params['storage_account_id'] is None):
            raise ValueError("Missing the required parameter `storage_account_id` when calling `get_storage_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'storage_account_id' in params:
            path_params['storage-account-id'] = params['storage_account_id']  # noqa: E501

        query_params = []

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
            '/backend/rest/storage-accounts/storage-accounts/{storage-account-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Bucket]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_storage_accounts(self, **kwargs):  # noqa: E501
        """Get all storage accounts for current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_buckets: Include storages of given storage account to the response
        :return: list[StorageAccount]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_storage_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_storage_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_storage_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """Get all storage accounts for current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_buckets: Include storages of given storage account to the response
        :return: list[StorageAccount]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_buckets']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_storage_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_buckets' in params:
            query_params.append(('include-buckets', params['include_buckets']))  # noqa: E501

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
            '/backend/rest/storage-accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[StorageAccount]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_storage_account(self, storage_account_id, **kwargs):  # noqa: E501
        """Requests and updates list of buckets/containers for the storage account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_storage_account(storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int storage_account_id: storage-account-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_storage_account_with_http_info(storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_storage_account_with_http_info(storage_account_id, **kwargs)  # noqa: E501
            return data

    def refresh_storage_account_with_http_info(self, storage_account_id, **kwargs):  # noqa: E501
        """Requests and updates list of buckets/containers for the storage account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_storage_account_with_http_info(storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int storage_account_id: storage-account-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['storage_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_storage_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_account_id' is set
        if ('storage_account_id' not in params or
                params['storage_account_id'] is None):
            raise ValueError("Missing the required parameter `storage_account_id` when calling `refresh_storage_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'storage_account_id' in params:
            path_params['storage-account-id'] = params['storage_account_id']  # noqa: E501

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
            '/backend/rest/storage-accounts/{storage-account-id}/actions/refresh', 'POST',
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

    def refresh_storage_accounts(self, request, **kwargs):  # noqa: E501
        """Requests and updates list of buckets/containers for a list of storage accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_storage_accounts(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdsList request: request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_storage_accounts_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_storage_accounts_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def refresh_storage_accounts_with_http_info(self, request, **kwargs):  # noqa: E501
        """Requests and updates list of buckets/containers for a list of storage accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_storage_accounts_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdsList request: request (required)
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
                    " to method refresh_storage_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `refresh_storage_accounts`")  # noqa: E501

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
            '/backend/rest/storage-accounts/actions/refresh', 'POST',
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

    def set_storage_account_settings(self, settings, storage_account_id, **kwargs):  # noqa: E501
        """Updates storage account settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_storage_account_settings(settings, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageAccountSettingsReq settings: settings (required)
        :param int storage_account_id: storage-account-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_storage_account_settings_with_http_info(settings, storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_storage_account_settings_with_http_info(settings, storage_account_id, **kwargs)  # noqa: E501
            return data

    def set_storage_account_settings_with_http_info(self, settings, storage_account_id, **kwargs):  # noqa: E501
        """Updates storage account settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_storage_account_settings_with_http_info(settings, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageAccountSettingsReq settings: settings (required)
        :param int storage_account_id: storage-account-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings', 'storage_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_storage_account_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings' is set
        if ('settings' not in params or
                params['settings'] is None):
            raise ValueError("Missing the required parameter `settings` when calling `set_storage_account_settings`")  # noqa: E501
        # verify the required parameter 'storage_account_id' is set
        if ('storage_account_id' not in params or
                params['storage_account_id'] is None):
            raise ValueError("Missing the required parameter `storage_account_id` when calling `set_storage_account_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'storage_account_id' in params:
            path_params['storage-account-id'] = params['storage_account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings' in params:
            body_params = params['settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/backend/rest/storage-accounts/{storage-account-id}/settings', 'PUT',
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
