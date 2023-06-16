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


class Sort(object):
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
        'empty': 'bool',
        'sorted': 'bool',
        'unsorted': 'bool'
    }

    attribute_map = {
        'empty': 'empty',
        'sorted': 'sorted',
        'unsorted': 'unsorted'
    }

    def __init__(self, empty=None, sorted=None, unsorted=None, _configuration=None):  # noqa: E501
        """Sort - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._empty = None
        self._sorted = None
        self._unsorted = None
        self.discriminator = None

        if empty is not None:
            self.empty = empty
        if sorted is not None:
            self.sorted = sorted
        if unsorted is not None:
            self.unsorted = unsorted

    @property
    def empty(self):
        """Gets the empty of this Sort.  # noqa: E501


        :return: The empty of this Sort.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this Sort.


        :param empty: The empty of this Sort.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def sorted(self):
        """Gets the sorted of this Sort.  # noqa: E501


        :return: The sorted of this Sort.  # noqa: E501
        :rtype: bool
        """
        return self._sorted

    @sorted.setter
    def sorted(self, sorted):
        """Sets the sorted of this Sort.


        :param sorted: The sorted of this Sort.  # noqa: E501
        :type: bool
        """

        self._sorted = sorted

    @property
    def unsorted(self):
        """Gets the unsorted of this Sort.  # noqa: E501


        :return: The unsorted of this Sort.  # noqa: E501
        :rtype: bool
        """
        return self._unsorted

    @unsorted.setter
    def unsorted(self, unsorted):
        """Sets the unsorted of this Sort.


        :param unsorted: The unsorted of this Sort.  # noqa: E501
        :type: bool
        """

        self._unsorted = unsorted

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
        if issubclass(Sort, dict):
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
        if not isinstance(other, Sort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sort):
            return True

        return self.to_dict() != other.to_dict()
