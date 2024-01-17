# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.15.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.storage_accounts_o_auth_controller_api import StorageAccountsOAuthControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestStorageAccountsOAuthControllerApi(unittest.TestCase):
    """StorageAccountsOAuthControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.storage_accounts_o_auth_controller_api.StorageAccountsOAuthControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config2(self):
        """Test case for get_config2

        getConfig  # noqa: E501
        """
        pass

    def test_get_device_code1(self):
        """Test case for get_device_code1

        getDeviceCode  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
