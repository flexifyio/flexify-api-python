# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.12-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NewStorageAccount(object):
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
        'auth_code': 'str',
        'provider_id': 'int',
        'settings': 'StorageAccountSettingsReq'
    }

    attribute_map = {
        'auth_code': 'authCode',
        'provider_id': 'providerId',
        'settings': 'settings'
    }

    def __init__(self, auth_code=None, provider_id=None, settings=None):  # noqa: E501
        """NewStorageAccount - a model defined in Swagger"""  # noqa: E501

        self._auth_code = None
        self._provider_id = None
        self._settings = None
        self.discriminator = None

        if auth_code is not None:
            self.auth_code = auth_code
        if provider_id is not None:
            self.provider_id = provider_id
        if settings is not None:
            self.settings = settings

    @property
    def auth_code(self):
        """Gets the auth_code of this NewStorageAccount.  # noqa: E501

        OAuth code used to request credentials if OAuth is used  # noqa: E501

        :return: The auth_code of this NewStorageAccount.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this NewStorageAccount.

        OAuth code used to request credentials if OAuth is used  # noqa: E501

        :param auth_code: The auth_code of this NewStorageAccount.  # noqa: E501
        :type: str
        """

        self._auth_code = auth_code

    @property
    def provider_id(self):
        """Gets the provider_id of this NewStorageAccount.  # noqa: E501


        :return: The provider_id of this NewStorageAccount.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this NewStorageAccount.


        :param provider_id: The provider_id of this NewStorageAccount.  # noqa: E501
        :type: int
        """

        self._provider_id = provider_id

    @property
    def settings(self):
        """Gets the settings of this NewStorageAccount.  # noqa: E501

        Configuration of the storage account  # noqa: E501

        :return: The settings of this NewStorageAccount.  # noqa: E501
        :rtype: StorageAccountSettingsReq
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this NewStorageAccount.

        Configuration of the storage account  # noqa: E501

        :param settings: The settings of this NewStorageAccount.  # noqa: E501
        :type: StorageAccountSettingsReq
        """

        self._settings = settings

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
        if issubclass(NewStorageAccount, dict):
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
        if not isinstance(other, NewStorageAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
