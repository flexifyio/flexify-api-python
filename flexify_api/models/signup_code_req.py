# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.4-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SignupCodeReq(object):
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
        'code': 'str',
        'org_id': 'int',
        'price_list_id': 'int',
        'roles': 'list[str]',
        'single_use': 'bool',
        'use_my_billing_account': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'org_id': 'orgId',
        'price_list_id': 'priceListId',
        'roles': 'roles',
        'single_use': 'singleUse',
        'use_my_billing_account': 'useMyBillingAccount'
    }

    def __init__(self, code=None, org_id=None, price_list_id=None, roles=None, single_use=None, use_my_billing_account=None):  # noqa: E501
        """SignupCodeReq - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._org_id = None
        self._price_list_id = None
        self._roles = None
        self._single_use = None
        self._use_my_billing_account = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if org_id is not None:
            self.org_id = org_id
        if price_list_id is not None:
            self.price_list_id = price_list_id
        if roles is not None:
            self.roles = roles
        if single_use is not None:
            self.single_use = single_use
        if use_my_billing_account is not None:
            self.use_my_billing_account = use_my_billing_account

    @property
    def code(self):
        """Gets the code of this SignupCodeReq.  # noqa: E501


        :return: The code of this SignupCodeReq.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SignupCodeReq.


        :param code: The code of this SignupCodeReq.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def org_id(self):
        """Gets the org_id of this SignupCodeReq.  # noqa: E501


        :return: The org_id of this SignupCodeReq.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this SignupCodeReq.


        :param org_id: The org_id of this SignupCodeReq.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def price_list_id(self):
        """Gets the price_list_id of this SignupCodeReq.  # noqa: E501


        :return: The price_list_id of this SignupCodeReq.  # noqa: E501
        :rtype: int
        """
        return self._price_list_id

    @price_list_id.setter
    def price_list_id(self, price_list_id):
        """Sets the price_list_id of this SignupCodeReq.


        :param price_list_id: The price_list_id of this SignupCodeReq.  # noqa: E501
        :type: int
        """

        self._price_list_id = price_list_id

    @property
    def roles(self):
        """Gets the roles of this SignupCodeReq.  # noqa: E501


        :return: The roles of this SignupCodeReq.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this SignupCodeReq.


        :param roles: The roles of this SignupCodeReq.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ROLE_ACTUATOR", "ROLE_ADMIN", "ROLE_BILLING", "ROLE_DISTRIBUTOR", "ROLE_IMPERSONATOR", "ROLE_PARTNER_ADMIN", "ROLE_USER"]  # noqa: E501
        if not set(roles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

    @property
    def single_use(self):
        """Gets the single_use of this SignupCodeReq.  # noqa: E501


        :return: The single_use of this SignupCodeReq.  # noqa: E501
        :rtype: bool
        """
        return self._single_use

    @single_use.setter
    def single_use(self, single_use):
        """Sets the single_use of this SignupCodeReq.


        :param single_use: The single_use of this SignupCodeReq.  # noqa: E501
        :type: bool
        """

        self._single_use = single_use

    @property
    def use_my_billing_account(self):
        """Gets the use_my_billing_account of this SignupCodeReq.  # noqa: E501


        :return: The use_my_billing_account of this SignupCodeReq.  # noqa: E501
        :rtype: bool
        """
        return self._use_my_billing_account

    @use_my_billing_account.setter
    def use_my_billing_account(self, use_my_billing_account):
        """Sets the use_my_billing_account of this SignupCodeReq.


        :param use_my_billing_account: The use_my_billing_account of this SignupCodeReq.  # noqa: E501
        :type: bool
        """

        self._use_my_billing_account = use_my_billing_account

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
        if issubclass(SignupCodeReq, dict):
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
        if not isinstance(other, SignupCodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
