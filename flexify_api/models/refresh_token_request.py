# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.13.0
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class RefreshTokenRequest(object):
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
        'oauth_provider_id': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'oauth_provider_id': 'oauthProviderId',
        'refresh_token': 'refreshToken'
    }

    def __init__(self, oauth_provider_id=None, refresh_token=None, _configuration=None):  # noqa: E501
        """RefreshTokenRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._oauth_provider_id = None
        self._refresh_token = None
        self.discriminator = None

        self.oauth_provider_id = oauth_provider_id
        self.refresh_token = refresh_token

    @property
    def oauth_provider_id(self):
        """Gets the oauth_provider_id of this RefreshTokenRequest.  # noqa: E501


        :return: The oauth_provider_id of this RefreshTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._oauth_provider_id

    @oauth_provider_id.setter
    def oauth_provider_id(self, oauth_provider_id):
        """Sets the oauth_provider_id of this RefreshTokenRequest.


        :param oauth_provider_id: The oauth_provider_id of this RefreshTokenRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and oauth_provider_id is None:
            raise ValueError("Invalid value for `oauth_provider_id`, must not be `None`")  # noqa: E501
        allowed_values = ["DROPBOX", "DROPBOX_TEAM", "MICROSOFT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                oauth_provider_id not in allowed_values):
            raise ValueError(
                "Invalid value for `oauth_provider_id` ({0}), must be one of {1}"  # noqa: E501
                .format(oauth_provider_id, allowed_values)
            )

        self._oauth_provider_id = oauth_provider_id

    @property
    def refresh_token(self):
        """Gets the refresh_token of this RefreshTokenRequest.  # noqa: E501


        :return: The refresh_token of this RefreshTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this RefreshTokenRequest.


        :param refresh_token: The refresh_token of this RefreshTokenRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

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
        if issubclass(RefreshTokenRequest, dict):
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
        if not isinstance(other, RefreshTokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefreshTokenRequest):
            return True

        return self.to_dict() != other.to_dict()
