# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class StoragesControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_buckets(self, request, storage_account_id, **kwargs):  # noqa: E501
        """Add buckets to the storage account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_buckets(request, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddBucketsRequest request: request (required)
        :param int storage_account_id: storage-account-id (required)
        :return: IdsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_buckets_with_http_info(request, storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_buckets_with_http_info(request, storage_account_id, **kwargs)  # noqa: E501
            return data

    def add_buckets_with_http_info(self, request, storage_account_id, **kwargs):  # noqa: E501
        """Add buckets to the storage account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_buckets_with_http_info(request, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddBucketsRequest request: request (required)
        :param int storage_account_id: storage-account-id (required)
        :return: IdsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'storage_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_buckets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `add_buckets`")  # noqa: E501
        # verify the required parameter 'storage_account_id' is set
        if self.api_client.client_side_validation and ('storage_account_id' not in params or
                                                       params['storage_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `storage_account_id` when calling `add_buckets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'storage_account_id' in params:
            path_params['storage-account-id'] = params['storage_account_id']  # noqa: E501

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
            '/backend/rest/storage-accounts/{storage-account-id}/buckets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_bucket(self, bucket_id, storage_account_id, **kwargs):  # noqa: E501
        """Deletes (hides) a bucket/container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bucket(bucket_id, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bucket_id: bucket-id (required)
        :param int storage_account_id: storage-account-id (required)
        :param bool force_detach: force-detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bucket_with_http_info(bucket_id, storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bucket_with_http_info(bucket_id, storage_account_id, **kwargs)  # noqa: E501
            return data

    def delete_bucket_with_http_info(self, bucket_id, storage_account_id, **kwargs):  # noqa: E501
        """Deletes (hides) a bucket/container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bucket_with_http_info(bucket_id, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bucket_id: bucket-id (required)
        :param int storage_account_id: storage-account-id (required)
        :param bool force_detach: force-detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id', 'storage_account_id', 'force_detach']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if self.api_client.client_side_validation and ('bucket_id' not in params or
                                                       params['bucket_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bucket_id` when calling `delete_bucket`")  # noqa: E501
        # verify the required parameter 'storage_account_id' is set
        if self.api_client.client_side_validation and ('storage_account_id' not in params or
                                                       params['storage_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `storage_account_id` when calling `delete_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucket-id'] = params['bucket_id']  # noqa: E501
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
            '/backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}', 'DELETE',
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

    def get_bucket(self, bucket_id, storage_account_id, **kwargs):  # noqa: E501
        """Get detailed stats for the bucket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bucket(bucket_id, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bucket_id: bucket-id (required)
        :param int storage_account_id: storage-account-id (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bucket_with_http_info(bucket_id, storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bucket_with_http_info(bucket_id, storage_account_id, **kwargs)  # noqa: E501
            return data

    def get_bucket_with_http_info(self, bucket_id, storage_account_id, **kwargs):  # noqa: E501
        """Get detailed stats for the bucket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bucket_with_http_info(bucket_id, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bucket_id: bucket-id (required)
        :param int storage_account_id: storage-account-id (required)
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id', 'storage_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if self.api_client.client_side_validation and ('bucket_id' not in params or
                                                       params['bucket_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bucket_id` when calling `get_bucket`")  # noqa: E501
        # verify the required parameter 'storage_account_id' is set
        if self.api_client.client_side_validation and ('storage_account_id' not in params or
                                                       params['storage_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `storage_account_id` when calling `get_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucket-id'] = params['bucket_id']  # noqa: E501
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
            '/backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Bucket',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_bucket(self, bucket_id, storage_account_id, **kwargs):  # noqa: E501
        """Refresh statistics of a single bucket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_bucket(bucket_id, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bucket_id: bucket-id (required)
        :param int storage_account_id: storage-account-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_bucket_with_http_info(bucket_id, storage_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_bucket_with_http_info(bucket_id, storage_account_id, **kwargs)  # noqa: E501
            return data

    def refresh_bucket_with_http_info(self, bucket_id, storage_account_id, **kwargs):  # noqa: E501
        """Refresh statistics of a single bucket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_bucket_with_http_info(bucket_id, storage_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int bucket_id: bucket-id (required)
        :param int storage_account_id: storage-account-id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_id', 'storage_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_bucket" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_id' is set
        if self.api_client.client_side_validation and ('bucket_id' not in params or
                                                       params['bucket_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bucket_id` when calling `refresh_bucket`")  # noqa: E501
        # verify the required parameter 'storage_account_id' is set
        if self.api_client.client_side_validation and ('storage_account_id' not in params or
                                                       params['storage_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `storage_account_id` when calling `refresh_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bucket_id' in params:
            path_params['bucket-id'] = params['bucket_id']  # noqa: E501
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
            '/backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}/actions/refresh', 'POST',
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
