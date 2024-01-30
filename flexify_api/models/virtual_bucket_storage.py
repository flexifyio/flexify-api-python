# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.15.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class VirtualBucketStorage(object):
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
        'bucket_id': 'int',
        'settings': 'VirtualBucketStorageSettings'
    }

    attribute_map = {
        'bucket_id': 'bucketId',
        'settings': 'settings'
    }

    def __init__(self, bucket_id=None, settings=None, _configuration=None):  # noqa: E501
        """VirtualBucketStorage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_id = None
        self._settings = None
        self.discriminator = None

        if bucket_id is not None:
            self.bucket_id = bucket_id
        if settings is not None:
            self.settings = settings

    @property
    def bucket_id(self):
        """Gets the bucket_id of this VirtualBucketStorage.  # noqa: E501

        ID of attached bucket  # noqa: E501

        :return: The bucket_id of this VirtualBucketStorage.  # noqa: E501
        :rtype: int
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this VirtualBucketStorage.

        ID of attached bucket  # noqa: E501

        :param bucket_id: The bucket_id of this VirtualBucketStorage.  # noqa: E501
        :type: int
        """

        self._bucket_id = bucket_id

    @property
    def settings(self):
        """Gets the settings of this VirtualBucketStorage.  # noqa: E501

        Attached storage configuration  # noqa: E501

        :return: The settings of this VirtualBucketStorage.  # noqa: E501
        :rtype: VirtualBucketStorageSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this VirtualBucketStorage.

        Attached storage configuration  # noqa: E501

        :param settings: The settings of this VirtualBucketStorage.  # noqa: E501
        :type: VirtualBucketStorageSettings
        """

        self._settings = settings

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
        if issubclass(VirtualBucketStorage, dict):
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
        if not isinstance(other, VirtualBucketStorage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualBucketStorage):
            return True

        return self.to_dict() != other.to_dict()
