# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.auth_controller_api import AuthControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestAuthControllerApi(unittest.TestCase):
    """AuthControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.auth_controller_api.AuthControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate(self):
        """Test case for authenticate

        Generate new access token for the user  # noqa: E501
        """
        pass

    def test_check_token_and_get_user(self):
        """Test case for check_token_and_get_user

        Check of given token  # noqa: E501
        """
        pass

    def test_get_config(self):
        """Test case for get_config

        Get public auth config  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
