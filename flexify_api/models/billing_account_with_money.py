# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BillingAccountWithMoney(object):
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
        'balance': 'Money',
        'billing_state': 'str',
        'created_date': 'datetime',
        'credit_exceeded': 'bool',
        'distributor': 'Distributor',
        'id': 'int',
        'max_credit': 'Money',
        'name': 'str',
        'price_list': 'PriceList',
        'total_cost': 'Money',
        'total_paid': 'Money'
    }

    attribute_map = {
        'admin_state': 'adminState',
        'aggregate_state': 'aggregateState',
        'balance': 'balance',
        'billing_state': 'billingState',
        'created_date': 'createdDate',
        'credit_exceeded': 'creditExceeded',
        'distributor': 'distributor',
        'id': 'id',
        'max_credit': 'maxCredit',
        'name': 'name',
        'price_list': 'priceList',
        'total_cost': 'totalCost',
        'total_paid': 'totalPaid'
    }

    def __init__(self, admin_state=None, aggregate_state=None, balance=None, billing_state=None, created_date=None, credit_exceeded=None, distributor=None, id=None, max_credit=None, name=None, price_list=None, total_cost=None, total_paid=None):  # noqa: E501
        """BillingAccountWithMoney - a model defined in Swagger"""  # noqa: E501

        self._admin_state = None
        self._aggregate_state = None
        self._balance = None
        self._billing_state = None
        self._created_date = None
        self._credit_exceeded = None
        self._distributor = None
        self._id = None
        self._max_credit = None
        self._name = None
        self._price_list = None
        self._total_cost = None
        self._total_paid = None
        self.discriminator = None

        if admin_state is not None:
            self.admin_state = admin_state
        if aggregate_state is not None:
            self.aggregate_state = aggregate_state
        if balance is not None:
            self.balance = balance
        if billing_state is not None:
            self.billing_state = billing_state
        if created_date is not None:
            self.created_date = created_date
        if credit_exceeded is not None:
            self.credit_exceeded = credit_exceeded
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
        if total_cost is not None:
            self.total_cost = total_cost
        if total_paid is not None:
            self.total_paid = total_paid

    @property
    def admin_state(self):
        """Gets the admin_state of this BillingAccountWithMoney.  # noqa: E501

        System Account state (Updated by Administrator)  # noqa: E501

        :return: The admin_state of this BillingAccountWithMoney.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this BillingAccountWithMoney.

        System Account state (Updated by Administrator)  # noqa: E501

        :param admin_state: The admin_state of this BillingAccountWithMoney.  # noqa: E501
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
        """Gets the aggregate_state of this BillingAccountWithMoney.  # noqa: E501

        Aggregated Account state (ACTIVE only if admin state and billing state are ACTIVE)  # noqa: E501

        :return: The aggregate_state of this BillingAccountWithMoney.  # noqa: E501
        :rtype: str
        """
        return self._aggregate_state

    @aggregate_state.setter
    def aggregate_state(self, aggregate_state):
        """Sets the aggregate_state of this BillingAccountWithMoney.

        Aggregated Account state (ACTIVE only if admin state and billing state are ACTIVE)  # noqa: E501

        :param aggregate_state: The aggregate_state of this BillingAccountWithMoney.  # noqa: E501
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
    def balance(self):
        """Gets the balance of this BillingAccountWithMoney.  # noqa: E501

        Account Current Balance  # noqa: E501

        :return: The balance of this BillingAccountWithMoney.  # noqa: E501
        :rtype: Money
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this BillingAccountWithMoney.

        Account Current Balance  # noqa: E501

        :param balance: The balance of this BillingAccountWithMoney.  # noqa: E501
        :type: Money
        """

        self._balance = balance

    @property
    def billing_state(self):
        """Gets the billing_state of this BillingAccountWithMoney.  # noqa: E501

        Billing Account state (Depend on balance and max credit)  # noqa: E501

        :return: The billing_state of this BillingAccountWithMoney.  # noqa: E501
        :rtype: str
        """
        return self._billing_state

    @billing_state.setter
    def billing_state(self, billing_state):
        """Sets the billing_state of this BillingAccountWithMoney.

        Billing Account state (Depend on balance and max credit)  # noqa: E501

        :param billing_state: The billing_state of this BillingAccountWithMoney.  # noqa: E501
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
    def created_date(self):
        """Gets the created_date of this BillingAccountWithMoney.  # noqa: E501

        Created Timestamp  # noqa: E501

        :return: The created_date of this BillingAccountWithMoney.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this BillingAccountWithMoney.

        Created Timestamp  # noqa: E501

        :param created_date: The created_date of this BillingAccountWithMoney.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def credit_exceeded(self):
        """Gets the credit_exceeded of this BillingAccountWithMoney.  # noqa: E501

        Is credit exceeded  # noqa: E501

        :return: The credit_exceeded of this BillingAccountWithMoney.  # noqa: E501
        :rtype: bool
        """
        return self._credit_exceeded

    @credit_exceeded.setter
    def credit_exceeded(self, credit_exceeded):
        """Sets the credit_exceeded of this BillingAccountWithMoney.

        Is credit exceeded  # noqa: E501

        :param credit_exceeded: The credit_exceeded of this BillingAccountWithMoney.  # noqa: E501
        :type: bool
        """

        self._credit_exceeded = credit_exceeded

    @property
    def distributor(self):
        """Gets the distributor of this BillingAccountWithMoney.  # noqa: E501

        Distributor that manages this account  # noqa: E501

        :return: The distributor of this BillingAccountWithMoney.  # noqa: E501
        :rtype: Distributor
        """
        return self._distributor

    @distributor.setter
    def distributor(self, distributor):
        """Sets the distributor of this BillingAccountWithMoney.

        Distributor that manages this account  # noqa: E501

        :param distributor: The distributor of this BillingAccountWithMoney.  # noqa: E501
        :type: Distributor
        """

        self._distributor = distributor

    @property
    def id(self):
        """Gets the id of this BillingAccountWithMoney.  # noqa: E501

        Account Id  # noqa: E501

        :return: The id of this BillingAccountWithMoney.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingAccountWithMoney.

        Account Id  # noqa: E501

        :param id: The id of this BillingAccountWithMoney.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_credit(self):
        """Gets the max_credit of this BillingAccountWithMoney.  # noqa: E501

        Account Maximum Credit  # noqa: E501

        :return: The max_credit of this BillingAccountWithMoney.  # noqa: E501
        :rtype: Money
        """
        return self._max_credit

    @max_credit.setter
    def max_credit(self, max_credit):
        """Sets the max_credit of this BillingAccountWithMoney.

        Account Maximum Credit  # noqa: E501

        :param max_credit: The max_credit of this BillingAccountWithMoney.  # noqa: E501
        :type: Money
        """

        self._max_credit = max_credit

    @property
    def name(self):
        """Gets the name of this BillingAccountWithMoney.  # noqa: E501

        Account Name  # noqa: E501

        :return: The name of this BillingAccountWithMoney.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingAccountWithMoney.

        Account Name  # noqa: E501

        :param name: The name of this BillingAccountWithMoney.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price_list(self):
        """Gets the price_list of this BillingAccountWithMoney.  # noqa: E501

        Price list (without prices)  # noqa: E501

        :return: The price_list of this BillingAccountWithMoney.  # noqa: E501
        :rtype: PriceList
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this BillingAccountWithMoney.

        Price list (without prices)  # noqa: E501

        :param price_list: The price_list of this BillingAccountWithMoney.  # noqa: E501
        :type: PriceList
        """

        self._price_list = price_list

    @property
    def total_cost(self):
        """Gets the total_cost of this BillingAccountWithMoney.  # noqa: E501

        Account Total Cost  # noqa: E501

        :return: The total_cost of this BillingAccountWithMoney.  # noqa: E501
        :rtype: Money
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this BillingAccountWithMoney.

        Account Total Cost  # noqa: E501

        :param total_cost: The total_cost of this BillingAccountWithMoney.  # noqa: E501
        :type: Money
        """

        self._total_cost = total_cost

    @property
    def total_paid(self):
        """Gets the total_paid of this BillingAccountWithMoney.  # noqa: E501

        Account Total Paid  # noqa: E501

        :return: The total_paid of this BillingAccountWithMoney.  # noqa: E501
        :rtype: Money
        """
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        """Sets the total_paid of this BillingAccountWithMoney.

        Account Total Paid  # noqa: E501

        :param total_paid: The total_paid of this BillingAccountWithMoney.  # noqa: E501
        :type: Money
        """

        self._total_paid = total_paid

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
        if issubclass(BillingAccountWithMoney, dict):
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
        if not isinstance(other, BillingAccountWithMoney):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
