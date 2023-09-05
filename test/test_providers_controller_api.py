# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.providers_controller_api import ProvidersControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestProvidersControllerApi(unittest.TestCase):
    """ProvidersControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.providers_controller_api.ProvidersControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_providers(self):
        """Test case for get_providers

        Get all storage providers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
