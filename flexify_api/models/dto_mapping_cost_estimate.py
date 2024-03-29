# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class DtoMappingCostEstimate(object):
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
        'costs': 'list[DtoMappingCostEstimateEntry]',
        'mapping': 'AddMigrationRequestMapping',
        'total_cost': 'Money',
        'total_usage': 'int'
    }

    attribute_map = {
        'costs': 'costs',
        'mapping': 'mapping',
        'total_cost': 'totalCost',
        'total_usage': 'totalUsage'
    }

    def __init__(self, costs=None, mapping=None, total_cost=None, total_usage=None, _configuration=None):  # noqa: E501
        """DtoMappingCostEstimate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._costs = None
        self._mapping = None
        self._total_cost = None
        self._total_usage = None
        self.discriminator = None

        if costs is not None:
            self.costs = costs
        if mapping is not None:
            self.mapping = mapping
        if total_cost is not None:
            self.total_cost = total_cost
        if total_usage is not None:
            self.total_usage = total_usage

    @property
    def costs(self):
        """Gets the costs of this DtoMappingCostEstimate.  # noqa: E501


        :return: The costs of this DtoMappingCostEstimate.  # noqa: E501
        :rtype: list[DtoMappingCostEstimateEntry]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this DtoMappingCostEstimate.


        :param costs: The costs of this DtoMappingCostEstimate.  # noqa: E501
        :type: list[DtoMappingCostEstimateEntry]
        """

        self._costs = costs

    @property
    def mapping(self):
        """Gets the mapping of this DtoMappingCostEstimate.  # noqa: E501


        :return: The mapping of this DtoMappingCostEstimate.  # noqa: E501
        :rtype: AddMigrationRequestMapping
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this DtoMappingCostEstimate.


        :param mapping: The mapping of this DtoMappingCostEstimate.  # noqa: E501
        :type: AddMigrationRequestMapping
        """

        self._mapping = mapping

    @property
    def total_cost(self):
        """Gets the total_cost of this DtoMappingCostEstimate.  # noqa: E501


        :return: The total_cost of this DtoMappingCostEstimate.  # noqa: E501
        :rtype: Money
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this DtoMappingCostEstimate.


        :param total_cost: The total_cost of this DtoMappingCostEstimate.  # noqa: E501
        :type: Money
        """

        self._total_cost = total_cost

    @property
    def total_usage(self):
        """Gets the total_usage of this DtoMappingCostEstimate.  # noqa: E501


        :return: The total_usage of this DtoMappingCostEstimate.  # noqa: E501
        :rtype: int
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this DtoMappingCostEstimate.


        :param total_usage: The total_usage of this DtoMappingCostEstimate.  # noqa: E501
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
        if issubclass(DtoMappingCostEstimate, dict):
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
        if not isinstance(other, DtoMappingCostEstimate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DtoMappingCostEstimate):
            return True

        return self.to_dict() != other.to_dict()
