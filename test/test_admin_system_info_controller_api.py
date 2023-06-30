# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.18-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.admin_system_info_controller_api import AdminSystemInfoControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestAdminSystemInfoControllerApi(unittest.TestCase):
    """AdminSystemInfoControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.admin_system_info_controller_api.AdminSystemInfoControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_system_info(self):
        """Test case for system_info

        Request General System Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()