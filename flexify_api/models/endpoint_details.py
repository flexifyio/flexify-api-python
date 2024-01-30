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


class EndpointDetails(object):
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
        'accounts': 'list[EndpointStorageAccount]',
        'id': 'int',
        'key_vault_secret_id': 'str',
        'secret_in_key_vault': 'bool',
        'settings': 'EndpointSettingsRes',
        'stat': 'EndpointStat',
        'virtual_buckets': 'list[VirtualBucket]'
    }

    attribute_map = {
        'accounts': 'accounts',
        'id': 'id',
        'key_vault_secret_id': 'keyVaultSecretId',
        'secret_in_key_vault': 'secretInKeyVault',
        'settings': 'settings',
        'stat': 'stat',
        'virtual_buckets': 'virtualBuckets'
    }

    def __init__(self, accounts=None, id=None, key_vault_secret_id=None, secret_in_key_vault=None, settings=None, stat=None, virtual_buckets=None, _configuration=None):  # noqa: E501
        """EndpointDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts = None
        self._id = None
        self._key_vault_secret_id = None
        self._secret_in_key_vault = None
        self._settings = None
        self._stat = None
        self._virtual_buckets = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if id is not None:
            self.id = id
        if key_vault_secret_id is not None:
            self.key_vault_secret_id = key_vault_secret_id
        if secret_in_key_vault is not None:
            self.secret_in_key_vault = secret_in_key_vault
        self.settings = settings
        if stat is not None:
            self.stat = stat
        if virtual_buckets is not None:
            self.virtual_buckets = virtual_buckets

    @property
    def accounts(self):
        """Gets the accounts of this EndpointDetails.  # noqa: E501


        :return: The accounts of this EndpointDetails.  # noqa: E501
        :rtype: list[EndpointStorageAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this EndpointDetails.


        :param accounts: The accounts of this EndpointDetails.  # noqa: E501
        :type: list[EndpointStorageAccount]
        """

        self._accounts = accounts

    @property
    def id(self):
        """Gets the id of this EndpointDetails.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this EndpointDetails.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointDetails.

        Id  # noqa: E501

        :param id: The id of this EndpointDetails.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key_vault_secret_id(self):
        """Gets the key_vault_secret_id of this EndpointDetails.  # noqa: E501

        Key Vault secret ID where this credential secret is stored (only for admins)  # noqa: E501

        :return: The key_vault_secret_id of this EndpointDetails.  # noqa: E501
        :rtype: str
        """
        return self._key_vault_secret_id

    @key_vault_secret_id.setter
    def key_vault_secret_id(self, key_vault_secret_id):
        """Sets the key_vault_secret_id of this EndpointDetails.

        Key Vault secret ID where this credential secret is stored (only for admins)  # noqa: E501

        :param key_vault_secret_id: The key_vault_secret_id of this EndpointDetails.  # noqa: E501
        :type: str
        """

        self._key_vault_secret_id = key_vault_secret_id

    @property
    def secret_in_key_vault(self):
        """Gets the secret_in_key_vault of this EndpointDetails.  # noqa: E501

        If secret credential is stored in Key Vault  # noqa: E501

        :return: The secret_in_key_vault of this EndpointDetails.  # noqa: E501
        :rtype: bool
        """
        return self._secret_in_key_vault

    @secret_in_key_vault.setter
    def secret_in_key_vault(self, secret_in_key_vault):
        """Sets the secret_in_key_vault of this EndpointDetails.

        If secret credential is stored in Key Vault  # noqa: E501

        :param secret_in_key_vault: The secret_in_key_vault of this EndpointDetails.  # noqa: E501
        :type: bool
        """

        self._secret_in_key_vault = secret_in_key_vault

    @property
    def settings(self):
        """Gets the settings of this EndpointDetails.  # noqa: E501

        Settings of endpoint  # noqa: E501

        :return: The settings of this EndpointDetails.  # noqa: E501
        :rtype: EndpointSettingsRes
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this EndpointDetails.

        Settings of endpoint  # noqa: E501

        :param settings: The settings of this EndpointDetails.  # noqa: E501
        :type: EndpointSettingsRes
        """
        if self._configuration.client_side_validation and settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def stat(self):
        """Gets the stat of this EndpointDetails.  # noqa: E501


        :return: The stat of this EndpointDetails.  # noqa: E501
        :rtype: EndpointStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this EndpointDetails.


        :param stat: The stat of this EndpointDetails.  # noqa: E501
        :type: EndpointStat
        """

        self._stat = stat

    @property
    def virtual_buckets(self):
        """Gets the virtual_buckets of this EndpointDetails.  # noqa: E501


        :return: The virtual_buckets of this EndpointDetails.  # noqa: E501
        :rtype: list[VirtualBucket]
        """
        return self._virtual_buckets

    @virtual_buckets.setter
    def virtual_buckets(self, virtual_buckets):
        """Sets the virtual_buckets of this EndpointDetails.


        :param virtual_buckets: The virtual_buckets of this EndpointDetails.  # noqa: E501
        :type: list[VirtualBucket]
        """

        self._virtual_buckets = virtual_buckets

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
        if issubclass(EndpointDetails, dict):
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
        if not isinstance(other, EndpointDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointDetails):
            return True

        return self.to_dict() != other.to_dict()
