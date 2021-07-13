# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.7-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BillingAccount(object):
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
        'admin_state': 'str',
        'aggregate_state': 'str',
        'billing_state': 'str',
        'billing_type': 'str',
        'created_date': 'datetime',
        'distributor': 'Distributor',
        'id': 'int',
        'max_credit': 'Money',
        'name': 'str',
        'price_list': 'PriceList'
    }

    attribute_map = {
        'admin_state': 'adminState',
        'aggregate_state': 'aggregateState',
        'billing_state': 'billingState',
        'billing_type': 'billingType',
        'created_date': 'createdDate',
        'distributor': 'distributor',
        'id': 'id',
        'max_credit': 'maxCredit',
        'name': 'name',
        'price_list': 'priceList'
    }

    def __init__(self, admin_state=None, aggregate_state=None, billing_state=None, billing_type=None, created_date=None, distributor=None, id=None, max_credit=None, name=None, price_list=None):  # noqa: E501
        """BillingAccount - a model defined in Swagger"""  # noqa: E501

        self._admin_state = None
        self._aggregate_state = None
        self._billing_state = None
        self._billing_type = None
        self._created_date = None
        self._distributor = None
        self._id = None
        self._max_credit = None
        self._name = None
        self._price_list = None
        self.discriminator = None

        if admin_state is not None:
            self.admin_state = admin_state
        if aggregate_state is not None:
            self.aggregate_state = aggregate_state
        if billing_state is not None:
            self.billing_state = billing_state
        if billing_type is not None:
            self.billing_type = billing_type
        if created_date is not None:
            self.created_date = created_date
        if distributor is not None:
            self.distributor = distributor
        if id is not None:
            self.id = id
        if max_credit is not None:
            self.max_credit = max_credit
        if name is not None:
            self.name = name
        if price_list is not None:
            self.price_list = price_list

    @property
    def admin_state(self):
        """Gets the admin_state of this BillingAccount.  # noqa: E501

        System Account state (Updated by Administrator)  # noqa: E501

        :return: The admin_state of this BillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this BillingAccount.

        System Account state (Updated by Administrator)  # noqa: E501

        :param admin_state: The admin_state of this BillingAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "SUSPENDED"]  # noqa: E501
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def aggregate_state(self):
        """Gets the aggregate_state of this BillingAccount.  # noqa: E501

        Aggregated Account state (ACTIVE only if admin state and billing state are ACTIVE)  # noqa: E501

        :return: The aggregate_state of this BillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._aggregate_state

    @aggregate_state.setter
    def aggregate_state(self, aggregate_state):
        """Sets the aggregate_state of this BillingAccount.

        Aggregated Account state (ACTIVE only if admin state and billing state are ACTIVE)  # noqa: E501

        :param aggregate_state: The aggregate_state of this BillingAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "SUSPENDED"]  # noqa: E501
        if aggregate_state not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregate_state` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregate_state, allowed_values)
            )

        self._aggregate_state = aggregate_state

    @property
    def billing_state(self):
        """Gets the billing_state of this BillingAccount.  # noqa: E501

        Billing Account state (Depend on balance and max credit)  # noqa: E501

        :return: The billing_state of this BillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._billing_state

    @billing_state.setter
    def billing_state(self, billing_state):
        """Sets the billing_state of this BillingAccount.

        Billing Account state (Depend on balance and max credit)  # noqa: E501

        :param billing_state: The billing_state of this BillingAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "SUSPENDED"]  # noqa: E501
        if billing_state not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_state` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_state, allowed_values)
            )

        self._billing_state = billing_state

    @property
    def billing_type(self):
        """Gets the billing_type of this BillingAccount.  # noqa: E501

        Type of billing for this account  # noqa: E501

        :return: The billing_type of this BillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this BillingAccount.

        Type of billing for this account  # noqa: E501

        :param billing_type: The billing_type of this BillingAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["BILLING_SERVER", "INTEGRATED"]  # noqa: E501
        if billing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_type` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_type, allowed_values)
            )

        self._billing_type = billing_type

    @property
    def created_date(self):
        """Gets the created_date of this BillingAccount.  # noqa: E501

        Created Timestamp  # noqa: E501

        :return: The created_date of this BillingAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this BillingAccount.

        Created Timestamp  # noqa: E501

        :param created_date: The created_date of this BillingAccount.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def distributor(self):
        """Gets the distributor of this BillingAccount.  # noqa: E501

        Distributor that manages this account  # noqa: E501

        :return: The distributor of this BillingAccount.  # noqa: E501
        :rtype: Distributor
        """
        return self._distributor

    @distributor.setter
    def distributor(self, distributor):
        """Sets the distributor of this BillingAccount.

        Distributor that manages this account  # noqa: E501

        :param distributor: The distributor of this BillingAccount.  # noqa: E501
        :type: Distributor
        """

        self._distributor = distributor

    @property
    def id(self):
        """Gets the id of this BillingAccount.  # noqa: E501

        Account Id  # noqa: E501

        :return: The id of this BillingAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingAccount.

        Account Id  # noqa: E501

        :param id: The id of this BillingAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_credit(self):
        """Gets the max_credit of this BillingAccount.  # noqa: E501

        Account Maximum Credit  # noqa: E501

        :return: The max_credit of this BillingAccount.  # noqa: E501
        :rtype: Money
        """
        return self._max_credit

    @max_credit.setter
    def max_credit(self, max_credit):
        """Sets the max_credit of this BillingAccount.

        Account Maximum Credit  # noqa: E501

        :param max_credit: The max_credit of this BillingAccount.  # noqa: E501
        :type: Money
        """

        self._max_credit = max_credit

    @property
    def name(self):
        """Gets the name of this BillingAccount.  # noqa: E501

        Account Name  # noqa: E501

        :return: The name of this BillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingAccount.

        Account Name  # noqa: E501

        :param name: The name of this BillingAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price_list(self):
        """Gets the price_list of this BillingAccount.  # noqa: E501

        Price list (without prices)  # noqa: E501

        :return: The price_list of this BillingAccount.  # noqa: E501
        :rtype: PriceList
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this BillingAccount.

        Price list (without prices)  # noqa: E501

        :param price_list: The price_list of this BillingAccount.  # noqa: E501
        :type: PriceList
        """

        self._price_list = price_list

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
        if issubclass(BillingAccount, dict):
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
        if not isinstance(other, BillingAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
