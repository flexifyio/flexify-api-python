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


class ChangeSsoMicrosoftRequest(object):
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
        'sso_email': 'str',
        'sso_id': 'str'
    }

    attribute_map = {
        'sso_email': 'ssoEmail',
        'sso_id': 'ssoId'
    }

    def __init__(self, sso_email=None, sso_id=None, _configuration=None):  # noqa: E501
        """ChangeSsoMicrosoftRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sso_email = None
        self._sso_id = None
        self.discriminator = None

        if sso_email is not None:
            self.sso_email = sso_email
        if sso_id is not None:
            self.sso_id = sso_id

    @property
    def sso_email(self):
        """Gets the sso_email of this ChangeSsoMicrosoftRequest.  # noqa: E501


        :return: The sso_email of this ChangeSsoMicrosoftRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_email

    @sso_email.setter
    def sso_email(self, sso_email):
        """Sets the sso_email of this ChangeSsoMicrosoftRequest.


        :param sso_email: The sso_email of this ChangeSsoMicrosoftRequest.  # noqa: E501
        :type: str
        """

        self._sso_email = sso_email

    @property
    def sso_id(self):
        """Gets the sso_id of this ChangeSsoMicrosoftRequest.  # noqa: E501


        :return: The sso_id of this ChangeSsoMicrosoftRequest.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this ChangeSsoMicrosoftRequest.


        :param sso_id: The sso_id of this ChangeSsoMicrosoftRequest.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

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
        if issubclass(ChangeSsoMicrosoftRequest, dict):
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
        if not isinstance(other, ChangeSsoMicrosoftRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeSsoMicrosoftRequest):
            return True

        return self.to_dict() != other.to_dict()
