# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.4
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PublicAuthenticationConfiguration(object):
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
        'configured': 'bool',
        'single_user_mode': 'bool'
    }

    attribute_map = {
        'configured': 'configured',
        'single_user_mode': 'singleUserMode'
    }

    def __init__(self, configured=None, single_user_mode=None):  # noqa: E501
        """PublicAuthenticationConfiguration - a model defined in Swagger"""  # noqa: E501

        self._configured = None
        self._single_user_mode = None
        self.discriminator = None

        if configured is not None:
            self.configured = configured
        if single_user_mode is not None:
            self.single_user_mode = single_user_mode

    @property
    def configured(self):
        """Gets the configured of this PublicAuthenticationConfiguration.  # noqa: E501

        Specifics if credentials are configured on a single user mode  # noqa: E501

        :return: The configured of this PublicAuthenticationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this PublicAuthenticationConfiguration.

        Specifics if credentials are configured on a single user mode  # noqa: E501

        :param configured: The configured of this PublicAuthenticationConfiguration.  # noqa: E501
        :type: bool
        """

        self._configured = configured

    @property
    def single_user_mode(self):
        """Gets the single_user_mode of this PublicAuthenticationConfiguration.  # noqa: E501

        In the single user mode only one user account is possible  # noqa: E501

        :return: The single_user_mode of this PublicAuthenticationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._single_user_mode

    @single_user_mode.setter
    def single_user_mode(self, single_user_mode):
        """Sets the single_user_mode of this PublicAuthenticationConfiguration.

        In the single user mode only one user account is possible  # noqa: E501

        :param single_user_mode: The single_user_mode of this PublicAuthenticationConfiguration.  # noqa: E501
        :type: bool
        """

        self._single_user_mode = single_user_mode

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
        if issubclass(PublicAuthenticationConfiguration, dict):
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
        if not isinstance(other, PublicAuthenticationConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
