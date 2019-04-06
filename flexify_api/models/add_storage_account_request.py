# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.8.0-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.models.new_storage_account import NewStorageAccount  # noqa: F401,E501


class AddStorageAccountRequest(object):
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
        'storage_account': 'NewStorageAccount',
        'include_buckets': 'list[str]',
        'endpoint_id': 'int',
        'put_objects': 'bool',
        'refresh': 'bool'
    }

    attribute_map = {
        'storage_account': 'storageAccount',
        'include_buckets': 'includeBuckets',
        'endpoint_id': 'endpointId',
        'put_objects': 'putObjects',
        'refresh': 'refresh'
    }

    def __init__(self, storage_account=None, include_buckets=None, endpoint_id=None, put_objects=None, refresh=None):  # noqa: E501
        """AddStorageAccountRequest - a model defined in Swagger"""  # noqa: E501

        self._storage_account = None
        self._include_buckets = None
        self._endpoint_id = None
        self._put_objects = None
        self._refresh = None
        self.discriminator = None

        if storage_account is not None:
            self.storage_account = storage_account
        if include_buckets is not None:
            self.include_buckets = include_buckets
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if put_objects is not None:
            self.put_objects = put_objects
        if refresh is not None:
            self.refresh = refresh

    @property
    def storage_account(self):
        """Gets the storage_account of this AddStorageAccountRequest.  # noqa: E501

        Storage account to create  # noqa: E501

        :return: The storage_account of this AddStorageAccountRequest.  # noqa: E501
        :rtype: NewStorageAccount
        """
        return self._storage_account

    @storage_account.setter
    def storage_account(self, storage_account):
        """Sets the storage_account of this AddStorageAccountRequest.

        Storage account to create  # noqa: E501

        :param storage_account: The storage_account of this AddStorageAccountRequest.  # noqa: E501
        :type: NewStorageAccount
        """

        self._storage_account = storage_account

    @property
    def include_buckets(self):
        """Gets the include_buckets of this AddStorageAccountRequest.  # noqa: E501

        Lists of buckets to start monitoring, or null to request buckets from the cloud  # noqa: E501

        :return: The include_buckets of this AddStorageAccountRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_buckets

    @include_buckets.setter
    def include_buckets(self, include_buckets):
        """Sets the include_buckets of this AddStorageAccountRequest.

        Lists of buckets to start monitoring, or null to request buckets from the cloud  # noqa: E501

        :param include_buckets: The include_buckets of this AddStorageAccountRequest.  # noqa: E501
        :type: list[str]
        """

        self._include_buckets = include_buckets

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this AddStorageAccountRequest.  # noqa: E501

        ID of the user endpoint to add storages to. Do not set the value if you want to attach storages to the endpoint later  # noqa: E501

        :return: The endpoint_id of this AddStorageAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this AddStorageAccountRequest.

        ID of the user endpoint to add storages to. Do not set the value if you want to attach storages to the endpoint later  # noqa: E501

        :param endpoint_id: The endpoint_id of this AddStorageAccountRequest.  # noqa: E501
        :type: int
        """

        self._endpoint_id = endpoint_id

    @property
    def put_objects(self):
        """Gets the put_objects of this AddStorageAccountRequest.  # noqa: E501

        Specifies if new data should be stored to added storages  # noqa: E501

        :return: The put_objects of this AddStorageAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._put_objects

    @put_objects.setter
    def put_objects(self, put_objects):
        """Sets the put_objects of this AddStorageAccountRequest.

        Specifies if new data should be stored to added storages  # noqa: E501

        :param put_objects: The put_objects of this AddStorageAccountRequest.  # noqa: E501
        :type: bool
        """

        self._put_objects = put_objects

    @property
    def refresh(self):
        """Gets the refresh of this AddStorageAccountRequest.  # noqa: E501

        If set to true, buckets will be refreshed after storage is added  # noqa: E501

        :return: The refresh of this AddStorageAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this AddStorageAccountRequest.

        If set to true, buckets will be refreshed after storage is added  # noqa: E501

        :param refresh: The refresh of this AddStorageAccountRequest.  # noqa: E501
        :type: bool
        """

        self._refresh = refresh

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
        if issubclass(AddStorageAccountRequest, dict):
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
        if not isinstance(other, AddStorageAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
