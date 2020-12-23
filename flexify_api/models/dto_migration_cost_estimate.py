# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DtoMigrationCostEstimate(object):
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
        'mappings': 'list[DtoMappingCostEstimate]',
        'total_cost': 'Money',
        'total_usage': 'int'
    }

    attribute_map = {
        'mappings': 'mappings',
        'total_cost': 'totalCost',
        'total_usage': 'totalUsage'
    }

    def __init__(self, mappings=None, total_cost=None, total_usage=None):  # noqa: E501
        """DtoMigrationCostEstimate - a model defined in Swagger"""  # noqa: E501

        self._mappings = None
        self._total_cost = None
        self._total_usage = None
        self.discriminator = None

        if mappings is not None:
            self.mappings = mappings
        if total_cost is not None:
            self.total_cost = total_cost
        if total_usage is not None:
            self.total_usage = total_usage

    @property
    def mappings(self):
        """Gets the mappings of this DtoMigrationCostEstimate.  # noqa: E501


        :return: The mappings of this DtoMigrationCostEstimate.  # noqa: E501
        :rtype: list[DtoMappingCostEstimate]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this DtoMigrationCostEstimate.


        :param mappings: The mappings of this DtoMigrationCostEstimate.  # noqa: E501
        :type: list[DtoMappingCostEstimate]
        """

        self._mappings = mappings

    @property
    def total_cost(self):
        """Gets the total_cost of this DtoMigrationCostEstimate.  # noqa: E501


        :return: The total_cost of this DtoMigrationCostEstimate.  # noqa: E501
        :rtype: Money
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this DtoMigrationCostEstimate.


        :param total_cost: The total_cost of this DtoMigrationCostEstimate.  # noqa: E501
        :type: Money
        """

        self._total_cost = total_cost

    @property
    def total_usage(self):
        """Gets the total_usage of this DtoMigrationCostEstimate.  # noqa: E501


        :return: The total_usage of this DtoMigrationCostEstimate.  # noqa: E501
        :rtype: int
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this DtoMigrationCostEstimate.


        :param total_usage: The total_usage of this DtoMigrationCostEstimate.  # noqa: E501
        :type: int
        """

        self._total_usage = total_usage

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
        if issubclass(DtoMigrationCostEstimate, dict):
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
        if not isinstance(other, DtoMigrationCostEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
