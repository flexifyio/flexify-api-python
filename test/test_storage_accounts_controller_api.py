# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.13.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.storage_accounts_controller_api import StorageAccountsControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestStorageAccountsControllerApi(unittest.TestCase):
    """StorageAccountsControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.storage_accounts_controller_api.StorageAccountsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_storage_account(self):
        """Test case for add_storage_account

        Add Storage Account with an optional list of buckets  # noqa: E501
        """
        pass

    def test_delete_storage_account(self):
        """Test case for delete_storage_account

        Deletes (hides) storage account and all its buckets/containers  # noqa: E501
        """
        pass

    def test_get_storage_account(self):
        """Test case for get_storage_account

        Get storage account by id  # noqa: E501
        """
        pass

    def test_get_storage_accounts(self):
        """Test case for get_storage_accounts

        Get all storage accounts for current user  # noqa: E501
        """
        pass

    def test_reauth_storage_account(self):
        """Test case for reauth_storage_account

        Reauthenticate storage account  # noqa: E501
        """
        pass

    def test_refresh_storage_account(self):
        """Test case for refresh_storage_account

        Requests and updates list of buckets/containers for the storage account  # noqa: E501
        """
        pass

    def test_set_storage_account_settings(self):
        """Test case for set_storage_account_settings

        Updates storage account settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
