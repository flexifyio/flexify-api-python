# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.11-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BucketStat(object):
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
        'bytes': 'int',
        'last_refreshed': 'datetime',
        'objects': 'int',
        'region': 'str',
        'state': 'str'
    }

    attribute_map = {
        'bytes': 'bytes',
        'last_refreshed': 'lastRefreshed',
        'objects': 'objects',
        'region': 'region',
        'state': 'state'
    }

    def __init__(self, bytes=None, last_refreshed=None, objects=None, region=None, state=None):  # noqa: E501
        """BucketStat - a model defined in Swagger"""  # noqa: E501

        self._bytes = None
        self._last_refreshed = None
        self._objects = None
        self._region = None
        self._state = None
        self.discriminator = None

        if bytes is not None:
            self.bytes = bytes
        if last_refreshed is not None:
            self.last_refreshed = last_refreshed
        if objects is not None:
            self.objects = objects
        if region is not None:
            self.region = region
        if state is not None:
            self.state = state

    @property
    def bytes(self):
        """Gets the bytes of this BucketStat.  # noqa: E501

        Bytes in this bucket/container  # noqa: E501

        :return: The bytes of this BucketStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this BucketStat.

        Bytes in this bucket/container  # noqa: E501

        :param bytes: The bytes of this BucketStat.  # noqa: E501
        :type: int
        """

        self._bytes = bytes

    @property
    def last_refreshed(self):
        """Gets the last_refreshed of this BucketStat.  # noqa: E501

        Last success refresh operation complete timestamp  # noqa: E501

        :return: The last_refreshed of this BucketStat.  # noqa: E501
        :rtype: datetime
        """
        return self._last_refreshed

    @last_refreshed.setter
    def last_refreshed(self, last_refreshed):
        """Sets the last_refreshed of this BucketStat.

        Last success refresh operation complete timestamp  # noqa: E501

        :param last_refreshed: The last_refreshed of this BucketStat.  # noqa: E501
        :type: datetime
        """

        self._last_refreshed = last_refreshed

    @property
    def objects(self):
        """Gets the objects of this BucketStat.  # noqa: E501

        Objects in this bucket/container  # noqa: E501

        :return: The objects of this BucketStat.  # noqa: E501
        :rtype: int
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this BucketStat.

        Objects in this bucket/container  # noqa: E501

        :param objects: The objects of this BucketStat.  # noqa: E501
        :type: int
        """

        self._objects = objects

    @property
    def region(self):
        """Gets the region of this BucketStat.  # noqa: E501

        Region where this bucket is located  # noqa: E501

        :return: The region of this BucketStat.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BucketStat.

        Region where this bucket is located  # noqa: E501

        :param region: The region of this BucketStat.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def state(self):
        """Gets the state of this BucketStat.  # noqa: E501

        State of the bucket/container  # noqa: E501

        :return: The state of this BucketStat.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BucketStat.

        State of the bucket/container  # noqa: E501

        :param state: The state of this BucketStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "NONE", "OK", "REFRESHING", "WARNING"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if issubclass(BucketStat, dict):
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
        if not isinstance(other, BucketStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
