# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class Slot(object):
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
        'slot_number': 'int',
        'stat': 'SlotStat'
    }

    attribute_map = {
        'slot_number': 'slotNumber',
        'stat': 'stat'
    }

    def __init__(self, slot_number=None, stat=None, _configuration=None):  # noqa: E501
        """Slot - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._slot_number = None
        self._stat = None
        self.discriminator = None

        if slot_number is not None:
            self.slot_number = slot_number
        if stat is not None:
            self.stat = stat

    @property
    def slot_number(self):
        """Gets the slot_number of this Slot.  # noqa: E501


        :return: The slot_number of this Slot.  # noqa: E501
        :rtype: int
        """
        return self._slot_number

    @slot_number.setter
    def slot_number(self, slot_number):
        """Sets the slot_number of this Slot.


        :param slot_number: The slot_number of this Slot.  # noqa: E501
        :type: int
        """

        self._slot_number = slot_number

    @property
    def stat(self):
        """Gets the stat of this Slot.  # noqa: E501


        :return: The stat of this Slot.  # noqa: E501
        :rtype: SlotStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this Slot.


        :param stat: The stat of this Slot.  # noqa: E501
        :type: SlotStat
        """

        self._stat = stat

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
        if issubclass(Slot, dict):
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
        if not isinstance(other, Slot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Slot):
            return True

        return self.to_dict() != other.to_dict()
