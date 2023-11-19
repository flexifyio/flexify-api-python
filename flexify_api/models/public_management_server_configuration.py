# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.13.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class PublicManagementServerConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'anonymous_signup_with_microsoft': 'bool',
        'anonymous_signup_with_password': 'bool',
        'billing_enabled': 'bool',
        'have_users': 'bool',
        'management_server_build_number': 'str',
        'single_engine': 'bool',
        'single_user_mode': 'bool',
        'sso_config': 'PublicAuthenticationConfiguration'
    }

    attribute_map = {
        'anonymous_signup_with_microsoft': 'anonymousSignupWithMicrosoft',
        'anonymous_signup_with_password': 'anonymousSignupWithPassword',
        'billing_enabled': 'billingEnabled',
        'have_users': 'haveUsers',
        'management_server_build_number': 'managementServerBuildNumber',
        'single_engine': 'singleEngine',
        'single_user_mode': 'singleUserMode',
        'sso_config': 'ssoConfig'
    }

    def __init__(self, anonymous_signup_with_microsoft=None, anonymous_signup_with_password=None, billing_enabled=None, have_users=None, management_server_build_number=None, single_engine=None, single_user_mode=None, sso_config=None, _configuration=None):  # noqa: E501
        """PublicManagementServerConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._anonymous_signup_with_microsoft = None
        self._anonymous_signup_with_password = None
        self._billing_enabled = None
        self._have_users = None
        self._management_server_build_number = None
        self._single_engine = None
        self._single_user_mode = None
        self._sso_config = None
        self.discriminator = None

        if anonymous_signup_with_microsoft is not None:
            self.anonymous_signup_with_microsoft = anonymous_signup_with_microsoft
        if anonymous_signup_with_password is not None:
            self.anonymous_signup_with_password = anonymous_signup_with_password
        if billing_enabled is not None:
            self.billing_enabled = billing_enabled
        if have_users is not None:
            self.have_users = have_users
        if management_server_build_number is not None:
            self.management_server_build_number = management_server_build_number
        if single_engine is not None:
            self.single_engine = single_engine
        if single_user_mode is not None:
            self.single_user_mode = single_user_mode
        if sso_config is not None:
            self.sso_config = sso_config

    @property
    def anonymous_signup_with_microsoft(self):
        """Gets the anonymous_signup_with_microsoft of this PublicManagementServerConfiguration.  # noqa: E501

        Allow anonymous signup with microsoft  # noqa: E501

        :return: The anonymous_signup_with_microsoft of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_signup_with_microsoft

    @anonymous_signup_with_microsoft.setter
    def anonymous_signup_with_microsoft(self, anonymous_signup_with_microsoft):
        """Sets the anonymous_signup_with_microsoft of this PublicManagementServerConfiguration.

        Allow anonymous signup with microsoft  # noqa: E501

        :param anonymous_signup_with_microsoft: The anonymous_signup_with_microsoft of this PublicManagementServerConfiguration.  # noqa: E501
        :type: bool
        """

        self._anonymous_signup_with_microsoft = anonymous_signup_with_microsoft

    @property
    def anonymous_signup_with_password(self):
        """Gets the anonymous_signup_with_password of this PublicManagementServerConfiguration.  # noqa: E501

        Allow anonymous signup with password  # noqa: E501

        :return: The anonymous_signup_with_password of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_signup_with_password

    @anonymous_signup_with_password.setter
    def anonymous_signup_with_password(self, anonymous_signup_with_password):
        """Sets the anonymous_signup_with_password of this PublicManagementServerConfiguration.

        Allow anonymous signup with password  # noqa: E501

        :param anonymous_signup_with_password: The anonymous_signup_with_password of this PublicManagementServerConfiguration.  # noqa: E501
        :type: bool
        """

        self._anonymous_signup_with_password = anonymous_signup_with_password

    @property
    def billing_enabled(self):
        """Gets the billing_enabled of this PublicManagementServerConfiguration.  # noqa: E501

        Billing-related content to be shown on web console  # noqa: E501

        :return: The billing_enabled of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._billing_enabled

    @billing_enabled.setter
    def billing_enabled(self, billing_enabled):
        """Sets the billing_enabled of this PublicManagementServerConfiguration.

        Billing-related content to be shown on web console  # noqa: E501

        :param billing_enabled: The billing_enabled of this PublicManagementServerConfiguration.  # noqa: E501
        :type: bool
        """

        self._billing_enabled = billing_enabled

    @property
    def have_users(self):
        """Gets the have_users of this PublicManagementServerConfiguration.  # noqa: E501

        Specifies if at least one user is configured  # noqa: E501

        :return: The have_users of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._have_users

    @have_users.setter
    def have_users(self, have_users):
        """Sets the have_users of this PublicManagementServerConfiguration.

        Specifies if at least one user is configured  # noqa: E501

        :param have_users: The have_users of this PublicManagementServerConfiguration.  # noqa: E501
        :type: bool
        """

        self._have_users = have_users

    @property
    def management_server_build_number(self):
        """Gets the management_server_build_number of this PublicManagementServerConfiguration.  # noqa: E501

        Management Server build number  # noqa: E501

        :return: The management_server_build_number of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._management_server_build_number

    @management_server_build_number.setter
    def management_server_build_number(self, management_server_build_number):
        """Sets the management_server_build_number of this PublicManagementServerConfiguration.

        Management Server build number  # noqa: E501

        :param management_server_build_number: The management_server_build_number of this PublicManagementServerConfiguration.  # noqa: E501
        :type: str
        """

        self._management_server_build_number = management_server_build_number

    @property
    def single_engine(self):
        """Gets the single_engine of this PublicManagementServerConfiguration.  # noqa: E501

        Only one engine can be created with web console  # noqa: E501

        :return: The single_engine of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._single_engine

    @single_engine.setter
    def single_engine(self, single_engine):
        """Sets the single_engine of this PublicManagementServerConfiguration.

        Only one engine can be created with web console  # noqa: E501

        :param single_engine: The single_engine of this PublicManagementServerConfiguration.  # noqa: E501
        :type: bool
        """

        self._single_engine = single_engine

    @property
    def single_user_mode(self):
        """Gets the single_user_mode of this PublicManagementServerConfiguration.  # noqa: E501

        In the single user mode only one user account is possible  # noqa: E501

        :return: The single_user_mode of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._single_user_mode

    @single_user_mode.setter
    def single_user_mode(self, single_user_mode):
        """Sets the single_user_mode of this PublicManagementServerConfiguration.

        In the single user mode only one user account is possible  # noqa: E501

        :param single_user_mode: The single_user_mode of this PublicManagementServerConfiguration.  # noqa: E501
        :type: bool
        """

        self._single_user_mode = single_user_mode

    @property
    def sso_config(self):
        """Gets the sso_config of this PublicManagementServerConfiguration.  # noqa: E501

        Configuration for SSO  # noqa: E501

        :return: The sso_config of this PublicManagementServerConfiguration.  # noqa: E501
        :rtype: PublicAuthenticationConfiguration
        """
        return self._sso_config

    @sso_config.setter
    def sso_config(self, sso_config):
        """Sets the sso_config of this PublicManagementServerConfiguration.

        Configuration for SSO  # noqa: E501

        :param sso_config: The sso_config of this PublicManagementServerConfiguration.  # noqa: E501
        :type: PublicAuthenticationConfiguration
        """

        self._sso_config = sso_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PublicManagementServerConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicManagementServerConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicManagementServerConfiguration):
            return True

        return self.to_dict() != other.to_dict()
