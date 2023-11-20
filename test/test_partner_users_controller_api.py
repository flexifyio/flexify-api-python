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
from flexify_api.api.partner_users_controller_api import PartnerUsersControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestPartnerUsersControllerApi(unittest.TestCase):
    """PartnerUsersControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.partner_users_controller_api.PartnerUsersControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_user_state(self):
        """Test case for change_user_state

        Change user state  # noqa: E501
        """
        pass

    def test_change_user_state1(self):
        """Test case for change_user_state1

        Change user state  # noqa: E501
        """
        pass

    def test_change_user_state_by_external_id(self):
        """Test case for change_user_state_by_external_id

        Change user state by external ID  # noqa: E501
        """
        pass

    def test_change_user_state_by_external_id1(self):
        """Test case for change_user_state_by_external_id1

        Change user state by external ID  # noqa: E501
        """
        pass

    def test_change_user_state_by_username(self):
        """Test case for change_user_state_by_username

        Change user state by username  # noqa: E501
        """
        pass

    def test_change_user_state_by_username1(self):
        """Test case for change_user_state_by_username1

        Change user state by username  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create a user  # noqa: E501
        """
        pass

    def test_create1(self):
        """Test case for create1

        Create a user  # noqa: E501
        """
        pass

    def test_create_password_reset_token(self):
        """Test case for create_password_reset_token

        Create password reset token  # noqa: E501
        """
        pass

    def test_create_password_reset_token1(self):
        """Test case for create_password_reset_token1

        Create password reset token  # noqa: E501
        """
        pass

    def test_create_password_reset_token_by_external_id(self):
        """Test case for create_password_reset_token_by_external_id

        Create password reset token by external ID  # noqa: E501
        """
        pass

    def test_create_password_reset_token_by_external_id1(self):
        """Test case for create_password_reset_token_by_external_id1

        Create password reset token by external ID  # noqa: E501
        """
        pass

    def test_create_password_reset_token_by_username(self):
        """Test case for create_password_reset_token_by_username

        Create password reset token by username  # noqa: E501
        """
        pass

    def test_create_password_reset_token_by_username1(self):
        """Test case for create_password_reset_token_by_username1

        Create password reset token by username  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user  # noqa: E501
        """
        pass

    def test_delete_user1(self):
        """Test case for delete_user1

        Delete user  # noqa: E501
        """
        pass

    def test_delete_user_by_external_id(self):
        """Test case for delete_user_by_external_id

        Delete user by external ID  # noqa: E501
        """
        pass

    def test_delete_user_by_external_id1(self):
        """Test case for delete_user_by_external_id1

        Delete user by external ID  # noqa: E501
        """
        pass

    def test_delete_user_by_username(self):
        """Test case for delete_user_by_username

        Delete user by username  # noqa: E501
        """
        pass

    def test_delete_user_by_username1(self):
        """Test case for delete_user_by_username1

        Delete user by username  # noqa: E501
        """
        pass

    def test_generate_token(self):
        """Test case for generate_token

        Create token  # noqa: E501
        """
        pass

    def test_generate_token1(self):
        """Test case for generate_token1

        Create token  # noqa: E501
        """
        pass

    def test_generate_token_by_external_id(self):
        """Test case for generate_token_by_external_id

        Create token by external ID  # noqa: E501
        """
        pass

    def test_generate_token_by_external_id1(self):
        """Test case for generate_token_by_external_id1

        Create token by external ID  # noqa: E501
        """
        pass

    def test_generate_token_by_username(self):
        """Test case for generate_token_by_username

        Create token by username  # noqa: E501
        """
        pass

    def test_generate_token_by_username1(self):
        """Test case for generate_token_by_username1

        Create token by username  # noqa: E501
        """
        pass

    def test_get_all_users_pageable(self):
        """Test case for get_all_users_pageable

        Get users with search, sorting and pagination  # noqa: E501
        """
        pass

    def test_get_all_users_pageable1(self):
        """Test case for get_all_users_pageable1

        Get users with search, sorting and pagination  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user details  # noqa: E501
        """
        pass

    def test_get_user1(self):
        """Test case for get_user1

        Get user details  # noqa: E501
        """
        pass

    def test_get_user_by_external_id(self):
        """Test case for get_user_by_external_id

        Get user details by external ID  # noqa: E501
        """
        pass

    def test_get_user_by_external_id1(self):
        """Test case for get_user_by_external_id1

        Get user details by external ID  # noqa: E501
        """
        pass

    def test_get_user_by_username(self):
        """Test case for get_user_by_username

        Get user details by username  # noqa: E501
        """
        pass

    def test_get_user_by_username1(self):
        """Test case for get_user_by_username1

        Get user details by username  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Get all users  # noqa: E501
        """
        pass

    def test_get_users1(self):
        """Test case for get_users1

        Get all users  # noqa: E501
        """
        pass

    def test_send_password_reset_email(self):
        """Test case for send_password_reset_email

        Set/reset password  # noqa: E501
        """
        pass

    def test_send_password_reset_email1(self):
        """Test case for send_password_reset_email1

        Set/reset password  # noqa: E501
        """
        pass

    def test_send_password_reset_email_by_external_id(self):
        """Test case for send_password_reset_email_by_external_id

        Set/reset password by external ID  # noqa: E501
        """
        pass

    def test_send_password_reset_email_by_external_id1(self):
        """Test case for send_password_reset_email_by_external_id1

        Set/reset password by external ID  # noqa: E501
        """
        pass

    def test_send_password_reset_email_by_username(self):
        """Test case for send_password_reset_email_by_username

        Set/reset password by username  # noqa: E501
        """
        pass

    def test_send_password_reset_email_by_username1(self):
        """Test case for send_password_reset_email_by_username1

        Set/reset password by username  # noqa: E501
        """
        pass

    def test_set_limits(self):
        """Test case for set_limits

        Set custom user limits by partner  # noqa: E501
        """
        pass

    def test_set_limits1(self):
        """Test case for set_limits1

        Set custom user limits by partner  # noqa: E501
        """
        pass

    def test_set_limits_by_external_id(self):
        """Test case for set_limits_by_external_id

        setLimitsByExternalId  # noqa: E501
        """
        pass

    def test_set_limits_by_external_id1(self):
        """Test case for set_limits_by_external_id1

        setLimitsByExternalId  # noqa: E501
        """
        pass

    def test_set_limits_by_username(self):
        """Test case for set_limits_by_username

        setLimitsByUsername  # noqa: E501
        """
        pass

    def test_set_limits_by_username1(self):
        """Test case for set_limits_by_username1

        setLimitsByUsername  # noqa: E501
        """
        pass

    def test_set_roles(self):
        """Test case for set_roles

        setRoles  # noqa: E501
        """
        pass

    def test_set_roles1(self):
        """Test case for set_roles1

        setRoles  # noqa: E501
        """
        pass

    def test_set_roles_by_external_id(self):
        """Test case for set_roles_by_external_id

        setRolesByExternalId  # noqa: E501
        """
        pass

    def test_set_roles_by_external_id1(self):
        """Test case for set_roles_by_external_id1

        setRolesByExternalId  # noqa: E501
        """
        pass

    def test_set_roles_by_username(self):
        """Test case for set_roles_by_username

        setRolesByUsername  # noqa: E501
        """
        pass

    def test_set_roles_by_username1(self):
        """Test case for set_roles_by_username1

        setRolesByUsername  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update profile  # noqa: E501
        """
        pass

    def test_update_user1(self):
        """Test case for update_user1

        Update profile  # noqa: E501
        """
        pass

    def test_update_user_by_external_id(self):
        """Test case for update_user_by_external_id

        Update profile by external ID  # noqa: E501
        """
        pass

    def test_update_user_by_external_id1(self):
        """Test case for update_user_by_external_id1

        Update profile by external ID  # noqa: E501
        """
        pass

    def test_update_user_by_username(self):
        """Test case for update_user_by_username

        Update profile by username  # noqa: E501
        """
        pass

    def test_update_user_by_username1(self):
        """Test case for update_user_by_username1

        Update profile by username  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
