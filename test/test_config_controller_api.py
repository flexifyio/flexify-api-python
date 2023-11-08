# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.config_controller_api import ConfigControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestConfigControllerApi(unittest.TestCase):
    """ConfigControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.config_controller_api.ConfigControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config(self):
        """Test case for get_config

        Get public Management Server config  # noqa: E501
        """
        pass

    def test_get_config1(self):
        """Test case for get_config1

        Get public Management Server config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
