# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.11-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PriceConstraints(object):
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
        'dest_region': 'str',
        'dest_storage_provider_id': 'int',
        'engine_cloud_name': 'str',
        'engine_cloud_region': 'str',
        'source_region': 'str',
        'source_storage_provider_id': 'int',
        'valid_from': 'datetime',
        'valid_to': 'datetime'
    }

    attribute_map = {
        'dest_region': 'destRegion',
        'dest_storage_provider_id': 'destStorageProviderId',
        'engine_cloud_name': 'engineCloudName',
        'engine_cloud_region': 'engineCloudRegion',
        'source_region': 'sourceRegion',
        'source_storage_provider_id': 'sourceStorageProviderId',
        'valid_from': 'validFrom',
        'valid_to': 'validTo'
    }

    def __init__(self, dest_region=None, dest_storage_provider_id=None, engine_cloud_name=None, engine_cloud_region=None, source_region=None, source_storage_provider_id=None, valid_from=None, valid_to=None):  # noqa: E501
        """PriceConstraints - a model defined in Swagger"""  # noqa: E501

        self._dest_region = None
        self._dest_storage_provider_id = None
        self._engine_cloud_name = None
        self._engine_cloud_region = None
        self._source_region = None
        self._source_storage_provider_id = None
        self._valid_from = None
        self._valid_to = None
        self.discriminator = None

        if dest_region is not None:
            self.dest_region = dest_region
        if dest_storage_provider_id is not None:
            self.dest_storage_provider_id = dest_storage_provider_id
        if engine_cloud_name is not None:
            self.engine_cloud_name = engine_cloud_name
        if engine_cloud_region is not None:
            self.engine_cloud_region = engine_cloud_region
        if source_region is not None:
            self.source_region = source_region
        if source_storage_provider_id is not None:
            self.source_storage_provider_id = source_storage_provider_id
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to

    @property
    def dest_region(self):
        """Gets the dest_region of this PriceConstraints.  # noqa: E501

        Destination region string  # noqa: E501

        :return: The dest_region of this PriceConstraints.  # noqa: E501
        :rtype: str
        """
        return self._dest_region

    @dest_region.setter
    def dest_region(self, dest_region):
        """Sets the dest_region of this PriceConstraints.

        Destination region string  # noqa: E501

        :param dest_region: The dest_region of this PriceConstraints.  # noqa: E501
        :type: str
        """

        self._dest_region = dest_region

    @property
    def dest_storage_provider_id(self):
        """Gets the dest_storage_provider_id of this PriceConstraints.  # noqa: E501

        Destination storage provider  # noqa: E501

        :return: The dest_storage_provider_id of this PriceConstraints.  # noqa: E501
        :rtype: int
        """
        return self._dest_storage_provider_id

    @dest_storage_provider_id.setter
    def dest_storage_provider_id(self, dest_storage_provider_id):
        """Sets the dest_storage_provider_id of this PriceConstraints.

        Destination storage provider  # noqa: E501

        :param dest_storage_provider_id: The dest_storage_provider_id of this PriceConstraints.  # noqa: E501
        :type: int
        """

        self._dest_storage_provider_id = dest_storage_provider_id

    @property
    def engine_cloud_name(self):
        """Gets the engine_cloud_name of this PriceConstraints.  # noqa: E501

        Cloud where engines run  # noqa: E501

        :return: The engine_cloud_name of this PriceConstraints.  # noqa: E501
        :rtype: str
        """
        return self._engine_cloud_name

    @engine_cloud_name.setter
    def engine_cloud_name(self, engine_cloud_name):
        """Sets the engine_cloud_name of this PriceConstraints.

        Cloud where engines run  # noqa: E501

        :param engine_cloud_name: The engine_cloud_name of this PriceConstraints.  # noqa: E501
        :type: str
        """

        self._engine_cloud_name = engine_cloud_name

    @property
    def engine_cloud_region(self):
        """Gets the engine_cloud_region of this PriceConstraints.  # noqa: E501

        Regions where engines run  # noqa: E501

        :return: The engine_cloud_region of this PriceConstraints.  # noqa: E501
        :rtype: str
        """
        return self._engine_cloud_region

    @engine_cloud_region.setter
    def engine_cloud_region(self, engine_cloud_region):
        """Sets the engine_cloud_region of this PriceConstraints.

        Regions where engines run  # noqa: E501

        :param engine_cloud_region: The engine_cloud_region of this PriceConstraints.  # noqa: E501
        :type: str
        """

        self._engine_cloud_region = engine_cloud_region

    @property
    def source_region(self):
        """Gets the source_region of this PriceConstraints.  # noqa: E501

        Source region string  # noqa: E501

        :return: The source_region of this PriceConstraints.  # noqa: E501
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this PriceConstraints.

        Source region string  # noqa: E501

        :param source_region: The source_region of this PriceConstraints.  # noqa: E501
        :type: str
        """

        self._source_region = source_region

    @property
    def source_storage_provider_id(self):
        """Gets the source_storage_provider_id of this PriceConstraints.  # noqa: E501

        Source storage provider  # noqa: E501

        :return: The source_storage_provider_id of this PriceConstraints.  # noqa: E501
        :rtype: int
        """
        return self._source_storage_provider_id

    @source_storage_provider_id.setter
    def source_storage_provider_id(self, source_storage_provider_id):
        """Sets the source_storage_provider_id of this PriceConstraints.

        Source storage provider  # noqa: E501

        :param source_storage_provider_id: The source_storage_provider_id of this PriceConstraints.  # noqa: E501
        :type: int
        """

        self._source_storage_provider_id = source_storage_provider_id

    @property
    def valid_from(self):
        """Gets the valid_from of this PriceConstraints.  # noqa: E501

        Price valid from date  # noqa: E501

        :return: The valid_from of this PriceConstraints.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this PriceConstraints.

        Price valid from date  # noqa: E501

        :param valid_from: The valid_from of this PriceConstraints.  # noqa: E501
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this PriceConstraints.  # noqa: E501

        Price valid to date  # noqa: E501

        :return: The valid_to of this PriceConstraints.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this PriceConstraints.

        Price valid to date  # noqa: E501

        :param valid_to: The valid_to of this PriceConstraints.  # noqa: E501
        :type: datetime
        """

        self._valid_to = valid_to

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
        if issubclass(PriceConstraints, dict):
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
        if not isinstance(other, PriceConstraints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
