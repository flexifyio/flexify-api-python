# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.12-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class LogoutRequest(object):
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
        'delete_all_impersonation_tokens': 'bool',
        'delete_all_integration_tokens': 'bool',
        'delete_all_login_tokens': 'bool'
    }

    attribute_map = {
        'delete_all_impersonation_tokens': 'deleteAllImpersonationTokens',
        'delete_all_integration_tokens': 'deleteAllIntegrationTokens',
        'delete_all_login_tokens': 'deleteAllLoginTokens'
    }

    def __init__(self, delete_all_impersonation_tokens=None, delete_all_integration_tokens=None, delete_all_login_tokens=None, _configuration=None):  # noqa: E501
        """LogoutRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delete_all_impersonation_tokens = None
        self._delete_all_integration_tokens = None
        self._delete_all_login_tokens = None
        self.discriminator = None

        if delete_all_impersonation_tokens is not None:
            self.delete_all_impersonation_tokens = delete_all_impersonation_tokens
        if delete_all_integration_tokens is not None:
            self.delete_all_integration_tokens = delete_all_integration_tokens
        if delete_all_login_tokens is not None:
            self.delete_all_login_tokens = delete_all_login_tokens

    @property
    def delete_all_impersonation_tokens(self):
        """Gets the delete_all_impersonation_tokens of this LogoutRequest.  # noqa: E501

        Specifies if all IMPERSONATION tokens should be deleted  # noqa: E501

        :return: The delete_all_impersonation_tokens of this LogoutRequest.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_impersonation_tokens

    @delete_all_impersonation_tokens.setter
    def delete_all_impersonation_tokens(self, delete_all_impersonation_tokens):
        """Sets the delete_all_impersonation_tokens of this LogoutRequest.

        Specifies if all IMPERSONATION tokens should be deleted  # noqa: E501

        :param delete_all_impersonation_tokens: The delete_all_impersonation_tokens of this LogoutRequest.  # noqa: E501
        :type: bool
        """

        self._delete_all_impersonation_tokens = delete_all_impersonation_tokens

    @property
    def delete_all_integration_tokens(self):
        """Gets the delete_all_integration_tokens of this LogoutRequest.  # noqa: E501

        Specifies if all INTEGRATION tokens should be deleted  # noqa: E501

        :return: The delete_all_integration_tokens of this LogoutRequest.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_integration_tokens

    @delete_all_integration_tokens.setter
    def delete_all_integration_tokens(self, delete_all_integration_tokens):
        """Sets the delete_all_integration_tokens of this LogoutRequest.

        Specifies if all INTEGRATION tokens should be deleted  # noqa: E501

        :param delete_all_integration_tokens: The delete_all_integration_tokens of this LogoutRequest.  # noqa: E501
        :type: bool
        """

        self._delete_all_integration_tokens = delete_all_integration_tokens

    @property
    def delete_all_login_tokens(self):
        """Gets the delete_all_login_tokens of this LogoutRequest.  # noqa: E501

        Specifies if all LOGIN tokens should be deleted  # noqa: E501

        :return: The delete_all_login_tokens of this LogoutRequest.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_login_tokens

    @delete_all_login_tokens.setter
    def delete_all_login_tokens(self, delete_all_login_tokens):
        """Sets the delete_all_login_tokens of this LogoutRequest.

        Specifies if all LOGIN tokens should be deleted  # noqa: E501

        :param delete_all_login_tokens: The delete_all_login_tokens of this LogoutRequest.  # noqa: E501
        :type: bool
        """

        self._delete_all_login_tokens = delete_all_login_tokens

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
        if issubclass(LogoutRequest, dict):
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
        if not isinstance(other, LogoutRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogoutRequest):
            return True

        return self.to_dict() != other.to_dict()
