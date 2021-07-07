# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.6-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AttachVirtualBucketStoragesRequest(object):
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
        'new_storages': 'list[VirtualBucketStorageReq]'
    }

    attribute_map = {
        'new_storages': 'newStorages'
    }

    def __init__(self, new_storages=None):  # noqa: E501
        """AttachVirtualBucketStoragesRequest - a model defined in Swagger"""  # noqa: E501

        self._new_storages = None
        self.discriminator = None

        if new_storages is not None:
            self.new_storages = new_storages

    @property
    def new_storages(self):
        """Gets the new_storages of this AttachVirtualBucketStoragesRequest.  # noqa: E501

        A list of storagea to accounts to virtual bucket  # noqa: E501

        :return: The new_storages of this AttachVirtualBucketStoragesRequest.  # noqa: E501
        :rtype: list[VirtualBucketStorageReq]
        """
        return self._new_storages

    @new_storages.setter
    def new_storages(self, new_storages):
        """Sets the new_storages of this AttachVirtualBucketStoragesRequest.

        A list of storagea to accounts to virtual bucket  # noqa: E501

        :param new_storages: The new_storages of this AttachVirtualBucketStoragesRequest.  # noqa: E501
        :type: list[VirtualBucketStorageReq]
        """

        self._new_storages = new_storages

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
        if issubclass(AttachVirtualBucketStoragesRequest, dict):
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
        if not isinstance(other, AttachVirtualBucketStoragesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
