# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.12-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StorageAccountsRequest(object):
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
        'new_storage_accounts': 'list[EndpointStorageAccountReq]'
    }

    attribute_map = {
        'new_storage_accounts': 'newStorageAccounts'
    }

    def __init__(self, new_storage_accounts=None):  # noqa: E501
        """StorageAccountsRequest - a model defined in Swagger"""  # noqa: E501

        self._new_storage_accounts = None
        self.discriminator = None

        if new_storage_accounts is not None:
            self.new_storage_accounts = new_storage_accounts

    @property
    def new_storage_accounts(self):
        """Gets the new_storage_accounts of this StorageAccountsRequest.  # noqa: E501

        A list of endpoint storage accounts to set or attach  # noqa: E501

        :return: The new_storage_accounts of this StorageAccountsRequest.  # noqa: E501
        :rtype: list[EndpointStorageAccountReq]
        """
        return self._new_storage_accounts

    @new_storage_accounts.setter
    def new_storage_accounts(self, new_storage_accounts):
        """Sets the new_storage_accounts of this StorageAccountsRequest.

        A list of endpoint storage accounts to set or attach  # noqa: E501

        :param new_storage_accounts: The new_storage_accounts of this StorageAccountsRequest.  # noqa: E501
        :type: list[EndpointStorageAccountReq]
        """

        self._new_storage_accounts = new_storage_accounts

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
        if issubclass(StorageAccountsRequest, dict):
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
        if not isinstance(other, StorageAccountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
