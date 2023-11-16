# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.partner_organizations_controller_api import PartnerOrganizationsControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestPartnerOrganizationsControllerApi(unittest.TestCase):
    """PartnerOrganizationsControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.partner_organizations_controller_api.PartnerOrganizationsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all(self):
        """Test case for get_all

        getAll  # noqa: E501
        """
        pass

    def test_get_org_limits(self):
        """Test case for get_org_limits

        getOrgLimits  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
