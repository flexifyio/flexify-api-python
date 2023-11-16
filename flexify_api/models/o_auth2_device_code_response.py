# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class OAuth2DeviceCodeResponse(object):
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
        'device_code': 'str',
        'expires_in': 'int',
        'interval': 'int',
        'message': 'str',
        'user_code': 'str',
        'verification_uri': 'str'
    }

    attribute_map = {
        'device_code': 'device_code',
        'expires_in': 'expires_in',
        'interval': 'interval',
        'message': 'message',
        'user_code': 'user_code',
        'verification_uri': 'verification_uri'
    }

    def __init__(self, device_code=None, expires_in=None, interval=None, message=None, user_code=None, verification_uri=None, _configuration=None):  # noqa: E501
        """OAuth2DeviceCodeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_code = None
        self._expires_in = None
        self._interval = None
        self._message = None
        self._user_code = None
        self._verification_uri = None
        self.discriminator = None

        if device_code is not None:
            self.device_code = device_code
        if expires_in is not None:
            self.expires_in = expires_in
        if interval is not None:
            self.interval = interval
        if message is not None:
            self.message = message
        if user_code is not None:
            self.user_code = user_code
        if verification_uri is not None:
            self.verification_uri = verification_uri

    @property
    def device_code(self):
        """Gets the device_code of this OAuth2DeviceCodeResponse.  # noqa: E501


        :return: The device_code of this OAuth2DeviceCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this OAuth2DeviceCodeResponse.


        :param device_code: The device_code of this OAuth2DeviceCodeResponse.  # noqa: E501
        :type: str
        """

        self._device_code = device_code

    @property
    def expires_in(self):
        """Gets the expires_in of this OAuth2DeviceCodeResponse.  # noqa: E501


        :return: The expires_in of this OAuth2DeviceCodeResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this OAuth2DeviceCodeResponse.


        :param expires_in: The expires_in of this OAuth2DeviceCodeResponse.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def interval(self):
        """Gets the interval of this OAuth2DeviceCodeResponse.  # noqa: E501


        :return: The interval of this OAuth2DeviceCodeResponse.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this OAuth2DeviceCodeResponse.


        :param interval: The interval of this OAuth2DeviceCodeResponse.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def message(self):
        """Gets the message of this OAuth2DeviceCodeResponse.  # noqa: E501


        :return: The message of this OAuth2DeviceCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OAuth2DeviceCodeResponse.


        :param message: The message of this OAuth2DeviceCodeResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def user_code(self):
        """Gets the user_code of this OAuth2DeviceCodeResponse.  # noqa: E501


        :return: The user_code of this OAuth2DeviceCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_code

    @user_code.setter
    def user_code(self, user_code):
        """Sets the user_code of this OAuth2DeviceCodeResponse.


        :param user_code: The user_code of this OAuth2DeviceCodeResponse.  # noqa: E501
        :type: str
        """

        self._user_code = user_code

    @property
    def verification_uri(self):
        """Gets the verification_uri of this OAuth2DeviceCodeResponse.  # noqa: E501


        :return: The verification_uri of this OAuth2DeviceCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._verification_uri

    @verification_uri.setter
    def verification_uri(self, verification_uri):
        """Sets the verification_uri of this OAuth2DeviceCodeResponse.


        :param verification_uri: The verification_uri of this OAuth2DeviceCodeResponse.  # noqa: E501
        :type: str
        """

        self._verification_uri = verification_uri

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
        if issubclass(OAuth2DeviceCodeResponse, dict):
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
        if not isinstance(other, OAuth2DeviceCodeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuth2DeviceCodeResponse):
            return True

        return self.to_dict() != other.to_dict()
