# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class SignUpRequest(object):
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
        'external_id': 'str',
        'password': 'str',
        'profile': 'UserProfile',
        'settings': 'UserSettings',
        'signup_code': 'str',
        'sso_email': 'str',
        'sso_id': 'str',
        'sso_type': 'str'
    }

    attribute_map = {
        'external_id': 'externalId',
        'password': 'password',
        'profile': 'profile',
        'settings': 'settings',
        'signup_code': 'signupCode',
        'sso_email': 'ssoEmail',
        'sso_id': 'ssoId',
        'sso_type': 'ssoType'
    }

    def __init__(self, external_id=None, password=None, profile=None, settings=None, signup_code=None, sso_email=None, sso_id=None, sso_type=None, _configuration=None):  # noqa: E501
        """SignUpRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_id = None
        self._password = None
        self._profile = None
        self._settings = None
        self._signup_code = None
        self._sso_email = None
        self._sso_id = None
        self._sso_type = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        if password is not None:
            self.password = password
        if profile is not None:
            self.profile = profile
        if settings is not None:
            self.settings = settings
        if signup_code is not None:
            self.signup_code = signup_code
        if sso_email is not None:
            self.sso_email = sso_email
        if sso_id is not None:
            self.sso_id = sso_id
        if sso_type is not None:
            self.sso_type = sso_type

    @property
    def external_id(self):
        """Gets the external_id of this SignUpRequest.  # noqa: E501


        :return: The external_id of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SignUpRequest.


        :param external_id: The external_id of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def password(self):
        """Gets the password of this SignUpRequest.  # noqa: E501


        :return: The password of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SignUpRequest.


        :param password: The password of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def profile(self):
        """Gets the profile of this SignUpRequest.  # noqa: E501


        :return: The profile of this SignUpRequest.  # noqa: E501
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SignUpRequest.


        :param profile: The profile of this SignUpRequest.  # noqa: E501
        :type: UserProfile
        """

        self._profile = profile

    @property
    def settings(self):
        """Gets the settings of this SignUpRequest.  # noqa: E501


        :return: The settings of this SignUpRequest.  # noqa: E501
        :rtype: UserSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this SignUpRequest.


        :param settings: The settings of this SignUpRequest.  # noqa: E501
        :type: UserSettings
        """

        self._settings = settings

    @property
    def signup_code(self):
        """Gets the signup_code of this SignUpRequest.  # noqa: E501


        :return: The signup_code of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._signup_code

    @signup_code.setter
    def signup_code(self, signup_code):
        """Sets the signup_code of this SignUpRequest.


        :param signup_code: The signup_code of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._signup_code = signup_code

    @property
    def sso_email(self):
        """Gets the sso_email of this SignUpRequest.  # noqa: E501


        :return: The sso_email of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_email

    @sso_email.setter
    def sso_email(self, sso_email):
        """Sets the sso_email of this SignUpRequest.


        :param sso_email: The sso_email of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._sso_email = sso_email

    @property
    def sso_id(self):
        """Gets the sso_id of this SignUpRequest.  # noqa: E501


        :return: The sso_id of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this SignUpRequest.


        :param sso_id: The sso_id of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

    @property
    def sso_type(self):
        """Gets the sso_type of this SignUpRequest.  # noqa: E501


        :return: The sso_type of this SignUpRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_type

    @sso_type.setter
    def sso_type(self, sso_type):
        """Sets the sso_type of this SignUpRequest.


        :param sso_type: The sso_type of this SignUpRequest.  # noqa: E501
        :type: str
        """

        self._sso_type = sso_type

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
        if issubclass(SignUpRequest, dict):
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
        if not isinstance(other, SignUpRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignUpRequest):
            return True

        return self.to_dict() != other.to_dict()
