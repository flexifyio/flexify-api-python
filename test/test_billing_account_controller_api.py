# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.billing_account_controller_api import BillingAccountControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestBillingAccountControllerApi(unittest.TestCase):
    """BillingAccountControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.billing_account_controller_api.BillingAccountControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_costs_for_current_user_billing_account(self):
        """Test case for get_costs_for_current_user_billing_account

        Get costs for current user  # noqa: E501
        """
        pass

    def test_get_current_user_billing_account(self):
        """Test case for get_current_user_billing_account

        Get billing account for current user  # noqa: E501
        """
        pass

    def test_get_payments_for_current_user(self):
        """Test case for get_payments_for_current_user

        Get payments for current user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
