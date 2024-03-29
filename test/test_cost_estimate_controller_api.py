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
from flexify_api.api.cost_estimate_controller_api import CostEstimateControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestCostEstimateControllerApi(unittest.TestCase):
    """CostEstimateControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.cost_estimate_controller_api.CostEstimateControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_estimate_migration_cost(self):
        """Test case for estimate_migration_cost

        estimateMigrationCost  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
