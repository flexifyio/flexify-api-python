# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class AddStorageAccountRequest(object):
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
        'include_buckets': 'list[str]',
        'refresh_now': 'bool',
        'storage_account': 'NewStorageAccount',
        'verify': 'bool'
    }

    attribute_map = {
        'include_buckets': 'includeBuckets',
        'refresh_now': 'refreshNow',
        'storage_account': 'storageAccount',
        'verify': 'verify'
    }

    def __init__(self, include_buckets=None, refresh_now=None, storage_account=None, verify=None, _configuration=None):  # noqa: E501
        """AddStorageAccountRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_buckets = None
        self._refresh_now = None
        self._storage_account = None
        self._verify = None
        self.discriminator = None

        if include_buckets is not None:
            self.include_buckets = include_buckets
        if refresh_now is not None:
            self.refresh_now = refresh_now
        if storage_account is not None:
            self.storage_account = storage_account
        if verify is not None:
            self.verify = verify

    @property
    def include_buckets(self):
        """Gets the include_buckets of this AddStorageAccountRequest.  # noqa: E501

        Lists of buckets to start monitoring, or null to request buckets from the cloud  # noqa: E501

        :return: The include_buckets of this AddStorageAccountRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_buckets

    @include_buckets.setter
    def include_buckets(self, include_buckets):
        """Sets the include_buckets of this AddStorageAccountRequest.

        Lists of buckets to start monitoring, or null to request buckets from the cloud  # noqa: E501

        :param include_buckets: The include_buckets of this AddStorageAccountRequest.  # noqa: E501
        :type: list[str]
        """

        self._include_buckets = include_buckets

    @property
    def refresh_now(self):
        """Gets the refresh_now of this AddStorageAccountRequest.  # noqa: E501

        If set to true, buckets will be refreshed after storage is added  # noqa: E501

        :return: The refresh_now of this AddStorageAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_now

    @refresh_now.setter
    def refresh_now(self, refresh_now):
        """Sets the refresh_now of this AddStorageAccountRequest.

        If set to true, buckets will be refreshed after storage is added  # noqa: E501

        :param refresh_now: The refresh_now of this AddStorageAccountRequest.  # noqa: E501
        :type: bool
        """

        self._refresh_now = refresh_now

    @property
    def storage_account(self):
        """Gets the storage_account of this AddStorageAccountRequest.  # noqa: E501

        Storage account to create  # noqa: E501

        :return: The storage_account of this AddStorageAccountRequest.  # noqa: E501
        :rtype: NewStorageAccount
        """
        return self._storage_account

    @storage_account.setter
    def storage_account(self, storage_account):
        """Sets the storage_account of this AddStorageAccountRequest.

        Storage account to create  # noqa: E501

        :param storage_account: The storage_account of this AddStorageAccountRequest.  # noqa: E501
        :type: NewStorageAccount
        """

        self._storage_account = storage_account

    @property
    def verify(self):
        """Gets the verify of this AddStorageAccountRequest.  # noqa: E501

        Specified if credentials or public access to included buckets should be checked  # noqa: E501

        :return: The verify of this AddStorageAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._verify

    @verify.setter
    def verify(self, verify):
        """Sets the verify of this AddStorageAccountRequest.

        Specified if credentials or public access to included buckets should be checked  # noqa: E501

        :param verify: The verify of this AddStorageAccountRequest.  # noqa: E501
        :type: bool
        """

        self._verify = verify

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
        if issubclass(AddStorageAccountRequest, dict):
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
        if not isinstance(other, AddStorageAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddStorageAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
