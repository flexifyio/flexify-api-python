# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class AddStorageAccountsWithAzureLinkRequest(object):
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
        'list_containers': 'bool',
        'refresh_now': 'bool',
        'settings': 'StorageAccountSettingsReq',
        'storage_account_names': 'list[str]'
    }

    attribute_map = {
        'list_containers': 'listContainers',
        'refresh_now': 'refreshNow',
        'settings': 'settings',
        'storage_account_names': 'storageAccountNames'
    }

    def __init__(self, list_containers=None, refresh_now=None, settings=None, storage_account_names=None, _configuration=None):  # noqa: E501
        """AddStorageAccountsWithAzureLinkRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._list_containers = None
        self._refresh_now = None
        self._settings = None
        self._storage_account_names = None
        self.discriminator = None

        if list_containers is not None:
            self.list_containers = list_containers
        if refresh_now is not None:
            self.refresh_now = refresh_now
        if settings is not None:
            self.settings = settings
        if storage_account_names is not None:
            self.storage_account_names = storage_account_names

    @property
    def list_containers(self):
        """Gets the list_containers of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501

        Specified if containers will be requested for each added storage account  # noqa: E501

        :return: The list_containers of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :rtype: bool
        """
        return self._list_containers

    @list_containers.setter
    def list_containers(self, list_containers):
        """Sets the list_containers of this AddStorageAccountsWithAzureLinkRequest.

        Specified if containers will be requested for each added storage account  # noqa: E501

        :param list_containers: The list_containers of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :type: bool
        """

        self._list_containers = list_containers

    @property
    def refresh_now(self):
        """Gets the refresh_now of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501

        If set to true, buckets will be refreshed after storage is added  # noqa: E501

        :return: The refresh_now of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_now

    @refresh_now.setter
    def refresh_now(self, refresh_now):
        """Sets the refresh_now of this AddStorageAccountsWithAzureLinkRequest.

        If set to true, buckets will be refreshed after storage is added  # noqa: E501

        :param refresh_now: The refresh_now of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :type: bool
        """

        self._refresh_now = refresh_now

    @property
    def settings(self):
        """Gets the settings of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501

        Configuration of the storage accounts  # noqa: E501

        :return: The settings of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :rtype: StorageAccountSettingsReq
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AddStorageAccountsWithAzureLinkRequest.

        Configuration of the storage accounts  # noqa: E501

        :param settings: The settings of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :type: StorageAccountSettingsReq
        """

        self._settings = settings

    @property
    def storage_account_names(self):
        """Gets the storage_account_names of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501

        List of names of storage accounts to add  # noqa: E501

        :return: The storage_account_names of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._storage_account_names

    @storage_account_names.setter
    def storage_account_names(self, storage_account_names):
        """Sets the storage_account_names of this AddStorageAccountsWithAzureLinkRequest.

        List of names of storage accounts to add  # noqa: E501

        :param storage_account_names: The storage_account_names of this AddStorageAccountsWithAzureLinkRequest.  # noqa: E501
        :type: list[str]
        """

        self._storage_account_names = storage_account_names

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
        if issubclass(AddStorageAccountsWithAzureLinkRequest, dict):
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
        if not isinstance(other, AddStorageAccountsWithAzureLinkRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddStorageAccountsWithAzureLinkRequest):
            return True

        return self.to_dict() != other.to_dict()
