# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.11.0-dev
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StorageAccountSettings(object):
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
        'anonymous': 'bool',
        'credential': 'str',
        'custom_endpoint': 'str',
        'identity': 'str',
        'name': 'str',
        'refresh_interval_sec': 'int',
        'refresh_storages_stat': 'bool',
        'use_ssl': 'bool'
    }

    attribute_map = {
        'anonymous': 'anonymous',
        'credential': 'credential',
        'custom_endpoint': 'customEndpoint',
        'identity': 'identity',
        'name': 'name',
        'refresh_interval_sec': 'refreshIntervalSec',
        'refresh_storages_stat': 'refreshStoragesStat',
        'use_ssl': 'useSsl'
    }

    def __init__(self, anonymous=None, credential=None, custom_endpoint=None, identity=None, name=None, refresh_interval_sec=None, refresh_storages_stat=None, use_ssl=None):  # noqa: E501
        """StorageAccountSettings - a model defined in Swagger"""  # noqa: E501

        self._anonymous = None
        self._credential = None
        self._custom_endpoint = None
        self._identity = None
        self._name = None
        self._refresh_interval_sec = None
        self._refresh_storages_stat = None
        self._use_ssl = None
        self.discriminator = None

        if anonymous is not None:
            self.anonymous = anonymous
        if credential is not None:
            self.credential = credential
        if custom_endpoint is not None:
            self.custom_endpoint = custom_endpoint
        if identity is not None:
            self.identity = identity
        if name is not None:
            self.name = name
        if refresh_interval_sec is not None:
            self.refresh_interval_sec = refresh_interval_sec
        if refresh_storages_stat is not None:
            self.refresh_storages_stat = refresh_storages_stat
        if use_ssl is not None:
            self.use_ssl = use_ssl

    @property
    def anonymous(self):
        """Gets the anonymous of this StorageAccountSettings.  # noqa: E501

        True for public account  # noqa: E501

        :return: The anonymous of this StorageAccountSettings.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous):
        """Sets the anonymous of this StorageAccountSettings.

        True for public account  # noqa: E501

        :param anonymous: The anonymous of this StorageAccountSettings.  # noqa: E501
        :type: bool
        """

        self._anonymous = anonymous

    @property
    def credential(self):
        """Gets the credential of this StorageAccountSettings.  # noqa: E501

        Credential (such as Secret Key) of the cloud account  # noqa: E501

        :return: The credential of this StorageAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this StorageAccountSettings.

        Credential (such as Secret Key) of the cloud account  # noqa: E501

        :param credential: The credential of this StorageAccountSettings.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def custom_endpoint(self):
        """Gets the custom_endpoint of this StorageAccountSettings.  # noqa: E501

        Custom endpoint to be used for requests  # noqa: E501

        :return: The custom_endpoint of this StorageAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """Sets the custom_endpoint of this StorageAccountSettings.

        Custom endpoint to be used for requests  # noqa: E501

        :param custom_endpoint: The custom_endpoint of this StorageAccountSettings.  # noqa: E501
        :type: str
        """

        self._custom_endpoint = custom_endpoint

    @property
    def identity(self):
        """Gets the identity of this StorageAccountSettings.  # noqa: E501

        Identity (such as Key ID) of the cloud account  # noqa: E501

        :return: The identity of this StorageAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this StorageAccountSettings.

        Identity (such as Key ID) of the cloud account  # noqa: E501

        :param identity: The identity of this StorageAccountSettings.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def name(self):
        """Gets the name of this StorageAccountSettings.  # noqa: E501

        User-defined storage account name  # noqa: E501

        :return: The name of this StorageAccountSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageAccountSettings.

        User-defined storage account name  # noqa: E501

        :param name: The name of this StorageAccountSettings.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refresh_interval_sec(self):
        """Gets the refresh_interval_sec of this StorageAccountSettings.  # noqa: E501

        Automatic refresh interval in seconds or null to disable automatic refresh  # noqa: E501

        :return: The refresh_interval_sec of this StorageAccountSettings.  # noqa: E501
        :rtype: int
        """
        return self._refresh_interval_sec

    @refresh_interval_sec.setter
    def refresh_interval_sec(self, refresh_interval_sec):
        """Sets the refresh_interval_sec of this StorageAccountSettings.

        Automatic refresh interval in seconds or null to disable automatic refresh  # noqa: E501

        :param refresh_interval_sec: The refresh_interval_sec of this StorageAccountSettings.  # noqa: E501
        :type: int
        """

        self._refresh_interval_sec = refresh_interval_sec

    @property
    def refresh_storages_stat(self):
        """Gets the refresh_storages_stat of this StorageAccountSettings.  # noqa: E501

        Indicates if statistics for each bucket/container should be calculated on automatic refresh  # noqa: E501

        :return: The refresh_storages_stat of this StorageAccountSettings.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_storages_stat

    @refresh_storages_stat.setter
    def refresh_storages_stat(self, refresh_storages_stat):
        """Sets the refresh_storages_stat of this StorageAccountSettings.

        Indicates if statistics for each bucket/container should be calculated on automatic refresh  # noqa: E501

        :param refresh_storages_stat: The refresh_storages_stat of this StorageAccountSettings.  # noqa: E501
        :type: bool
        """

        self._refresh_storages_stat = refresh_storages_stat

    @property
    def use_ssl(self):
        """Gets the use_ssl of this StorageAccountSettings.  # noqa: E501

        Encrypt transfer with SSL  # noqa: E501

        :return: The use_ssl of this StorageAccountSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this StorageAccountSettings.

        Encrypt transfer with SSL  # noqa: E501

        :param use_ssl: The use_ssl of this StorageAccountSettings.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

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
        if issubclass(StorageAccountSettings, dict):
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
        if not isinstance(other, StorageAccountSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
