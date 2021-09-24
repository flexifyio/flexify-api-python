# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.7
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.cloud_locations_controller_api import CloudLocationsControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestCloudLocationsControllerApi(unittest.TestCase):
    """CloudLocationsControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.cloud_locations_controller_api.CloudLocationsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_auto_deploy_available_locations_for_current_user(self):
        """Test case for get_auto_deploy_available_locations_for_current_user

        getAutoDeployAvailableLocationsForCurrentUser  # noqa: E501
        """
        pass

    def test_get_existing_available_locations_for_current_user(self):
        """Test case for get_existing_available_locations_for_current_user

        getExistingAvailableLocationsForCurrentUser  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
