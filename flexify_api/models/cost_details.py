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


class CostDetails(object):
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
        'price': 'Price',
        'usage': 'int',
        'username': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'price': 'price',
        'usage': 'usage',
        'username': 'username'
    }

    def __init__(self, cost=None, price=None, usage=None, username=None, _configuration=None):  # noqa: E501
        """CostDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cost = None
        self._price = None
        self._usage = None
        self._username = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if price is not None:
            self.price = price
        if usage is not None:
            self.usage = usage
        if username is not None:
            self.username = username

    @property
    def cost(self):
        """Gets the cost of this CostDetails.  # noqa: E501

        Cost  # noqa: E501

        :return: The cost of this CostDetails.  # noqa: E501
        :rtype: Money
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this CostDetails.

        Cost  # noqa: E501

        :param cost: The cost of this CostDetails.  # noqa: E501
        :type: Money
        """

        self._cost = cost

    @property
    def price(self):
        """Gets the price of this CostDetails.  # noqa: E501

        Price list entry used to calculate this cost  # noqa: E501

        :return: The price of this CostDetails.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CostDetails.

        Price list entry used to calculate this cost  # noqa: E501

        :param price: The price of this CostDetails.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def usage(self):
        """Gets the usage of this CostDetails.  # noqa: E501

        Usage in bytes  # noqa: E501

        :return: The usage of this CostDetails.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this CostDetails.

        Usage in bytes  # noqa: E501

        :param usage: The usage of this CostDetails.  # noqa: E501
        :type: int
        """

        self._usage = usage

    @property
    def username(self):
        """Gets the username of this CostDetails.  # noqa: E501

        Username  # noqa: E501

        :return: The username of this CostDetails.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CostDetails.

        Username  # noqa: E501

        :param username: The username of this CostDetails.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(CostDetails, dict):
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
        if not isinstance(other, CostDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CostDetails):
            return True

        return self.to_dict() != other.to_dict()
