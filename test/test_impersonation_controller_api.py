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
from flexify_api.api.impersonation_controller_api import ImpersonationControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestImpersonationControllerApi(unittest.TestCase):
    """ImpersonationControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.impersonation_controller_api.ImpersonationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_impersonate_code(self):
        """Test case for add_impersonate_code

        addImpersonateCode  # noqa: E501
        """
        pass

    def test_add_impersonate_from_user(self):
        """Test case for add_impersonate_from_user

        addImpersonateFromUser  # noqa: E501
        """
        pass

    def test_get_impersonate_codes_list(self):
        """Test case for get_impersonate_codes_list

        getImpersonateCodesList  # noqa: E501
        """
        pass

    def test_get_impersonate_from_list(self):
        """Test case for get_impersonate_from_list

        getImpersonateFromList  # noqa: E501
        """
        pass

    def test_get_impersonate_to_list(self):
        """Test case for get_impersonate_to_list

        getImpersonateToList  # noqa: E501
        """
        pass

    def test_impersonate(self):
        """Test case for impersonate

        impersonate  # noqa: E501
        """
        pass

    def test_remove_impersonate_from_user(self):
        """Test case for remove_impersonate_from_user

        removeImpersonateFromUser  # noqa: E501
        """
        pass

    def test_remove_impersonate_from_user1(self):
        """Test case for remove_impersonate_from_user1

        removeImpersonateFromUser  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
