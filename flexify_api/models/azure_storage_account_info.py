# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class AzureStorageAccountInfo(object):
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
        'id': 'str',
        'kind': 'str',
        'location': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'kind': 'kind',
        'location': 'location',
        'name': 'name'
    }

    def __init__(self, id=None, kind=None, location=None, name=None, _configuration=None):  # noqa: E501
        """AzureStorageAccountInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._kind = None
        self._location = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if kind is not None:
            self.kind = kind
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this AzureStorageAccountInfo.  # noqa: E501


        :return: The id of this AzureStorageAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureStorageAccountInfo.


        :param id: The id of this AzureStorageAccountInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this AzureStorageAccountInfo.  # noqa: E501


        :return: The kind of this AzureStorageAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AzureStorageAccountInfo.


        :param kind: The kind of this AzureStorageAccountInfo.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def location(self):
        """Gets the location of this AzureStorageAccountInfo.  # noqa: E501


        :return: The location of this AzureStorageAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AzureStorageAccountInfo.


        :param location: The location of this AzureStorageAccountInfo.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this AzureStorageAccountInfo.  # noqa: E501


        :return: The name of this AzureStorageAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureStorageAccountInfo.


        :param name: The name of this AzureStorageAccountInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(AzureStorageAccountInfo, dict):
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
        if not isinstance(other, AzureStorageAccountInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureStorageAccountInfo):
            return True

        return self.to_dict() != other.to_dict()
