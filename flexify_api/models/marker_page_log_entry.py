# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.9
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MarkerPageLogEntry(object):
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
        'content': 'list[LogEntry]',
        'next_marker': 'int'
    }

    attribute_map = {
        'content': 'content',
        'next_marker': 'nextMarker'
    }

    def __init__(self, content=None, next_marker=None):  # noqa: E501
        """MarkerPageLogEntry - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._next_marker = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def content(self):
        """Gets the content of this MarkerPageLogEntry.  # noqa: E501

        Content of the page  # noqa: E501

        :return: The content of this MarkerPageLogEntry.  # noqa: E501
        :rtype: list[LogEntry]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MarkerPageLogEntry.

        Content of the page  # noqa: E501

        :param content: The content of this MarkerPageLogEntry.  # noqa: E501
        :type: list[LogEntry]
        """

        self._content = content

    @property
    def next_marker(self):
        """Gets the next_marker of this MarkerPageLogEntry.  # noqa: E501

        Marker that canbe used to request next page  # noqa: E501

        :return: The next_marker of this MarkerPageLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this MarkerPageLogEntry.

        Marker that canbe used to request next page  # noqa: E501

        :param next_marker: The next_marker of this MarkerPageLogEntry.  # noqa: E501
        :type: int
        """

        self._next_marker = next_marker

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
        if issubclass(MarkerPageLogEntry, dict):
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
        if not isinstance(other, MarkerPageLogEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
