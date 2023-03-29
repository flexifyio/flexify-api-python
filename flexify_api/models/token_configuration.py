# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.13
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class TokenConfiguration(object):
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
        'comments': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'token_type': 'tokenType'
    }

    def __init__(self, comments=None, token_type=None, _configuration=None):  # noqa: E501
        """TokenConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._comments = None
        self._token_type = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if token_type is not None:
            self.token_type = token_type

    @property
    def comments(self):
        """Gets the comments of this TokenConfiguration.  # noqa: E501

        User-defined comments for the token  # noqa: E501

        :return: The comments of this TokenConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TokenConfiguration.

        User-defined comments for the token  # noqa: E501

        :param comments: The comments of this TokenConfiguration.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def token_type(self):
        """Gets the token_type of this TokenConfiguration.  # noqa: E501

        Type of this token  # noqa: E501

        :return: The token_type of this TokenConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this TokenConfiguration.

        Type of this token  # noqa: E501

        :param token_type: The token_type of this TokenConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["API", "IMPERSONATION", "INTEGRATION", "LOGIN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                token_type not in allowed_values):
            raise ValueError(
                "Invalid value for `token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(token_type, allowed_values)
            )

        self._token_type = token_type

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
        if issubclass(TokenConfiguration, dict):
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
        if not isinstance(other, TokenConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenConfiguration):
            return True

        return self.to_dict() != other.to_dict()
