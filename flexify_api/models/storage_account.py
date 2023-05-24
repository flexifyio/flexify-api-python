# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.16
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class StorageAccount(object):
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
        'id': 'int',
        'is_sas': 'bool',
        'private_url': 'str',
        'provider': 'StorageProvider',
        'settings': 'StorageAccountSettingsRes',
        'stat': 'StorageAccountStat',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_sas': 'isSas',
        'private_url': 'privateUrl',
        'provider': 'provider',
        'settings': 'settings',
        'stat': 'stat',
        'url': 'url'
    }

    def __init__(self, id=None, is_sas=None, private_url=None, provider=None, settings=None, stat=None, url=None, _configuration=None):  # noqa: E501
        """StorageAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._is_sas = None
        self._private_url = None
        self._provider = None
        self._settings = None
        self._stat = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_sas is not None:
            self.is_sas = is_sas
        if private_url is not None:
            self.private_url = private_url
        if provider is not None:
            self.provider = provider
        if settings is not None:
            self.settings = settings
        if stat is not None:
            self.stat = stat
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this StorageAccount.  # noqa: E501

        Id of the storage account  # noqa: E501

        :return: The id of this StorageAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageAccount.

        Id of the storage account  # noqa: E501

        :param id: The id of this StorageAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_sas(self):
        """Gets the is_sas of this StorageAccount.  # noqa: E501


        :return: The is_sas of this StorageAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_sas

    @is_sas.setter
    def is_sas(self, is_sas):
        """Sets the is_sas of this StorageAccount.


        :param is_sas: The is_sas of this StorageAccount.  # noqa: E501
        :type: bool
        """

        self._is_sas = is_sas

    @property
    def private_url(self):
        """Gets the private_url of this StorageAccount.  # noqa: E501

        URL used by engines to access the cloud  # noqa: E501

        :return: The private_url of this StorageAccount.  # noqa: E501
        :rtype: str
        """
        return self._private_url

    @private_url.setter
    def private_url(self, private_url):
        """Sets the private_url of this StorageAccount.

        URL used by engines to access the cloud  # noqa: E501

        :param private_url: The private_url of this StorageAccount.  # noqa: E501
        :type: str
        """

        self._private_url = private_url

    @property
    def provider(self):
        """Gets the provider of this StorageAccount.  # noqa: E501

        Link to the storage provider (Amazon, Azure, etc)  # noqa: E501

        :return: The provider of this StorageAccount.  # noqa: E501
        :rtype: StorageProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this StorageAccount.

        Link to the storage provider (Amazon, Azure, etc)  # noqa: E501

        :param provider: The provider of this StorageAccount.  # noqa: E501
        :type: StorageProvider
        """

        self._provider = provider

    @property
    def settings(self):
        """Gets the settings of this StorageAccount.  # noqa: E501

        Configuration of this storage account  # noqa: E501

        :return: The settings of this StorageAccount.  # noqa: E501
        :rtype: StorageAccountSettingsRes
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this StorageAccount.

        Configuration of this storage account  # noqa: E501

        :param settings: The settings of this StorageAccount.  # noqa: E501
        :type: StorageAccountSettingsRes
        """

        self._settings = settings

    @property
    def stat(self):
        """Gets the stat of this StorageAccount.  # noqa: E501

        Storage account state and statistics  # noqa: E501

        :return: The stat of this StorageAccount.  # noqa: E501
        :rtype: StorageAccountStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this StorageAccount.

        Storage account state and statistics  # noqa: E501

        :param stat: The stat of this StorageAccount.  # noqa: E501
        :type: StorageAccountStat
        """

        self._stat = stat

    @property
    def url(self):
        """Gets the url of this StorageAccount.  # noqa: E501

        URL to the cloud  # noqa: E501

        :return: The url of this StorageAccount.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this StorageAccount.

        URL to the cloud  # noqa: E501

        :param url: The url of this StorageAccount.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(StorageAccount, dict):
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
        if not isinstance(other, StorageAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageAccount):
            return True

        return self.to_dict() != other.to_dict()
