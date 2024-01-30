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


class ResetSsoRequest(object):
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
        'settings': 'UserSettings',
        'sso_email': 'str',
        'sso_id': 'str',
        'sso_provider_id': 'str',
        'token': 'str'
    }

    attribute_map = {
        'settings': 'settings',
        'sso_email': 'ssoEmail',
        'sso_id': 'ssoId',
        'sso_provider_id': 'ssoProviderId',
        'token': 'token'
    }

    def __init__(self, settings=None, sso_email=None, sso_id=None, sso_provider_id=None, token=None, _configuration=None):  # noqa: E501
        """ResetSsoRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._settings = None
        self._sso_email = None
        self._sso_id = None
        self._sso_provider_id = None
        self._token = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        if sso_email is not None:
            self.sso_email = sso_email
        if sso_id is not None:
            self.sso_id = sso_id
        if sso_provider_id is not None:
            self.sso_provider_id = sso_provider_id
        if token is not None:
            self.token = token

    @property
    def settings(self):
        """Gets the settings of this ResetSsoRequest.  # noqa: E501


        :return: The settings of this ResetSsoRequest.  # noqa: E501
        :rtype: UserSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ResetSsoRequest.


        :param settings: The settings of this ResetSsoRequest.  # noqa: E501
        :type: UserSettings
        """

        self._settings = settings

    @property
    def sso_email(self):
        """Gets the sso_email of this ResetSsoRequest.  # noqa: E501


        :return: The sso_email of this ResetSsoRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_email

    @sso_email.setter
    def sso_email(self, sso_email):
        """Sets the sso_email of this ResetSsoRequest.


        :param sso_email: The sso_email of this ResetSsoRequest.  # noqa: E501
        :type: str
        """

        self._sso_email = sso_email

    @property
    def sso_id(self):
        """Gets the sso_id of this ResetSsoRequest.  # noqa: E501


        :return: The sso_id of this ResetSsoRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this ResetSsoRequest.


        :param sso_id: The sso_id of this ResetSsoRequest.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

    @property
    def sso_provider_id(self):
        """Gets the sso_provider_id of this ResetSsoRequest.  # noqa: E501


        :return: The sso_provider_id of this ResetSsoRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_provider_id

    @sso_provider_id.setter
    def sso_provider_id(self, sso_provider_id):
        """Sets the sso_provider_id of this ResetSsoRequest.


        :param sso_provider_id: The sso_provider_id of this ResetSsoRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DROPBOX", "DROPBOX_TEAM", "MICROSOFT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sso_provider_id not in allowed_values):
            raise ValueError(
                "Invalid value for `sso_provider_id` ({0}), must be one of {1}"  # noqa: E501
                .format(sso_provider_id, allowed_values)
            )

        self._sso_provider_id = sso_provider_id

    @property
    def token(self):
        """Gets the token of this ResetSsoRequest.  # noqa: E501


        :return: The token of this ResetSsoRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ResetSsoRequest.


        :param token: The token of this ResetSsoRequest.  # noqa: E501
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
        if issubclass(ResetSsoRequest, dict):
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
        if not isinstance(other, ResetSsoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetSsoRequest):
            return True

        return self.to_dict() != other.to_dict()
