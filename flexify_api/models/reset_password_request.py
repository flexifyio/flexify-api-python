# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.9
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ResetPasswordRequest(object):
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
        'new_password': 'str',
        'settings': 'UserSettings',
        'token': 'str'
    }

    attribute_map = {
        'new_password': 'newPassword',
        'settings': 'settings',
        'token': 'token'
    }

    def __init__(self, new_password=None, settings=None, token=None):  # noqa: E501
        """ResetPasswordRequest - a model defined in Swagger"""  # noqa: E501

        self._new_password = None
        self._settings = None
        self._token = None
        self.discriminator = None

        if new_password is not None:
            self.new_password = new_password
        if settings is not None:
            self.settings = settings
        if token is not None:
            self.token = token

    @property
    def new_password(self):
        """Gets the new_password of this ResetPasswordRequest.  # noqa: E501


        :return: The new_password of this ResetPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetPasswordRequest.


        :param new_password: The new_password of this ResetPasswordRequest.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

    @property
    def settings(self):
        """Gets the settings of this ResetPasswordRequest.  # noqa: E501


        :return: The settings of this ResetPasswordRequest.  # noqa: E501
        :rtype: UserSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ResetPasswordRequest.


        :param settings: The settings of this ResetPasswordRequest.  # noqa: E501
        :type: UserSettings
        """

        self._settings = settings

    @property
    def token(self):
        """Gets the token of this ResetPasswordRequest.  # noqa: E501


        :return: The token of this ResetPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ResetPasswordRequest.


        :param token: The token of this ResetPasswordRequest.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(ResetPasswordRequest, dict):
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
        if not isinstance(other, ResetPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
