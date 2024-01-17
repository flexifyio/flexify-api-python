# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.0
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class PublicAuthenticationConfiguration(object):
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
        'microsoft_client_id': 'str',
        'microsoft_scope': 'str',
        'microsoft_tenant_id': 'str',
        'use_device_code_flow': 'bool'
    }

    attribute_map = {
        'microsoft_client_id': 'microsoftClientId',
        'microsoft_scope': 'microsoftScope',
        'microsoft_tenant_id': 'microsoftTenantId',
        'use_device_code_flow': 'useDeviceCodeFlow'
    }

    def __init__(self, microsoft_client_id=None, microsoft_scope=None, microsoft_tenant_id=None, use_device_code_flow=None, _configuration=None):  # noqa: E501
        """PublicAuthenticationConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._microsoft_client_id = None
        self._microsoft_scope = None
        self._microsoft_tenant_id = None
        self._use_device_code_flow = None
        self.discriminator = None

        if microsoft_client_id is not None:
            self.microsoft_client_id = microsoft_client_id
        if microsoft_scope is not None:
            self.microsoft_scope = microsoft_scope
        if microsoft_tenant_id is not None:
            self.microsoft_tenant_id = microsoft_tenant_id
        if use_device_code_flow is not None:
            self.use_device_code_flow = use_device_code_flow

    @property
    def microsoft_client_id(self):
        """Gets the microsoft_client_id of this PublicAuthenticationConfiguration.  # noqa: E501

        Required client Id in Microsoft access token  # noqa: E501

        :return: The microsoft_client_id of this PublicAuthenticationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._microsoft_client_id

    @microsoft_client_id.setter
    def microsoft_client_id(self, microsoft_client_id):
        """Sets the microsoft_client_id of this PublicAuthenticationConfiguration.

        Required client Id in Microsoft access token  # noqa: E501

        :param microsoft_client_id: The microsoft_client_id of this PublicAuthenticationConfiguration.  # noqa: E501
        :type: str
        """

        self._microsoft_client_id = microsoft_client_id

    @property
    def microsoft_scope(self):
        """Gets the microsoft_scope of this PublicAuthenticationConfiguration.  # noqa: E501

        Required scope in Microsoft access token  # noqa: E501

        :return: The microsoft_scope of this PublicAuthenticationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._microsoft_scope

    @microsoft_scope.setter
    def microsoft_scope(self, microsoft_scope):
        """Sets the microsoft_scope of this PublicAuthenticationConfiguration.

        Required scope in Microsoft access token  # noqa: E501

        :param microsoft_scope: The microsoft_scope of this PublicAuthenticationConfiguration.  # noqa: E501
        :type: str
        """

        self._microsoft_scope = microsoft_scope

    @property
    def microsoft_tenant_id(self):
        """Gets the microsoft_tenant_id of this PublicAuthenticationConfiguration.  # noqa: E501

        Optional tenant Id in Microsoft access token  # noqa: E501

        :return: The microsoft_tenant_id of this PublicAuthenticationConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._microsoft_tenant_id

    @microsoft_tenant_id.setter
    def microsoft_tenant_id(self, microsoft_tenant_id):
        """Sets the microsoft_tenant_id of this PublicAuthenticationConfiguration.

        Optional tenant Id in Microsoft access token  # noqa: E501

        :param microsoft_tenant_id: The microsoft_tenant_id of this PublicAuthenticationConfiguration.  # noqa: E501
        :type: str
        """

        self._microsoft_tenant_id = microsoft_tenant_id

    @property
    def use_device_code_flow(self):
        """Gets the use_device_code_flow of this PublicAuthenticationConfiguration.  # noqa: E501

        Use device code flow for authentication  # noqa: E501

        :return: The use_device_code_flow of this PublicAuthenticationConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_device_code_flow

    @use_device_code_flow.setter
    def use_device_code_flow(self, use_device_code_flow):
        """Sets the use_device_code_flow of this PublicAuthenticationConfiguration.

        Use device code flow for authentication  # noqa: E501

        :param use_device_code_flow: The use_device_code_flow of this PublicAuthenticationConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_device_code_flow = use_device_code_flow

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
        if issubclass(PublicAuthenticationConfiguration, dict):
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
        if not isinstance(other, PublicAuthenticationConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAuthenticationConfiguration):
            return True

        return self.to_dict() != other.to_dict()
