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
from flexify_api.api.endpoints_controller_api import EndpointsControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestEndpointsControllerApi(unittest.TestCase):
    """EndpointsControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.endpoints_controller_api.EndpointsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_accounts(self):
        """Test case for attach_accounts

        Attach storage accounts to the endpoint  # noqa: E501
        """
        pass

    def test_attach_buckets(self):
        """Test case for attach_buckets

        Attach storages to the virtual bucket  # noqa: E501
        """
        pass

    def test_change_accounts(self):
        """Test case for change_accounts

        Modified all storage accounts to the endpoint  # noqa: E501
        """
        pass

    def test_change_buckets(self):
        """Test case for change_buckets

        Replaces the list of storages attached to the virtual bucket  # noqa: E501
        """
        pass

    def test_create_endpoint(self):
        """Test case for create_endpoint

        Creates new endpoint  # noqa: E501
        """
        pass

    def test_create_virtual_bucket(self):
        """Test case for create_virtual_bucket

        Creates new virtual bucket  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete the endpoint  # noqa: E501
        """
        pass

    def test_delete_virtual_bucket(self):
        """Test case for delete_virtual_bucket

        Deletes virtual bucket  # noqa: E501
        """
        pass

    def test_detach_account(self):
        """Test case for detach_account

        Detach storage account from the endpoint  # noqa: E501
        """
        pass

    def test_detach_bucket(self):
        """Test case for detach_bucket

        Detach storage account from the endpoint  # noqa: E501
        """
        pass

    def test_disable(self):
        """Test case for disable

        Disable the endpoint  # noqa: E501
        """
        pass

    def test_enable(self):
        """Test case for enable

        Enable the endpoint  # noqa: E501
        """
        pass

    def test_generate_access_keys(self):
        """Test case for generate_access_keys

        Generate new access keys pair  # noqa: E501
        """
        pass

    def test_get_endpoint_details(self):
        """Test case for get_endpoint_details

        Get endpoint details  # noqa: E501
        """
        pass

    def test_get_endpoint_secret_key(self):
        """Test case for get_endpoint_secret_key

        Get endpoint secret key  # noqa: E501
        """
        pass

    def test_get_endpoints_for_current_user(self):
        """Test case for get_endpoints_for_current_user

        Get the list of endpoints for current user optionally filtering by name or identity using SQL LIKE syntax  # noqa: E501
        """
        pass

    def test_set_attached_account_settings(self):
        """Test case for set_attached_account_settings

        Modifies settings of the attached storage account  # noqa: E501
        """
        pass

    def test_set_attached_bucket_settings(self):
        """Test case for set_attached_bucket_settings

        Modifies settings of the attached storage  # noqa: E501
        """
        pass

    def test_set_virtual_bucket_settings(self):
        """Test case for set_virtual_bucket_settings

        Modifies virtual bucket configuration  # noqa: E501
        """
        pass

    def test_update_endpoint_settings(self):
        """Test case for update_endpoint_settings

        Update attributes of the endpoint  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
