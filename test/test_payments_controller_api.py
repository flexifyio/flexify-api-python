# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.10.hf2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.payments_controller_api import PaymentsControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestPaymentsControllerApi(unittest.TestCase):
    """PaymentsControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.payments_controller_api.PaymentsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payment_options(self):
        """Test case for get_payment_options

        getPaymentOptions  # noqa: E501
        """
        pass

    def test_payment_fulfilled(self):
        """Test case for payment_fulfilled

        paymentFulfilled  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
