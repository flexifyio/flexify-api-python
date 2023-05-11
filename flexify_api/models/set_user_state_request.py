# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class SetUserStateRequest(object):
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
        'new_state': 'str'
    }

    attribute_map = {
        'new_state': 'newState'
    }

    def __init__(self, new_state=None, _configuration=None):  # noqa: E501
        """SetUserStateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_state = None
        self.discriminator = None

        if new_state is not None:
            self.new_state = new_state

    @property
    def new_state(self):
        """Gets the new_state of this SetUserStateRequest.  # noqa: E501


        :return: The new_state of this SetUserStateRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_state

    @new_state.setter
    def new_state(self, new_state):
        """Sets the new_state of this SetUserStateRequest.


        :param new_state: The new_state of this SetUserStateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "DISABLED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                new_state not in allowed_values):
            raise ValueError(
                "Invalid value for `new_state` ({0}), must be one of {1}"  # noqa: E501
                .format(new_state, allowed_values)
            )

        self._new_state = new_state

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
        if issubclass(SetUserStateRequest, dict):
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
        if not isinstance(other, SetUserStateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetUserStateRequest):
            return True

        return self.to_dict() != other.to_dict()
