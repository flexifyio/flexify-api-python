# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.9.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.migrations_controller_api import MigrationsControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestMigrationsControllerApi(unittest.TestCase):
    """MigrationsControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.migrations_controller_api.MigrationsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_migration(self):
        """Test case for add_migration

        Add new migration  # noqa: E501
        """
        pass

    def test_get_migration(self):
        """Test case for get_migration

        Get migration by id. Only migration owner or administrator have access to the migration  # noqa: E501
        """
        pass

    def test_get_migrations(self):
        """Test case for get_migrations

        Get all migrations for logged in user in paged mode  # noqa: E501
        """
        pass

    def test_hide_all_migrations(self):
        """Test case for hide_all_migrations

        Mark all unfinished migrations as hidden UI  # noqa: E501
        """
        pass

    def test_hide_migration(self):
        """Test case for hide_migration

        Mark migration as hidden  # noqa: E501
        """
        pass

    def test_restart_slot(self):
        """Test case for restart_slot

        Mark migration as hidden  # noqa: E501
        """
        pass

    def test_stop_migration(self):
        """Test case for stop_migration

        Stop (cancel) the migration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
