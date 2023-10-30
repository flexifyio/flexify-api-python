# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.20-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class VirtualBucketStorageSettings(object):
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
        'delete_objects': 'bool',
        'put_objects': 'bool'
    }

    attribute_map = {
        'delete_objects': 'deleteObjects',
        'put_objects': 'putObjects'
    }

    def __init__(self, delete_objects=None, put_objects=None, _configuration=None):  # noqa: E501
        """VirtualBucketStorageSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delete_objects = None
        self._put_objects = None
        self.discriminator = None

        if delete_objects is not None:
            self.delete_objects = delete_objects
        if put_objects is not None:
            self.put_objects = put_objects

    @property
    def delete_objects(self):
        """Gets the delete_objects of this VirtualBucketStorageSettings.  # noqa: E501

        Delete data from this storage  # noqa: E501

        :return: The delete_objects of this VirtualBucketStorageSettings.  # noqa: E501
        :rtype: bool
        """
        return self._delete_objects

    @delete_objects.setter
    def delete_objects(self, delete_objects):
        """Sets the delete_objects of this VirtualBucketStorageSettings.

        Delete data from this storage  # noqa: E501

        :param delete_objects: The delete_objects of this VirtualBucketStorageSettings.  # noqa: E501
        :type: bool
        """

        self._delete_objects = delete_objects

    @property
    def put_objects(self):
        """Gets the put_objects of this VirtualBucketStorageSettings.  # noqa: E501

        Save new data to this storage  # noqa: E501

        :return: The put_objects of this VirtualBucketStorageSettings.  # noqa: E501
        :rtype: bool
        """
        return self._put_objects

    @put_objects.setter
    def put_objects(self, put_objects):
        """Sets the put_objects of this VirtualBucketStorageSettings.

        Save new data to this storage  # noqa: E501

        :param put_objects: The put_objects of this VirtualBucketStorageSettings.  # noqa: E501
        :type: bool
        """

        self._put_objects = put_objects

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
        if issubclass(VirtualBucketStorageSettings, dict):
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
        if not isinstance(other, VirtualBucketStorageSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualBucketStorageSettings):
            return True

        return self.to_dict() != other.to_dict()
