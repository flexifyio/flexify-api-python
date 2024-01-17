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
from flexify_api.api.user_controller_api import UserControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestUserControllerApi(unittest.TestCase):
    """UserControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.user_controller_api.UserControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_microsoft_sso(self):
        """Test case for change_microsoft_sso

        changeMicrosoftSso  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Get details of user corresponding to provided auth token  # noqa: E501
        """
        pass

    def test_request_delete(self):
        """Test case for request_delete

        requestDelete  # noqa: E501
        """
        pass

    def test_request_reset_password(self):
        """Test case for request_reset_password

        requestResetPassword  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
