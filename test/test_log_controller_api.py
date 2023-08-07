# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.18
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.log_controller_api import LogControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestLogControllerApi(unittest.TestCase):
    """LogControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.log_controller_api.LogControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_log_for_current_user(self):
        """Test case for get_log_for_current_user

        getLogForCurrentUser  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
