# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.2.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Mapping(object):
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
        'dest_bucket': 'Bucket',
        'dest_bucket_new_region': 'str',
        'dest_storage_account': 'StorageAccount',
        'id': 'int',
        'key_add_prefix': 'str',
        'key_remove_prefix': 'str',
        'slots': 'list[Slot]',
        'source_bucket': 'Bucket',
        'source_storage_account': 'StorageAccount',
        'stat': 'MappingStat'
    }

    attribute_map = {
        'dest_bucket': 'destBucket',
        'dest_bucket_new_region': 'destBucketNewRegion',
        'dest_storage_account': 'destStorageAccount',
        'id': 'id',
        'key_add_prefix': 'keyAddPrefix',
        'key_remove_prefix': 'keyRemovePrefix',
        'slots': 'slots',
        'source_bucket': 'sourceBucket',
        'source_storage_account': 'sourceStorageAccount',
        'stat': 'stat'
    }

    def __init__(self, dest_bucket=None, dest_bucket_new_region=None, dest_storage_account=None, id=None, key_add_prefix=None, key_remove_prefix=None, slots=None, source_bucket=None, source_storage_account=None, stat=None):  # noqa: E501
        """Mapping - a model defined in Swagger"""  # noqa: E501

        self._dest_bucket = None
        self._dest_bucket_new_region = None
        self._dest_storage_account = None
        self._id = None
        self._key_add_prefix = None
        self._key_remove_prefix = None
        self._slots = None
        self._source_bucket = None
        self._source_storage_account = None
        self._stat = None
        self.discriminator = None

        self.dest_bucket = dest_bucket
        if dest_bucket_new_region is not None:
            self.dest_bucket_new_region = dest_bucket_new_region
        self.dest_storage_account = dest_storage_account
        self.id = id
        if key_add_prefix is not None:
            self.key_add_prefix = key_add_prefix
        if key_remove_prefix is not None:
            self.key_remove_prefix = key_remove_prefix
        self.slots = slots
        self.source_bucket = source_bucket
        self.source_storage_account = source_storage_account
        self.stat = stat

    @property
    def dest_bucket(self):
        """Gets the dest_bucket of this Mapping.  # noqa: E501

        Destination bucket/container  # noqa: E501

        :return: The dest_bucket of this Mapping.  # noqa: E501
        :rtype: Bucket
        """
        return self._dest_bucket

    @dest_bucket.setter
    def dest_bucket(self, dest_bucket):
        """Sets the dest_bucket of this Mapping.

        Destination bucket/container  # noqa: E501

        :param dest_bucket: The dest_bucket of this Mapping.  # noqa: E501
        :type: Bucket
        """
        if dest_bucket is None:
            raise ValueError("Invalid value for `dest_bucket`, must not be `None`")  # noqa: E501

        self._dest_bucket = dest_bucket

    @property
    def dest_bucket_new_region(self):
        """Gets the dest_bucket_new_region of this Mapping.  # noqa: E501

        Region where bucket should be created if missing  # noqa: E501

        :return: The dest_bucket_new_region of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._dest_bucket_new_region

    @dest_bucket_new_region.setter
    def dest_bucket_new_region(self, dest_bucket_new_region):
        """Sets the dest_bucket_new_region of this Mapping.

        Region where bucket should be created if missing  # noqa: E501

        :param dest_bucket_new_region: The dest_bucket_new_region of this Mapping.  # noqa: E501
        :type: str
        """

        self._dest_bucket_new_region = dest_bucket_new_region

    @property
    def dest_storage_account(self):
        """Gets the dest_storage_account of this Mapping.  # noqa: E501

        Destination storage account  # noqa: E501

        :return: The dest_storage_account of this Mapping.  # noqa: E501
        :rtype: StorageAccount
        """
        return self._dest_storage_account

    @dest_storage_account.setter
    def dest_storage_account(self, dest_storage_account):
        """Sets the dest_storage_account of this Mapping.

        Destination storage account  # noqa: E501

        :param dest_storage_account: The dest_storage_account of this Mapping.  # noqa: E501
        :type: StorageAccount
        """
        if dest_storage_account is None:
            raise ValueError("Invalid value for `dest_storage_account`, must not be `None`")  # noqa: E501

        self._dest_storage_account = dest_storage_account

    @property
    def id(self):
        """Gets the id of this Mapping.  # noqa: E501

        ID of this mapping  # noqa: E501

        :return: The id of this Mapping.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Mapping.

        ID of this mapping  # noqa: E501

        :param id: The id of this Mapping.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def key_add_prefix(self):
        """Gets the key_add_prefix of this Mapping.  # noqa: E501

        Prefix added to each object key  # noqa: E501

        :return: The key_add_prefix of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._key_add_prefix

    @key_add_prefix.setter
    def key_add_prefix(self, key_add_prefix):
        """Sets the key_add_prefix of this Mapping.

        Prefix added to each object key  # noqa: E501

        :param key_add_prefix: The key_add_prefix of this Mapping.  # noqa: E501
        :type: str
        """

        self._key_add_prefix = key_add_prefix

    @property
    def key_remove_prefix(self):
        """Gets the key_remove_prefix of this Mapping.  # noqa: E501

        Prefix removed from each object key  # noqa: E501

        :return: The key_remove_prefix of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._key_remove_prefix

    @key_remove_prefix.setter
    def key_remove_prefix(self, key_remove_prefix):
        """Sets the key_remove_prefix of this Mapping.

        Prefix removed from each object key  # noqa: E501

        :param key_remove_prefix: The key_remove_prefix of this Mapping.  # noqa: E501
        :type: str
        """

        self._key_remove_prefix = key_remove_prefix

    @property
    def slots(self):
        """Gets the slots of this Mapping.  # noqa: E501

        Slots that this mapping is split into  # noqa: E501

        :return: The slots of this Mapping.  # noqa: E501
        :rtype: list[Slot]
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        """Sets the slots of this Mapping.

        Slots that this mapping is split into  # noqa: E501

        :param slots: The slots of this Mapping.  # noqa: E501
        :type: list[Slot]
        """
        if slots is None:
            raise ValueError("Invalid value for `slots`, must not be `None`")  # noqa: E501

        self._slots = slots

    @property
    def source_bucket(self):
        """Gets the source_bucket of this Mapping.  # noqa: E501

        Source bucket/container  # noqa: E501

        :return: The source_bucket of this Mapping.  # noqa: E501
        :rtype: Bucket
        """
        return self._source_bucket

    @source_bucket.setter
    def source_bucket(self, source_bucket):
        """Sets the source_bucket of this Mapping.

        Source bucket/container  # noqa: E501

        :param source_bucket: The source_bucket of this Mapping.  # noqa: E501
        :type: Bucket
        """
        if source_bucket is None:
            raise ValueError("Invalid value for `source_bucket`, must not be `None`")  # noqa: E501

        self._source_bucket = source_bucket

    @property
    def source_storage_account(self):
        """Gets the source_storage_account of this Mapping.  # noqa: E501

        Source storage account  # noqa: E501

        :return: The source_storage_account of this Mapping.  # noqa: E501
        :rtype: StorageAccount
        """
        return self._source_storage_account

    @source_storage_account.setter
    def source_storage_account(self, source_storage_account):
        """Sets the source_storage_account of this Mapping.

        Source storage account  # noqa: E501

        :param source_storage_account: The source_storage_account of this Mapping.  # noqa: E501
        :type: StorageAccount
        """
        if source_storage_account is None:
            raise ValueError("Invalid value for `source_storage_account`, must not be `None`")  # noqa: E501

        self._source_storage_account = source_storage_account

    @property
    def stat(self):
        """Gets the stat of this Mapping.  # noqa: E501

        Cumulative statistics of this mapping  # noqa: E501

        :return: The stat of this Mapping.  # noqa: E501
        :rtype: MappingStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this Mapping.

        Cumulative statistics of this mapping  # noqa: E501

        :param stat: The stat of this Mapping.  # noqa: E501
        :type: MappingStat
        """
        if stat is None:
            raise ValueError("Invalid value for `stat`, must not be `None`")  # noqa: E501

        self._stat = stat

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
        if issubclass(Mapping, dict):
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
        if not isinstance(other, Mapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
