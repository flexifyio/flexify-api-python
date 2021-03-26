# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.2.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SignupResult(object):
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
        'billing_account_id': 'int',
        'external_id': 'str',
        'id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'billing_account_id': 'billingAccountId',
        'external_id': 'externalId',
        'id': 'id',
        'username': 'username'
    }

    def __init__(self, billing_account_id=None, external_id=None, id=None, username=None):  # noqa: E501
        """SignupResult - a model defined in Swagger"""  # noqa: E501

        self._billing_account_id = None
        self._external_id = None
        self._id = None
        self._username = None
        self.discriminator = None

        if billing_account_id is not None:
            self.billing_account_id = billing_account_id
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username

    @property
    def billing_account_id(self):
        """Gets the billing_account_id of this SignupResult.  # noqa: E501


        :return: The billing_account_id of this SignupResult.  # noqa: E501
        :rtype: int
        """
        return self._billing_account_id

    @billing_account_id.setter
    def billing_account_id(self, billing_account_id):
        """Sets the billing_account_id of this SignupResult.


        :param billing_account_id: The billing_account_id of this SignupResult.  # noqa: E501
        :type: int
        """

        self._billing_account_id = billing_account_id

    @property
    def external_id(self):
        """Gets the external_id of this SignupResult.  # noqa: E501


        :return: The external_id of this SignupResult.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SignupResult.


        :param external_id: The external_id of this SignupResult.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this SignupResult.  # noqa: E501


        :return: The id of this SignupResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignupResult.


        :param id: The id of this SignupResult.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this SignupResult.  # noqa: E501


        :return: The username of this SignupResult.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SignupResult.


        :param username: The username of this SignupResult.  # noqa: E501
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
        if issubclass(SignupResult, dict):
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
        if not isinstance(other, SignupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
