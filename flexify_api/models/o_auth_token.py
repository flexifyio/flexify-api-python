# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class OAuthToken(object):
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
        'access_token': 'str',
        'expires_at': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'expires_at': 'expiresAt',
        'refresh_token': 'refreshToken'
    }

    def __init__(self, access_token=None, expires_at=None, refresh_token=None, _configuration=None):  # noqa: E501
        """OAuthToken - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._expires_at = None
        self._refresh_token = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if expires_at is not None:
            self.expires_at = expires_at
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def access_token(self):
        """Gets the access_token of this OAuthToken.  # noqa: E501


        :return: The access_token of this OAuthToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OAuthToken.


        :param access_token: The access_token of this OAuthToken.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_at(self):
        """Gets the expires_at of this OAuthToken.  # noqa: E501


        :return: The expires_at of this OAuthToken.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this OAuthToken.


        :param expires_at: The expires_at of this OAuthToken.  # noqa: E501
        :type: str
        """

        self._expires_at = expires_at

    @property
    def refresh_token(self):
        """Gets the refresh_token of this OAuthToken.  # noqa: E501


        :return: The refresh_token of this OAuthToken.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this OAuthToken.


        :param refresh_token: The refresh_token of this OAuthToken.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

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
        if issubclass(OAuthToken, dict):
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
        if not isinstance(other, OAuthToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuthToken):
            return True

        return self.to_dict() != other.to_dict()
