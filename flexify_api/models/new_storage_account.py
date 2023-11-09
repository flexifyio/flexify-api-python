# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.20-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


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
        'finish_o_auth_params': 'FinishOAuthParams',
        'provider_id': 'int',
        'settings': 'StorageAccountSettingsReq'
    }

    attribute_map = {
        'finish_o_auth_params': 'finishOAuthParams',
        'provider_id': 'providerId',
        'settings': 'settings'
    }

    def __init__(self, finish_o_auth_params=None, provider_id=None, settings=None, _configuration=None):  # noqa: E501
        """NewStorageAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._finish_o_auth_params = None
        self._provider_id = None
        self._settings = None
        self.discriminator = None

        if finish_o_auth_params is not None:
            self.finish_o_auth_params = finish_o_auth_params
        if provider_id is not None:
            self.provider_id = provider_id
        if settings is not None:
            self.settings = settings

    @property
    def finish_o_auth_params(self):
        """Gets the finish_o_auth_params of this NewStorageAccount.  # noqa: E501

        OAuth parameters used to request credentials if OAuth is used  # noqa: E501

        :return: The finish_o_auth_params of this NewStorageAccount.  # noqa: E501
        :rtype: FinishOAuthParams
        """
        return self._finish_o_auth_params

    @finish_o_auth_params.setter
    def finish_o_auth_params(self, finish_o_auth_params):
        """Sets the finish_o_auth_params of this NewStorageAccount.

        OAuth parameters used to request credentials if OAuth is used  # noqa: E501

        :param finish_o_auth_params: The finish_o_auth_params of this NewStorageAccount.  # noqa: E501
        :type: FinishOAuthParams
        """

        self._finish_o_auth_params = finish_o_auth_params

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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewStorageAccount):
            return True

        return self.to_dict() != other.to_dict()
