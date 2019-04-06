# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.8.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.models.user_profile import UserProfile  # noqa: F401,E501


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
        'password': 'str',
        'profile': 'UserProfile',
        'signup_code': 'str'
    }

    attribute_map = {
        'password': 'password',
        'profile': 'profile',
        'signup_code': 'signupCode'
    }

    def __init__(self, password=None, profile=None, signup_code=None):  # noqa: E501
        """SignUpRequest - a model defined in Swagger"""  # noqa: E501

        self._password = None
        self._profile = None
        self._signup_code = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if profile is not None:
            self.profile = profile
        if signup_code is not None:
            self.signup_code = signup_code

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
