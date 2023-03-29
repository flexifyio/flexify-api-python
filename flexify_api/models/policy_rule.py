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


class PolicyRule(object):
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
        'action': 'str',
        'key_pattern': 'str',
        'operations': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'key_pattern': 'keyPattern',
        'operations': 'operations'
    }

    def __init__(self, action=None, key_pattern=None, operations=None, _configuration=None):  # noqa: E501
        """PolicyRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._key_pattern = None
        self._operations = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if key_pattern is not None:
            self.key_pattern = key_pattern
        if operations is not None:
            self.operations = operations

    @property
    def action(self):
        """Gets the action of this PolicyRule.  # noqa: E501


        :return: The action of this PolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PolicyRule.


        :param action: The action of this PolicyRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "allowPublic", "forbid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def key_pattern(self):
        """Gets the key_pattern of this PolicyRule.  # noqa: E501


        :return: The key_pattern of this PolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._key_pattern

    @key_pattern.setter
    def key_pattern(self, key_pattern):
        """Sets the key_pattern of this PolicyRule.


        :param key_pattern: The key_pattern of this PolicyRule.  # noqa: E501
        :type: str
        """

        self._key_pattern = key_pattern

    @property
    def operations(self):
        """Gets the operations of this PolicyRule.  # noqa: E501


        :return: The operations of this PolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this PolicyRule.


        :param operations: The operations of this PolicyRule.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["DeleteObject", "GetObject", "HeadBucket", "ListObjects", "PutObject", "RestoreObject"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(operations).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `operations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(operations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._operations = operations

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
        if issubclass(PolicyRule, dict):
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
        if not isinstance(other, PolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyRule):
            return True

        return self.to_dict() != other.to_dict()
