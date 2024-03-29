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


class StorageAccountWithBuckets(object):
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
        'buckets': 'list[Bucket]',
        'id': 'int',
        'is_sas': 'bool',
        'key_vault_secret_id': 'str',
        'oauth_provider_id': 'str',
        'private_url': 'str',
        'provider': 'StorageProvider',
        'secret_in_key_vault': 'bool',
        'settings': 'StorageAccountSettingsRes',
        'stat': 'StorageAccountStat',
        'url': 'str'
    }

    attribute_map = {
        'buckets': 'buckets',
        'id': 'id',
        'is_sas': 'isSas',
        'key_vault_secret_id': 'keyVaultSecretId',
        'oauth_provider_id': 'oauthProviderId',
        'private_url': 'privateUrl',
        'provider': 'provider',
        'secret_in_key_vault': 'secretInKeyVault',
        'settings': 'settings',
        'stat': 'stat',
        'url': 'url'
    }

    def __init__(self, buckets=None, id=None, is_sas=None, key_vault_secret_id=None, oauth_provider_id=None, private_url=None, provider=None, secret_in_key_vault=None, settings=None, stat=None, url=None, _configuration=None):  # noqa: E501
        """StorageAccountWithBuckets - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._buckets = None
        self._id = None
        self._is_sas = None
        self._key_vault_secret_id = None
        self._oauth_provider_id = None
        self._private_url = None
        self._provider = None
        self._secret_in_key_vault = None
        self._settings = None
        self._stat = None
        self._url = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets
        if id is not None:
            self.id = id
        if is_sas is not None:
            self.is_sas = is_sas
        if key_vault_secret_id is not None:
            self.key_vault_secret_id = key_vault_secret_id
        if oauth_provider_id is not None:
            self.oauth_provider_id = oauth_provider_id
        if private_url is not None:
            self.private_url = private_url
        if provider is not None:
            self.provider = provider
        if secret_in_key_vault is not None:
            self.secret_in_key_vault = secret_in_key_vault
        if settings is not None:
            self.settings = settings
        if stat is not None:
            self.stat = stat
        if url is not None:
            self.url = url

    @property
    def buckets(self):
        """Gets the buckets of this StorageAccountWithBuckets.  # noqa: E501

        Buckets that we have cached for this storage account  # noqa: E501

        :return: The buckets of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: list[Bucket]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this StorageAccountWithBuckets.

        Buckets that we have cached for this storage account  # noqa: E501

        :param buckets: The buckets of this StorageAccountWithBuckets.  # noqa: E501
        :type: list[Bucket]
        """

        self._buckets = buckets

    @property
    def id(self):
        """Gets the id of this StorageAccountWithBuckets.  # noqa: E501

        Id of the storage account  # noqa: E501

        :return: The id of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageAccountWithBuckets.

        Id of the storage account  # noqa: E501

        :param id: The id of this StorageAccountWithBuckets.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_sas(self):
        """Gets the is_sas of this StorageAccountWithBuckets.  # noqa: E501

        For Azure - if credential is SAS signature (not included if storing in key vault)  # noqa: E501

        :return: The is_sas of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: bool
        """
        return self._is_sas

    @is_sas.setter
    def is_sas(self, is_sas):
        """Sets the is_sas of this StorageAccountWithBuckets.

        For Azure - if credential is SAS signature (not included if storing in key vault)  # noqa: E501

        :param is_sas: The is_sas of this StorageAccountWithBuckets.  # noqa: E501
        :type: bool
        """

        self._is_sas = is_sas

    @property
    def key_vault_secret_id(self):
        """Gets the key_vault_secret_id of this StorageAccountWithBuckets.  # noqa: E501

        Key Vault secret ID where this credential secret is stored (only for admins)  # noqa: E501

        :return: The key_vault_secret_id of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: str
        """
        return self._key_vault_secret_id

    @key_vault_secret_id.setter
    def key_vault_secret_id(self, key_vault_secret_id):
        """Sets the key_vault_secret_id of this StorageAccountWithBuckets.

        Key Vault secret ID where this credential secret is stored (only for admins)  # noqa: E501

        :param key_vault_secret_id: The key_vault_secret_id of this StorageAccountWithBuckets.  # noqa: E501
        :type: str
        """

        self._key_vault_secret_id = key_vault_secret_id

    @property
    def oauth_provider_id(self):
        """Gets the oauth_provider_id of this StorageAccountWithBuckets.  # noqa: E501

        OAuth provider if the storage account is using OAuth, or null otherwise  # noqa: E501

        :return: The oauth_provider_id of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: str
        """
        return self._oauth_provider_id

    @oauth_provider_id.setter
    def oauth_provider_id(self, oauth_provider_id):
        """Sets the oauth_provider_id of this StorageAccountWithBuckets.

        OAuth provider if the storage account is using OAuth, or null otherwise  # noqa: E501

        :param oauth_provider_id: The oauth_provider_id of this StorageAccountWithBuckets.  # noqa: E501
        :type: str
        """
        allowed_values = ["DROPBOX", "DROPBOX_TEAM", "MICROSOFT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                oauth_provider_id not in allowed_values):
            raise ValueError(
                "Invalid value for `oauth_provider_id` ({0}), must be one of {1}"  # noqa: E501
                .format(oauth_provider_id, allowed_values)
            )

        self._oauth_provider_id = oauth_provider_id

    @property
    def private_url(self):
        """Gets the private_url of this StorageAccountWithBuckets.  # noqa: E501

        URL used by engines to access the cloud  # noqa: E501

        :return: The private_url of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: str
        """
        return self._private_url

    @private_url.setter
    def private_url(self, private_url):
        """Sets the private_url of this StorageAccountWithBuckets.

        URL used by engines to access the cloud  # noqa: E501

        :param private_url: The private_url of this StorageAccountWithBuckets.  # noqa: E501
        :type: str
        """

        self._private_url = private_url

    @property
    def provider(self):
        """Gets the provider of this StorageAccountWithBuckets.  # noqa: E501

        Link to the storage provider (Amazon, Azure, etc)  # noqa: E501

        :return: The provider of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: StorageProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this StorageAccountWithBuckets.

        Link to the storage provider (Amazon, Azure, etc)  # noqa: E501

        :param provider: The provider of this StorageAccountWithBuckets.  # noqa: E501
        :type: StorageProvider
        """

        self._provider = provider

    @property
    def secret_in_key_vault(self):
        """Gets the secret_in_key_vault of this StorageAccountWithBuckets.  # noqa: E501

        If secret credential is stored in Key Vault  # noqa: E501

        :return: The secret_in_key_vault of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: bool
        """
        return self._secret_in_key_vault

    @secret_in_key_vault.setter
    def secret_in_key_vault(self, secret_in_key_vault):
        """Sets the secret_in_key_vault of this StorageAccountWithBuckets.

        If secret credential is stored in Key Vault  # noqa: E501

        :param secret_in_key_vault: The secret_in_key_vault of this StorageAccountWithBuckets.  # noqa: E501
        :type: bool
        """

        self._secret_in_key_vault = secret_in_key_vault

    @property
    def settings(self):
        """Gets the settings of this StorageAccountWithBuckets.  # noqa: E501

        Configuration of this storage account  # noqa: E501

        :return: The settings of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: StorageAccountSettingsRes
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this StorageAccountWithBuckets.

        Configuration of this storage account  # noqa: E501

        :param settings: The settings of this StorageAccountWithBuckets.  # noqa: E501
        :type: StorageAccountSettingsRes
        """

        self._settings = settings

    @property
    def stat(self):
        """Gets the stat of this StorageAccountWithBuckets.  # noqa: E501

        Storage account state and statistics  # noqa: E501

        :return: The stat of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: StorageAccountStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this StorageAccountWithBuckets.

        Storage account state and statistics  # noqa: E501

        :param stat: The stat of this StorageAccountWithBuckets.  # noqa: E501
        :type: StorageAccountStat
        """

        self._stat = stat

    @property
    def url(self):
        """Gets the url of this StorageAccountWithBuckets.  # noqa: E501

        URL to the cloud  # noqa: E501

        :return: The url of this StorageAccountWithBuckets.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this StorageAccountWithBuckets.

        URL to the cloud  # noqa: E501

        :param url: The url of this StorageAccountWithBuckets.  # noqa: E501
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
        if issubclass(StorageAccountWithBuckets, dict):
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
        if not isinstance(other, StorageAccountWithBuckets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageAccountWithBuckets):
            return True

        return self.to_dict() != other.to_dict()
