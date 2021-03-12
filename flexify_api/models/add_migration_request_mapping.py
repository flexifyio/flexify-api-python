# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.2-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AddMigrationRequestMapping(object):
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
        'dest_bucket_name': 'str',
        'dest_bucket_new_region': 'str',
        'dest_storage_account_id': 'int',
        'key_add_prefix': 'str',
        'key_remove_prefix': 'str',
        'source_bucket_name': 'str',
        'source_storage_account_id': 'int'
    }

    attribute_map = {
        'dest_bucket_name': 'destBucketName',
        'dest_bucket_new_region': 'destBucketNewRegion',
        'dest_storage_account_id': 'destStorageAccountId',
        'key_add_prefix': 'keyAddPrefix',
        'key_remove_prefix': 'keyRemovePrefix',
        'source_bucket_name': 'sourceBucketName',
        'source_storage_account_id': 'sourceStorageAccountId'
    }

    def __init__(self, dest_bucket_name=None, dest_bucket_new_region=None, dest_storage_account_id=None, key_add_prefix=None, key_remove_prefix=None, source_bucket_name=None, source_storage_account_id=None):  # noqa: E501
        """AddMigrationRequestMapping - a model defined in Swagger"""  # noqa: E501

        self._dest_bucket_name = None
        self._dest_bucket_new_region = None
        self._dest_storage_account_id = None
        self._key_add_prefix = None
        self._key_remove_prefix = None
        self._source_bucket_name = None
        self._source_storage_account_id = None
        self.discriminator = None

        self.dest_bucket_name = dest_bucket_name
        if dest_bucket_new_region is not None:
            self.dest_bucket_new_region = dest_bucket_new_region
        self.dest_storage_account_id = dest_storage_account_id
        if key_add_prefix is not None:
            self.key_add_prefix = key_add_prefix
        if key_remove_prefix is not None:
            self.key_remove_prefix = key_remove_prefix
        self.source_bucket_name = source_bucket_name
        self.source_storage_account_id = source_storage_account_id

    @property
    def dest_bucket_name(self):
        """Gets the dest_bucket_name of this AddMigrationRequestMapping.  # noqa: E501

        Name of source destination or container  # noqa: E501

        :return: The dest_bucket_name of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: str
        """
        return self._dest_bucket_name

    @dest_bucket_name.setter
    def dest_bucket_name(self, dest_bucket_name):
        """Sets the dest_bucket_name of this AddMigrationRequestMapping.

        Name of source destination or container  # noqa: E501

        :param dest_bucket_name: The dest_bucket_name of this AddMigrationRequestMapping.  # noqa: E501
        :type: str
        """
        if dest_bucket_name is None:
            raise ValueError("Invalid value for `dest_bucket_name`, must not be `None`")  # noqa: E501

        self._dest_bucket_name = dest_bucket_name

    @property
    def dest_bucket_new_region(self):
        """Gets the dest_bucket_new_region of this AddMigrationRequestMapping.  # noqa: E501

        Region where the destination bucket will be created if it does not exist. null to use cloud's default region  # noqa: E501

        :return: The dest_bucket_new_region of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: str
        """
        return self._dest_bucket_new_region

    @dest_bucket_new_region.setter
    def dest_bucket_new_region(self, dest_bucket_new_region):
        """Sets the dest_bucket_new_region of this AddMigrationRequestMapping.

        Region where the destination bucket will be created if it does not exist. null to use cloud's default region  # noqa: E501

        :param dest_bucket_new_region: The dest_bucket_new_region of this AddMigrationRequestMapping.  # noqa: E501
        :type: str
        """

        self._dest_bucket_new_region = dest_bucket_new_region

    @property
    def dest_storage_account_id(self):
        """Gets the dest_storage_account_id of this AddMigrationRequestMapping.  # noqa: E501

        ID of source destination account  # noqa: E501

        :return: The dest_storage_account_id of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: int
        """
        return self._dest_storage_account_id

    @dest_storage_account_id.setter
    def dest_storage_account_id(self, dest_storage_account_id):
        """Sets the dest_storage_account_id of this AddMigrationRequestMapping.

        ID of source destination account  # noqa: E501

        :param dest_storage_account_id: The dest_storage_account_id of this AddMigrationRequestMapping.  # noqa: E501
        :type: int
        """
        if dest_storage_account_id is None:
            raise ValueError("Invalid value for `dest_storage_account_id`, must not be `None`")  # noqa: E501

        self._dest_storage_account_id = dest_storage_account_id

    @property
    def key_add_prefix(self):
        """Gets the key_add_prefix of this AddMigrationRequestMapping.  # noqa: E501

        Prefix to to be added to each key when migrating  # noqa: E501

        :return: The key_add_prefix of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: str
        """
        return self._key_add_prefix

    @key_add_prefix.setter
    def key_add_prefix(self, key_add_prefix):
        """Sets the key_add_prefix of this AddMigrationRequestMapping.

        Prefix to to be added to each key when migrating  # noqa: E501

        :param key_add_prefix: The key_add_prefix of this AddMigrationRequestMapping.  # noqa: E501
        :type: str
        """

        self._key_add_prefix = key_add_prefix

    @property
    def key_remove_prefix(self):
        """Gets the key_remove_prefix of this AddMigrationRequestMapping.  # noqa: E501

        Prefix to to be removed from each key when migrating  # noqa: E501

        :return: The key_remove_prefix of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: str
        """
        return self._key_remove_prefix

    @key_remove_prefix.setter
    def key_remove_prefix(self, key_remove_prefix):
        """Sets the key_remove_prefix of this AddMigrationRequestMapping.

        Prefix to to be removed from each key when migrating  # noqa: E501

        :param key_remove_prefix: The key_remove_prefix of this AddMigrationRequestMapping.  # noqa: E501
        :type: str
        """

        self._key_remove_prefix = key_remove_prefix

    @property
    def source_bucket_name(self):
        """Gets the source_bucket_name of this AddMigrationRequestMapping.  # noqa: E501

        Name of source bucket or container  # noqa: E501

        :return: The source_bucket_name of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: str
        """
        return self._source_bucket_name

    @source_bucket_name.setter
    def source_bucket_name(self, source_bucket_name):
        """Sets the source_bucket_name of this AddMigrationRequestMapping.

        Name of source bucket or container  # noqa: E501

        :param source_bucket_name: The source_bucket_name of this AddMigrationRequestMapping.  # noqa: E501
        :type: str
        """
        if source_bucket_name is None:
            raise ValueError("Invalid value for `source_bucket_name`, must not be `None`")  # noqa: E501

        self._source_bucket_name = source_bucket_name

    @property
    def source_storage_account_id(self):
        """Gets the source_storage_account_id of this AddMigrationRequestMapping.  # noqa: E501

        ID of source storage account  # noqa: E501

        :return: The source_storage_account_id of this AddMigrationRequestMapping.  # noqa: E501
        :rtype: int
        """
        return self._source_storage_account_id

    @source_storage_account_id.setter
    def source_storage_account_id(self, source_storage_account_id):
        """Sets the source_storage_account_id of this AddMigrationRequestMapping.

        ID of source storage account  # noqa: E501

        :param source_storage_account_id: The source_storage_account_id of this AddMigrationRequestMapping.  # noqa: E501
        :type: int
        """
        if source_storage_account_id is None:
            raise ValueError("Invalid value for `source_storage_account_id`, must not be `None`")  # noqa: E501

        self._source_storage_account_id = source_storage_account_id

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
        if issubclass(AddMigrationRequestMapping, dict):
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
        if not isinstance(other, AddMigrationRequestMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
