# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.azure_integration_o_auth_controller_api import AzureIntegrationOAuthControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestAzureIntegrationOAuthControllerApi(unittest.TestCase):
    """AzureIntegrationOAuthControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.azure_integration_o_auth_controller_api.AzureIntegrationOAuthControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_azure_integration(self):
        """Test case for add_azure_integration

        Add new Azure integration  # noqa: E501
        """
        pass

    def test_auth_storage(self):
        """Test case for auth_storage

        Authenticate Azure integration storage access  # noqa: E501
        """
        pass

    def test_delete_azure_integration(self):
        """Test case for delete_azure_integration

        Deletes (hides) Azure integration by Id  # noqa: E501
        """
        pass

    def test_get_azure_integrations(self):
        """Test case for get_azure_integrations

        Get Azure integration by id  # noqa: E501
        """
        pass

    def test_get_config_for_azure_integration(self):
        """Test case for get_config_for_azure_integration

        Get OAuth configuration to authorize Azure integration  # noqa: E501
        """
        pass

    def test_get_device_code_for_azure_integration_management(self):
        """Test case for get_device_code_for_azure_integration_management

        Request device code to authorize Azure integration with device code flow (management access)  # noqa: E501
        """
        pass

    def test_get_device_code_for_azure_integration_storage(self):
        """Test case for get_device_code_for_azure_integration_storage

        Request device code to authorize Azure integration with device code flow (storage access)  # noqa: E501
        """
        pass

    def test_get_storage_accounts_from_azure(self):
        """Test case for get_storage_accounts_from_azure

        Use Azure integration to get list of storage accounts from Azure  # noqa: E501
        """
        pass

    def test_reauth_azure_integration(self):
        """Test case for reauth_azure_integration

        Reauthenticate Azure integration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
