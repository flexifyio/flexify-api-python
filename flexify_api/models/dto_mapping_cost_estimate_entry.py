# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class DtoMappingCostEstimateEntry(object):
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
        'cost': 'Money',
        'dest_region': 'str',
        'engine_location': 'CloudLocationRes',
        'engines_count': 'int',
        'price': 'Price',
        'source_region': 'str',
        'usage': 'int'
    }

    attribute_map = {
        'cost': 'cost',
        'dest_region': 'destRegion',
        'engine_location': 'engineLocation',
        'engines_count': 'enginesCount',
        'price': 'price',
        'source_region': 'sourceRegion',
        'usage': 'usage'
    }

    def __init__(self, cost=None, dest_region=None, engine_location=None, engines_count=None, price=None, source_region=None, usage=None, _configuration=None):  # noqa: E501
        """DtoMappingCostEstimateEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cost = None
        self._dest_region = None
        self._engine_location = None
        self._engines_count = None
        self._price = None
        self._source_region = None
        self._usage = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if dest_region is not None:
            self.dest_region = dest_region
        if engine_location is not None:
            self.engine_location = engine_location
        if engines_count is not None:
            self.engines_count = engines_count
        if price is not None:
            self.price = price
        if source_region is not None:
            self.source_region = source_region
        if usage is not None:
            self.usage = usage

    @property
    def cost(self):
        """Gets the cost of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The cost of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: Money
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this DtoMappingCostEstimateEntry.


        :param cost: The cost of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: Money
        """

        self._cost = cost

    @property
    def dest_region(self):
        """Gets the dest_region of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The dest_region of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: str
        """
        return self._dest_region

    @dest_region.setter
    def dest_region(self, dest_region):
        """Sets the dest_region of this DtoMappingCostEstimateEntry.


        :param dest_region: The dest_region of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: str
        """

        self._dest_region = dest_region

    @property
    def engine_location(self):
        """Gets the engine_location of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The engine_location of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: CloudLocationRes
        """
        return self._engine_location

    @engine_location.setter
    def engine_location(self, engine_location):
        """Sets the engine_location of this DtoMappingCostEstimateEntry.


        :param engine_location: The engine_location of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: CloudLocationRes
        """

        self._engine_location = engine_location

    @property
    def engines_count(self):
        """Gets the engines_count of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The engines_count of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: int
        """
        return self._engines_count

    @engines_count.setter
    def engines_count(self, engines_count):
        """Sets the engines_count of this DtoMappingCostEstimateEntry.


        :param engines_count: The engines_count of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: int
        """

        self._engines_count = engines_count

    @property
    def price(self):
        """Gets the price of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The price of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this DtoMappingCostEstimateEntry.


        :param price: The price of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def source_region(self):
        """Gets the source_region of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The source_region of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this DtoMappingCostEstimateEntry.


        :param source_region: The source_region of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: str
        """

        self._source_region = source_region

    @property
    def usage(self):
        """Gets the usage of this DtoMappingCostEstimateEntry.  # noqa: E501


        :return: The usage of this DtoMappingCostEstimateEntry.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this DtoMappingCostEstimateEntry.


        :param usage: The usage of this DtoMappingCostEstimateEntry.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if issubclass(DtoMappingCostEstimateEntry, dict):
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
        if not isinstance(other, DtoMappingCostEstimateEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoMappingCostEstimateEntry):
            return True

        return self.to_dict() != other.to_dict()
