# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class StorageAccountSettingsReq(object):
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
        'bucket_dot_encode_sequence': 'str',
        'credential': 'str',
        'custom_endpoint': 'str',
        'identity': 'str',
        'name': 'str',
        'refresh_interval_sec': 'int',
        'refresh_storages_stat': 'bool',
        'use_ssl': 'bool'
    }

    attribute_map = {
        'bucket_dot_encode_sequence': 'bucketDotEncodeSequence',
        'credential': 'credential',
        'custom_endpoint': 'customEndpoint',
        'identity': 'identity',
        'name': 'name',
        'refresh_interval_sec': 'refreshIntervalSec',
        'refresh_storages_stat': 'refreshStoragesStat',
        'use_ssl': 'useSsl'
    }

    def __init__(self, bucket_dot_encode_sequence=None, credential=None, custom_endpoint=None, identity=None, name=None, refresh_interval_sec=None, refresh_storages_stat=None, use_ssl=None, _configuration=None):  # noqa: E501
        """StorageAccountSettingsReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_dot_encode_sequence = None
        self._credential = None
        self._custom_endpoint = None
        self._identity = None
        self._name = None
        self._refresh_interval_sec = None
        self._refresh_storages_stat = None
        self._use_ssl = None
        self.discriminator = None

        if bucket_dot_encode_sequence is not None:
            self.bucket_dot_encode_sequence = bucket_dot_encode_sequence
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
    def bucket_dot_encode_sequence(self):
        """Gets the bucket_dot_encode_sequence of this StorageAccountSettingsReq.  # noqa: E501

        Dot escape sequence for buckets  # noqa: E501

        :return: The bucket_dot_encode_sequence of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._bucket_dot_encode_sequence

    @bucket_dot_encode_sequence.setter
    def bucket_dot_encode_sequence(self, bucket_dot_encode_sequence):
        """Sets the bucket_dot_encode_sequence of this StorageAccountSettingsReq.

        Dot escape sequence for buckets  # noqa: E501

        :param bucket_dot_encode_sequence: The bucket_dot_encode_sequence of this StorageAccountSettingsReq.  # noqa: E501
        :type: str
        """

        self._bucket_dot_encode_sequence = bucket_dot_encode_sequence

    @property
    def credential(self):
        """Gets the credential of this StorageAccountSettingsReq.  # noqa: E501

        Credential (such as Secret Key) of the cloud account  # noqa: E501

        :return: The credential of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this StorageAccountSettingsReq.

        Credential (such as Secret Key) of the cloud account  # noqa: E501

        :param credential: The credential of this StorageAccountSettingsReq.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def custom_endpoint(self):
        """Gets the custom_endpoint of this StorageAccountSettingsReq.  # noqa: E501

        Custom endpoint to be used for requests  # noqa: E501

        :return: The custom_endpoint of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """Sets the custom_endpoint of this StorageAccountSettingsReq.

        Custom endpoint to be used for requests  # noqa: E501

        :param custom_endpoint: The custom_endpoint of this StorageAccountSettingsReq.  # noqa: E501
        :type: str
        """

        self._custom_endpoint = custom_endpoint

    @property
    def identity(self):
        """Gets the identity of this StorageAccountSettingsReq.  # noqa: E501

        Identity (such as Key ID) of the cloud account  # noqa: E501

        :return: The identity of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this StorageAccountSettingsReq.

        Identity (such as Key ID) of the cloud account  # noqa: E501

        :param identity: The identity of this StorageAccountSettingsReq.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def name(self):
        """Gets the name of this StorageAccountSettingsReq.  # noqa: E501

        User-defined storage account name  # noqa: E501

        :return: The name of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageAccountSettingsReq.

        User-defined storage account name  # noqa: E501

        :param name: The name of this StorageAccountSettingsReq.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refresh_interval_sec(self):
        """Gets the refresh_interval_sec of this StorageAccountSettingsReq.  # noqa: E501

        Automatic refresh interval in seconds or null to disable automatic refresh  # noqa: E501

        :return: The refresh_interval_sec of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: int
        """
        return self._refresh_interval_sec

    @refresh_interval_sec.setter
    def refresh_interval_sec(self, refresh_interval_sec):
        """Sets the refresh_interval_sec of this StorageAccountSettingsReq.

        Automatic refresh interval in seconds or null to disable automatic refresh  # noqa: E501

        :param refresh_interval_sec: The refresh_interval_sec of this StorageAccountSettingsReq.  # noqa: E501
        :type: int
        """

        self._refresh_interval_sec = refresh_interval_sec

    @property
    def refresh_storages_stat(self):
        """Gets the refresh_storages_stat of this StorageAccountSettingsReq.  # noqa: E501

        Indicates if statistics for each bucket/container should be calculated on automatic refresh  # noqa: E501

        :return: The refresh_storages_stat of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_storages_stat

    @refresh_storages_stat.setter
    def refresh_storages_stat(self, refresh_storages_stat):
        """Sets the refresh_storages_stat of this StorageAccountSettingsReq.

        Indicates if statistics for each bucket/container should be calculated on automatic refresh  # noqa: E501

        :param refresh_storages_stat: The refresh_storages_stat of this StorageAccountSettingsReq.  # noqa: E501
        :type: bool
        """

        self._refresh_storages_stat = refresh_storages_stat

    @property
    def use_ssl(self):
        """Gets the use_ssl of this StorageAccountSettingsReq.  # noqa: E501

        Encrypt transfer with SSL  # noqa: E501

        :return: The use_ssl of this StorageAccountSettingsReq.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this StorageAccountSettingsReq.

        Encrypt transfer with SSL  # noqa: E501

        :param use_ssl: The use_ssl of this StorageAccountSettingsReq.  # noqa: E501
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
        if issubclass(StorageAccountSettingsReq, dict):
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
        if not isinstance(other, StorageAccountSettingsReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageAccountSettingsReq):
            return True

        return self.to_dict() != other.to_dict()
