# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.8.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.authentication_controller_api import AuthenticationControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestAuthenticationControllerApi(unittest.TestCase):
    """AuthenticationControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.authentication_controller_api.AuthenticationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate(self):
        """Test case for authenticate

        Generate new access token for the user  # noqa: E501
        """
        pass

    def test_get_config(self):
        """Test case for get_config

        Logout  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
