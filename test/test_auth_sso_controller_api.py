# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.20-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.auth_sso_controller_api import AuthSsoControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestAuthSsoControllerApi(unittest.TestCase):
    """AuthSsoControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.auth_sso_controller_api.AuthSsoControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config(self):
        """Test case for get_config

        getConfig  # noqa: E501
        """
        pass

    def test_get_device_code(self):
        """Test case for get_device_code

        getDeviceCode  # noqa: E501
        """
        pass

    def test_get_token_by_device_code(self):
        """Test case for get_token_by_device_code

        getTokenByDeviceCode  # noqa: E501
        """
        pass

    def test_refresh_token_for_device_code_flow(self):
        """Test case for refresh_token_for_device_code_flow

        refreshTokenForDeviceCodeFlow  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
