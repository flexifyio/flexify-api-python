# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.5-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserStat(object):
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
        'active_migrations_count': 'int',
        'billing_account_admin_state': 'str',
        'billing_account_name': 'str',
        'billing_account_state': 'str',
        'company': 'str',
        'delete_requested': 'datetime',
        'display_name': 'str',
        'distributor_name': 'str',
        'email': 'str',
        'id': 'int',
        'org_name': 'str',
        'price_list_name': 'str',
        'registered': 'datetime',
        'storage_accounts_count': 'int',
        'total_migrations_count': 'int',
        'user_state': 'str'
    }

    attribute_map = {
        'active_migrations_count': 'activeMigrationsCount',
        'billing_account_admin_state': 'billingAccountAdminState',
        'billing_account_name': 'billingAccountName',
        'billing_account_state': 'billingAccountState',
        'company': 'company',
        'delete_requested': 'deleteRequested',
        'display_name': 'displayName',
        'distributor_name': 'distributorName',
        'email': 'email',
        'id': 'id',
        'org_name': 'orgName',
        'price_list_name': 'priceListName',
        'registered': 'registered',
        'storage_accounts_count': 'storageAccountsCount',
        'total_migrations_count': 'totalMigrationsCount',
        'user_state': 'userState'
    }

    def __init__(self, active_migrations_count=None, billing_account_admin_state=None, billing_account_name=None, billing_account_state=None, company=None, delete_requested=None, display_name=None, distributor_name=None, email=None, id=None, org_name=None, price_list_name=None, registered=None, storage_accounts_count=None, total_migrations_count=None, user_state=None):  # noqa: E501
        """UserStat - a model defined in Swagger"""  # noqa: E501

        self._active_migrations_count = None
        self._billing_account_admin_state = None
        self._billing_account_name = None
        self._billing_account_state = None
        self._company = None
        self._delete_requested = None
        self._display_name = None
        self._distributor_name = None
        self._email = None
        self._id = None
        self._org_name = None
        self._price_list_name = None
        self._registered = None
        self._storage_accounts_count = None
        self._total_migrations_count = None
        self._user_state = None
        self.discriminator = None

        if active_migrations_count is not None:
            self.active_migrations_count = active_migrations_count
        if billing_account_admin_state is not None:
            self.billing_account_admin_state = billing_account_admin_state
        if billing_account_name is not None:
            self.billing_account_name = billing_account_name
        if billing_account_state is not None:
            self.billing_account_state = billing_account_state
        if company is not None:
            self.company = company
        if delete_requested is not None:
            self.delete_requested = delete_requested
        if display_name is not None:
            self.display_name = display_name
        if distributor_name is not None:
            self.distributor_name = distributor_name
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if org_name is not None:
            self.org_name = org_name
        if price_list_name is not None:
            self.price_list_name = price_list_name
        if registered is not None:
            self.registered = registered
        if storage_accounts_count is not None:
            self.storage_accounts_count = storage_accounts_count
        if total_migrations_count is not None:
            self.total_migrations_count = total_migrations_count
        if user_state is not None:
            self.user_state = user_state

    @property
    def active_migrations_count(self):
        """Gets the active_migrations_count of this UserStat.  # noqa: E501


        :return: The active_migrations_count of this UserStat.  # noqa: E501
        :rtype: int
        """
        return self._active_migrations_count

    @active_migrations_count.setter
    def active_migrations_count(self, active_migrations_count):
        """Sets the active_migrations_count of this UserStat.


        :param active_migrations_count: The active_migrations_count of this UserStat.  # noqa: E501
        :type: int
        """

        self._active_migrations_count = active_migrations_count

    @property
    def billing_account_admin_state(self):
        """Gets the billing_account_admin_state of this UserStat.  # noqa: E501


        :return: The billing_account_admin_state of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_admin_state

    @billing_account_admin_state.setter
    def billing_account_admin_state(self, billing_account_admin_state):
        """Sets the billing_account_admin_state of this UserStat.


        :param billing_account_admin_state: The billing_account_admin_state of this UserStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "SUSPENDED"]  # noqa: E501
        if billing_account_admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_account_admin_state` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_account_admin_state, allowed_values)
            )

        self._billing_account_admin_state = billing_account_admin_state

    @property
    def billing_account_name(self):
        """Gets the billing_account_name of this UserStat.  # noqa: E501


        :return: The billing_account_name of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_name

    @billing_account_name.setter
    def billing_account_name(self, billing_account_name):
        """Sets the billing_account_name of this UserStat.


        :param billing_account_name: The billing_account_name of this UserStat.  # noqa: E501
        :type: str
        """

        self._billing_account_name = billing_account_name

    @property
    def billing_account_state(self):
        """Gets the billing_account_state of this UserStat.  # noqa: E501


        :return: The billing_account_state of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_state

    @billing_account_state.setter
    def billing_account_state(self, billing_account_state):
        """Sets the billing_account_state of this UserStat.


        :param billing_account_state: The billing_account_state of this UserStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "SUSPENDED"]  # noqa: E501
        if billing_account_state not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_account_state` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_account_state, allowed_values)
            )

        self._billing_account_state = billing_account_state

    @property
    def company(self):
        """Gets the company of this UserStat.  # noqa: E501


        :return: The company of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UserStat.


        :param company: The company of this UserStat.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def delete_requested(self):
        """Gets the delete_requested of this UserStat.  # noqa: E501


        :return: The delete_requested of this UserStat.  # noqa: E501
        :rtype: datetime
        """
        return self._delete_requested

    @delete_requested.setter
    def delete_requested(self, delete_requested):
        """Sets the delete_requested of this UserStat.


        :param delete_requested: The delete_requested of this UserStat.  # noqa: E501
        :type: datetime
        """

        self._delete_requested = delete_requested

    @property
    def display_name(self):
        """Gets the display_name of this UserStat.  # noqa: E501


        :return: The display_name of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserStat.


        :param display_name: The display_name of this UserStat.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def distributor_name(self):
        """Gets the distributor_name of this UserStat.  # noqa: E501


        :return: The distributor_name of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._distributor_name

    @distributor_name.setter
    def distributor_name(self, distributor_name):
        """Sets the distributor_name of this UserStat.


        :param distributor_name: The distributor_name of this UserStat.  # noqa: E501
        :type: str
        """

        self._distributor_name = distributor_name

    @property
    def email(self):
        """Gets the email of this UserStat.  # noqa: E501


        :return: The email of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserStat.


        :param email: The email of this UserStat.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this UserStat.  # noqa: E501


        :return: The id of this UserStat.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserStat.


        :param id: The id of this UserStat.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def org_name(self):
        """Gets the org_name of this UserStat.  # noqa: E501


        :return: The org_name of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this UserStat.


        :param org_name: The org_name of this UserStat.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def price_list_name(self):
        """Gets the price_list_name of this UserStat.  # noqa: E501


        :return: The price_list_name of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._price_list_name

    @price_list_name.setter
    def price_list_name(self, price_list_name):
        """Sets the price_list_name of this UserStat.


        :param price_list_name: The price_list_name of this UserStat.  # noqa: E501
        :type: str
        """

        self._price_list_name = price_list_name

    @property
    def registered(self):
        """Gets the registered of this UserStat.  # noqa: E501


        :return: The registered of this UserStat.  # noqa: E501
        :rtype: datetime
        """
        return self._registered

    @registered.setter
    def registered(self, registered):
        """Sets the registered of this UserStat.


        :param registered: The registered of this UserStat.  # noqa: E501
        :type: datetime
        """

        self._registered = registered

    @property
    def storage_accounts_count(self):
        """Gets the storage_accounts_count of this UserStat.  # noqa: E501


        :return: The storage_accounts_count of this UserStat.  # noqa: E501
        :rtype: int
        """
        return self._storage_accounts_count

    @storage_accounts_count.setter
    def storage_accounts_count(self, storage_accounts_count):
        """Sets the storage_accounts_count of this UserStat.


        :param storage_accounts_count: The storage_accounts_count of this UserStat.  # noqa: E501
        :type: int
        """

        self._storage_accounts_count = storage_accounts_count

    @property
    def total_migrations_count(self):
        """Gets the total_migrations_count of this UserStat.  # noqa: E501


        :return: The total_migrations_count of this UserStat.  # noqa: E501
        :rtype: int
        """
        return self._total_migrations_count

    @total_migrations_count.setter
    def total_migrations_count(self, total_migrations_count):
        """Sets the total_migrations_count of this UserStat.


        :param total_migrations_count: The total_migrations_count of this UserStat.  # noqa: E501
        :type: int
        """

        self._total_migrations_count = total_migrations_count

    @property
    def user_state(self):
        """Gets the user_state of this UserStat.  # noqa: E501


        :return: The user_state of this UserStat.  # noqa: E501
        :rtype: str
        """
        return self._user_state

    @user_state.setter
    def user_state(self, user_state):
        """Sets the user_state of this UserStat.


        :param user_state: The user_state of this UserStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "DISABLED"]  # noqa: E501
        if user_state not in allowed_values:
            raise ValueError(
                "Invalid value for `user_state` ({0}), must be one of {1}"  # noqa: E501
                .format(user_state, allowed_values)
            )

        self._user_state = user_state

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
        if issubclass(UserStat, dict):
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
        if not isinstance(other, UserStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
