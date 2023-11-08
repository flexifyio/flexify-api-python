# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class CloudLocationRes(object):
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
        'cloud_name': 'str',
        'cloud_region': 'str',
        'engines': 'int'
    }

    attribute_map = {
        'cloud_name': 'cloudName',
        'cloud_region': 'cloudRegion',
        'engines': 'engines'
    }

    def __init__(self, cloud_name=None, cloud_region=None, engines=None, _configuration=None):  # noqa: E501
        """CloudLocationRes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloud_name = None
        self._cloud_region = None
        self._engines = None
        self.discriminator = None

        if cloud_name is not None:
            self.cloud_name = cloud_name
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if engines is not None:
            self.engines = engines

    @property
    def cloud_name(self):
        """Gets the cloud_name of this CloudLocationRes.  # noqa: E501

        Cloud name  # noqa: E501

        :return: The cloud_name of this CloudLocationRes.  # noqa: E501
        :rtype: str
        """
        return self._cloud_name

    @cloud_name.setter
    def cloud_name(self, cloud_name):
        """Sets the cloud_name of this CloudLocationRes.

        Cloud name  # noqa: E501

        :param cloud_name: The cloud_name of this CloudLocationRes.  # noqa: E501
        :type: str
        """

        self._cloud_name = cloud_name

    @property
    def cloud_region(self):
        """Gets the cloud_region of this CloudLocationRes.  # noqa: E501

        Cloud Region  # noqa: E501

        :return: The cloud_region of this CloudLocationRes.  # noqa: E501
        :rtype: str
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this CloudLocationRes.

        Cloud Region  # noqa: E501

        :param cloud_region: The cloud_region of this CloudLocationRes.  # noqa: E501
        :type: str
        """

        self._cloud_region = cloud_region

    @property
    def engines(self):
        """Gets the engines of this CloudLocationRes.  # noqa: E501

        Number of Available Engines in the location  # noqa: E501

        :return: The engines of this CloudLocationRes.  # noqa: E501
        :rtype: int
        """
        return self._engines

    @engines.setter
    def engines(self, engines):
        """Sets the engines of this CloudLocationRes.

        Number of Available Engines in the location  # noqa: E501

        :param engines: The engines of this CloudLocationRes.  # noqa: E501
        :type: int
        """

        self._engines = engines

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
        if issubclass(CloudLocationRes, dict):
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
        if not isinstance(other, CloudLocationRes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudLocationRes):
            return True

        return self.to_dict() != other.to_dict()
