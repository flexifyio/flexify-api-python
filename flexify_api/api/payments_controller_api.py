# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flexify_api.api_client import ApiClient


class PaymentsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_payment_options(self, amount, currency, **kwargs):  # noqa: E501
        """getPaymentOptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_options(amount, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float amount: amount (required)
        :param str currency: currency (required)
        :return: PaymentOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payment_options_with_http_info(amount, currency, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payment_options_with_http_info(amount, currency, **kwargs)  # noqa: E501
            return data

    def get_payment_options_with_http_info(self, amount, currency, **kwargs):  # noqa: E501
        """getPaymentOptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_options_with_http_info(amount, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float amount: amount (required)
        :param str currency: currency (required)
        :return: PaymentOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['amount', 'currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'amount' is set
        if self.api_client.client_side_validation and ('amount' not in params or
                                                       params['amount'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `amount` when calling `get_payment_options`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if self.api_client.client_side_validation and ('currency' not in params or
                                                       params['currency'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `currency` when calling `get_payment_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501

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
            '/backend/rest/pay/paddle/options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentOptions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payment_fulfilled(self, **kwargs):  # noqa: E501
        """paymentFulfilled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payment_fulfilled(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payment_fulfilled_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.payment_fulfilled_with_http_info(**kwargs)  # noqa: E501
            return data

    def payment_fulfilled_with_http_info(self, **kwargs):  # noqa: E501
        """paymentFulfilled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payment_fulfilled_with_http_info(async_req=True)
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
                    " to method payment_fulfilled" % key
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
            '/backend/rest/pay/paddle/webhook', 'GET',
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
