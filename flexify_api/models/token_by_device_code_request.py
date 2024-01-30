# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class TokenByDeviceCodeRequest(object):
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
        'oauth_provider_id': 'str'
    }

    attribute_map = {
        'device_code': 'deviceCode',
        'oauth_provider_id': 'oauthProviderId'
    }

    def __init__(self, device_code=None, oauth_provider_id=None, _configuration=None):  # noqa: E501
        """TokenByDeviceCodeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_code = None
        self._oauth_provider_id = None
        self.discriminator = None

        self.device_code = device_code
        self.oauth_provider_id = oauth_provider_id

    @property
    def device_code(self):
        """Gets the device_code of this TokenByDeviceCodeRequest.  # noqa: E501


        :return: The device_code of this TokenByDeviceCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this TokenByDeviceCodeRequest.


        :param device_code: The device_code of this TokenByDeviceCodeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and device_code is None:
            raise ValueError("Invalid value for `device_code`, must not be `None`")  # noqa: E501

        self._device_code = device_code

    @property
    def oauth_provider_id(self):
        """Gets the oauth_provider_id of this TokenByDeviceCodeRequest.  # noqa: E501


        :return: The oauth_provider_id of this TokenByDeviceCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._oauth_provider_id

    @oauth_provider_id.setter
    def oauth_provider_id(self, oauth_provider_id):
        """Sets the oauth_provider_id of this TokenByDeviceCodeRequest.


        :param oauth_provider_id: The oauth_provider_id of this TokenByDeviceCodeRequest.  # noqa: E501
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
        if issubclass(TokenByDeviceCodeRequest, dict):
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
        if not isinstance(other, TokenByDeviceCodeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenByDeviceCodeRequest):
            return True

        return self.to_dict() != other.to_dict()
