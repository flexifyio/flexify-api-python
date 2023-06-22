# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.18-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class SignupCodeStat(object):
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
        'available': 'bool',
        'billing_account': 'BillingAccount',
        'created': 'datetime',
        'org': 'Organization',
        'price_list': 'PriceList',
        'used_by': 'list[str]'
    }

    attribute_map = {
        'available': 'available',
        'billing_account': 'billingAccount',
        'created': 'created',
        'org': 'org',
        'price_list': 'priceList',
        'used_by': 'usedBy'
    }

    def __init__(self, available=None, billing_account=None, created=None, org=None, price_list=None, used_by=None, _configuration=None):  # noqa: E501
        """SignupCodeStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._available = None
        self._billing_account = None
        self._created = None
        self._org = None
        self._price_list = None
        self._used_by = None
        self.discriminator = None

        if available is not None:
            self.available = available
        if billing_account is not None:
            self.billing_account = billing_account
        if created is not None:
            self.created = created
        if org is not None:
            self.org = org
        if price_list is not None:
            self.price_list = price_list
        if used_by is not None:
            self.used_by = used_by

    @property
    def available(self):
        """Gets the available of this SignupCodeStat.  # noqa: E501


        :return: The available of this SignupCodeStat.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this SignupCodeStat.


        :param available: The available of this SignupCodeStat.  # noqa: E501
        :type: bool
        """

        self._available = available

    @property
    def billing_account(self):
        """Gets the billing_account of this SignupCodeStat.  # noqa: E501


        :return: The billing_account of this SignupCodeStat.  # noqa: E501
        :rtype: BillingAccount
        """
        return self._billing_account

    @billing_account.setter
    def billing_account(self, billing_account):
        """Sets the billing_account of this SignupCodeStat.


        :param billing_account: The billing_account of this SignupCodeStat.  # noqa: E501
        :type: BillingAccount
        """

        self._billing_account = billing_account

    @property
    def created(self):
        """Gets the created of this SignupCodeStat.  # noqa: E501


        :return: The created of this SignupCodeStat.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SignupCodeStat.


        :param created: The created of this SignupCodeStat.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def org(self):
        """Gets the org of this SignupCodeStat.  # noqa: E501


        :return: The org of this SignupCodeStat.  # noqa: E501
        :rtype: Organization
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this SignupCodeStat.


        :param org: The org of this SignupCodeStat.  # noqa: E501
        :type: Organization
        """

        self._org = org

    @property
    def price_list(self):
        """Gets the price_list of this SignupCodeStat.  # noqa: E501


        :return: The price_list of this SignupCodeStat.  # noqa: E501
        :rtype: PriceList
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this SignupCodeStat.


        :param price_list: The price_list of this SignupCodeStat.  # noqa: E501
        :type: PriceList
        """

        self._price_list = price_list

    @property
    def used_by(self):
        """Gets the used_by of this SignupCodeStat.  # noqa: E501


        :return: The used_by of this SignupCodeStat.  # noqa: E501
        :rtype: list[str]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this SignupCodeStat.


        :param used_by: The used_by of this SignupCodeStat.  # noqa: E501
        :type: list[str]
        """

        self._used_by = used_by

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
        if issubclass(SignupCodeStat, dict):
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
        if not isinstance(other, SignupCodeStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignupCodeStat):
            return True

        return self.to_dict() != other.to_dict()
