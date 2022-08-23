# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.10.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.storages_controller_api import StoragesControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestStoragesControllerApi(unittest.TestCase):
    """StoragesControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.storages_controller_api.StoragesControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_buckets(self):
        """Test case for add_buckets

        Add buckets to the storage account  # noqa: E501
        """
        pass

    def test_delete_bucket(self):
        """Test case for delete_bucket

        Deletes (hides) a bucket/container  # noqa: E501
        """
        pass

    def test_get_bucket(self):
        """Test case for get_bucket

        Get detailed stats for the bucket  # noqa: E501
        """
        pass

    def test_refresh_bucket(self):
        """Test case for refresh_bucket

        Refresh statistics of a single bucket  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
