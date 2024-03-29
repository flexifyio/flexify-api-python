# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class StorageAccountStat(object):
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
        'azure_env': 'str',
        'azure_region': 'str',
        'last_refreshed': 'datetime',
        'state': 'str',
        'storages_count': 'int',
        'storages_limit_exceeded': 'bool'
    }

    attribute_map = {
        'azure_env': 'azureEnv',
        'azure_region': 'azureRegion',
        'last_refreshed': 'lastRefreshed',
        'state': 'state',
        'storages_count': 'storagesCount',
        'storages_limit_exceeded': 'storagesLimitExceeded'
    }

    def __init__(self, azure_env=None, azure_region=None, last_refreshed=None, state=None, storages_count=None, storages_limit_exceeded=None, _configuration=None):  # noqa: E501
        """StorageAccountStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._azure_env = None
        self._azure_region = None
        self._last_refreshed = None
        self._state = None
        self._storages_count = None
        self._storages_limit_exceeded = None
        self.discriminator = None

        if azure_env is not None:
            self.azure_env = azure_env
        if azure_region is not None:
            self.azure_region = azure_region
        if last_refreshed is not None:
            self.last_refreshed = last_refreshed
        if state is not None:
            self.state = state
        if storages_count is not None:
            self.storages_count = storages_count
        if storages_limit_exceeded is not None:
            self.storages_limit_exceeded = storages_limit_exceeded

    @property
    def azure_env(self):
        """Gets the azure_env of this StorageAccountStat.  # noqa: E501

        Cloud environment (Gov, Germany, etc.) for Azure storage account  # noqa: E501

        :return: The azure_env of this StorageAccountStat.  # noqa: E501
        :rtype: str
        """
        return self._azure_env

    @azure_env.setter
    def azure_env(self, azure_env):
        """Sets the azure_env of this StorageAccountStat.

        Cloud environment (Gov, Germany, etc.) for Azure storage account  # noqa: E501

        :param azure_env: The azure_env of this StorageAccountStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["AzureGermany", "AzureGovernment", "China", "Private", "Public"]  # noqa: E501
        if (self._configuration.client_side_validation and
                azure_env not in allowed_values):
            raise ValueError(
                "Invalid value for `azure_env` ({0}), must be one of {1}"  # noqa: E501
                .format(azure_env, allowed_values)
            )

        self._azure_env = azure_env

    @property
    def azure_region(self):
        """Gets the azure_region of this StorageAccountStat.  # noqa: E501

        Region for Azure storage account  # noqa: E501

        :return: The azure_region of this StorageAccountStat.  # noqa: E501
        :rtype: str
        """
        return self._azure_region

    @azure_region.setter
    def azure_region(self, azure_region):
        """Sets the azure_region of this StorageAccountStat.

        Region for Azure storage account  # noqa: E501

        :param azure_region: The azure_region of this StorageAccountStat.  # noqa: E501
        :type: str
        """

        self._azure_region = azure_region

    @property
    def last_refreshed(self):
        """Gets the last_refreshed of this StorageAccountStat.  # noqa: E501

        When buckets/containers were requested last time  # noqa: E501

        :return: The last_refreshed of this StorageAccountStat.  # noqa: E501
        :rtype: datetime
        """
        return self._last_refreshed

    @last_refreshed.setter
    def last_refreshed(self, last_refreshed):
        """Sets the last_refreshed of this StorageAccountStat.

        When buckets/containers were requested last time  # noqa: E501

        :param last_refreshed: The last_refreshed of this StorageAccountStat.  # noqa: E501
        :type: datetime
        """

        self._last_refreshed = last_refreshed

    @property
    def state(self):
        """Gets the state of this StorageAccountStat.  # noqa: E501

        State of this storage account  # noqa: E501

        :return: The state of this StorageAccountStat.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StorageAccountStat.

        State of this storage account  # noqa: E501

        :param state: The state of this StorageAccountStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTH_EXPIRED", "ERROR", "NONE", "OK", "REFRESHING", "REFRESH_REQUESTED", "WARNING"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def storages_count(self):
        """Gets the storages_count of this StorageAccountStat.  # noqa: E501

        Number of buckets/containers reported by the storage  # noqa: E501

        :return: The storages_count of this StorageAccountStat.  # noqa: E501
        :rtype: int
        """
        return self._storages_count

    @storages_count.setter
    def storages_count(self, storages_count):
        """Sets the storages_count of this StorageAccountStat.

        Number of buckets/containers reported by the storage  # noqa: E501

        :param storages_count: The storages_count of this StorageAccountStat.  # noqa: E501
        :type: int
        """

        self._storages_count = storages_count

    @property
    def storages_limit_exceeded(self):
        """Gets the storages_limit_exceeded of this StorageAccountStat.  # noqa: E501

        When the limit of the maximum number of buckets/containers is exceed and not all storages are shown  # noqa: E501

        :return: The storages_limit_exceeded of this StorageAccountStat.  # noqa: E501
        :rtype: bool
        """
        return self._storages_limit_exceeded

    @storages_limit_exceeded.setter
    def storages_limit_exceeded(self, storages_limit_exceeded):
        """Sets the storages_limit_exceeded of this StorageAccountStat.

        When the limit of the maximum number of buckets/containers is exceed and not all storages are shown  # noqa: E501

        :param storages_limit_exceeded: The storages_limit_exceeded of this StorageAccountStat.  # noqa: E501
        :type: bool
        """

        self._storages_limit_exceeded = storages_limit_exceeded

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
        if issubclass(StorageAccountStat, dict):
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
        if not isinstance(other, StorageAccountStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageAccountStat):
            return True

        return self.to_dict() != other.to_dict()
