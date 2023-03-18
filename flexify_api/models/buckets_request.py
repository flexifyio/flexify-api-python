# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.12
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class BucketsRequest(object):
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
        'bucket_names': 'list[str]',
        'refresh': 'bool'
    }

    attribute_map = {
        'bucket_names': 'bucketNames',
        'refresh': 'refresh'
    }

    def __init__(self, bucket_names=None, refresh=None, _configuration=None):  # noqa: E501
        """BucketsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_names = None
        self._refresh = None
        self.discriminator = None

        self.bucket_names = bucket_names
        if refresh is not None:
            self.refresh = refresh

    @property
    def bucket_names(self):
        """Gets the bucket_names of this BucketsRequest.  # noqa: E501


        :return: The bucket_names of this BucketsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bucket_names

    @bucket_names.setter
    def bucket_names(self, bucket_names):
        """Sets the bucket_names of this BucketsRequest.


        :param bucket_names: The bucket_names of this BucketsRequest.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and bucket_names is None:
            raise ValueError("Invalid value for `bucket_names`, must not be `None`")  # noqa: E501

        self._bucket_names = bucket_names

    @property
    def refresh(self):
        """Gets the refresh of this BucketsRequest.  # noqa: E501

        If set to true, we will start calculating statistics for the buckets  # noqa: E501

        :return: The refresh of this BucketsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this BucketsRequest.

        If set to true, we will start calculating statistics for the buckets  # noqa: E501

        :param refresh: The refresh of this BucketsRequest.  # noqa: E501
        :type: bool
        """

        self._refresh = refresh

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
        if issubclass(BucketsRequest, dict):
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
        if not isinstance(other, BucketsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BucketsRequest):
            return True

        return self.to_dict() != other.to_dict()
