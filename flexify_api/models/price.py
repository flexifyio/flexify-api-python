# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1.h1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Price(object):
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
        'constraints': 'PriceConstraints',
        'counter': 'str',
        'id': 'int',
        'price': 'Money',
        'service': 'str',
        'unit_name': 'str',
        'unit_size': 'int'
    }

    attribute_map = {
        'constraints': 'constraints',
        'counter': 'counter',
        'id': 'id',
        'price': 'price',
        'service': 'service',
        'unit_name': 'unitName',
        'unit_size': 'unitSize'
    }

    def __init__(self, constraints=None, counter=None, id=None, price=None, service=None, unit_name=None, unit_size=None):  # noqa: E501
        """Price - a model defined in Swagger"""  # noqa: E501

        self._constraints = None
        self._counter = None
        self._id = None
        self._price = None
        self._service = None
        self._unit_name = None
        self._unit_size = None
        self.discriminator = None

        if constraints is not None:
            self.constraints = constraints
        if counter is not None:
            self.counter = counter
        if id is not None:
            self.id = id
        if price is not None:
            self.price = price
        if service is not None:
            self.service = service
        if unit_name is not None:
            self.unit_name = unit_name
        if unit_size is not None:
            self.unit_size = unit_size

    @property
    def constraints(self):
        """Gets the constraints of this Price.  # noqa: E501

        Constraints that this price works for  # noqa: E501

        :return: The constraints of this Price.  # noqa: E501
        :rtype: PriceConstraints
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this Price.

        Constraints that this price works for  # noqa: E501

        :param constraints: The constraints of this Price.  # noqa: E501
        :type: PriceConstraints
        """

        self._constraints = constraints

    @property
    def counter(self):
        """Gets the counter of this Price.  # noqa: E501

        Billable counter (such as traffic or storage volume)  # noqa: E501

        :return: The counter of this Price.  # noqa: E501
        :rtype: str
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this Price.

        Billable counter (such as traffic or storage volume)  # noqa: E501

        :param counter: The counter of this Price.  # noqa: E501
        :type: str
        """
        allowed_values = ["STORAGE_VOLUME", "TRAFFIC"]  # noqa: E501
        if counter not in allowed_values:
            raise ValueError(
                "Invalid value for `counter` ({0}), must be one of {1}"  # noqa: E501
                .format(counter, allowed_values)
            )

        self._counter = counter

    @property
    def id(self):
        """Gets the id of this Price.  # noqa: E501

        Unique ID of this price  # noqa: E501

        :return: The id of this Price.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Price.

        Unique ID of this price  # noqa: E501

        :param id: The id of this Price.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def price(self):
        """Gets the price of this Price.  # noqa: E501

        Price of one unit  # noqa: E501

        :return: The price of this Price.  # noqa: E501
        :rtype: Money
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Price.

        Price of one unit  # noqa: E501

        :param price: The price of this Price.  # noqa: E501
        :type: Money
        """

        self._price = price

    @property
    def service(self):
        """Gets the service of this Price.  # noqa: E501

        Service  # noqa: E501

        :return: The service of this Price.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Price.

        Service  # noqa: E501

        :param service: The service of this Price.  # noqa: E501
        :type: str
        """
        allowed_values = ["DATA_FORWARDING", "DATA_MIGRATION"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def unit_name(self):
        """Gets the unit_name of this Price.  # noqa: E501

        Name of billable unit  # noqa: E501

        :return: The unit_name of this Price.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this Price.

        Name of billable unit  # noqa: E501

        :param unit_name: The unit_name of this Price.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

    @property
    def unit_size(self):
        """Gets the unit_size of this Price.  # noqa: E501

        Size of billable unit in bytes  # noqa: E501

        :return: The unit_size of this Price.  # noqa: E501
        :rtype: int
        """
        return self._unit_size

    @unit_size.setter
    def unit_size(self, unit_size):
        """Sets the unit_size of this Price.

        Size of billable unit in bytes  # noqa: E501

        :param unit_size: The unit_size of this Price.  # noqa: E501
        :type: int
        """

        self._unit_size = unit_size

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
        if issubclass(Price, dict):
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
        if not isinstance(other, Price):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
