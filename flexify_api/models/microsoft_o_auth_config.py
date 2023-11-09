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


class MicrosoftOAuthConfig(object):
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
        'auth_url': 'str',
        'client_id': 'str',
        'scope': 'str',
        'tenant_id': 'str',
        'use_device_code_flow': 'bool'
    }

    attribute_map = {
        'auth_url': 'authUrl',
        'client_id': 'clientId',
        'scope': 'scope',
        'tenant_id': 'tenantId',
        'use_device_code_flow': 'useDeviceCodeFlow'
    }

    def __init__(self, auth_url=None, client_id=None, scope=None, tenant_id=None, use_device_code_flow=None, _configuration=None):  # noqa: E501
        """MicrosoftOAuthConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_url = None
        self._client_id = None
        self._scope = None
        self._tenant_id = None
        self._use_device_code_flow = None
        self.discriminator = None

        if auth_url is not None:
            self.auth_url = auth_url
        if client_id is not None:
            self.client_id = client_id
        if scope is not None:
            self.scope = scope
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if use_device_code_flow is not None:
            self.use_device_code_flow = use_device_code_flow

    @property
    def auth_url(self):
        """Gets the auth_url of this MicrosoftOAuthConfig.  # noqa: E501


        :return: The auth_url of this MicrosoftOAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this MicrosoftOAuthConfig.


        :param auth_url: The auth_url of this MicrosoftOAuthConfig.  # noqa: E501
        :type: str
        """

        self._auth_url = auth_url

    @property
    def client_id(self):
        """Gets the client_id of this MicrosoftOAuthConfig.  # noqa: E501


        :return: The client_id of this MicrosoftOAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this MicrosoftOAuthConfig.


        :param client_id: The client_id of this MicrosoftOAuthConfig.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def scope(self):
        """Gets the scope of this MicrosoftOAuthConfig.  # noqa: E501


        :return: The scope of this MicrosoftOAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this MicrosoftOAuthConfig.


        :param scope: The scope of this MicrosoftOAuthConfig.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def tenant_id(self):
        """Gets the tenant_id of this MicrosoftOAuthConfig.  # noqa: E501


        :return: The tenant_id of this MicrosoftOAuthConfig.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this MicrosoftOAuthConfig.


        :param tenant_id: The tenant_id of this MicrosoftOAuthConfig.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def use_device_code_flow(self):
        """Gets the use_device_code_flow of this MicrosoftOAuthConfig.  # noqa: E501


        :return: The use_device_code_flow of this MicrosoftOAuthConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_device_code_flow

    @use_device_code_flow.setter
    def use_device_code_flow(self, use_device_code_flow):
        """Sets the use_device_code_flow of this MicrosoftOAuthConfig.


        :param use_device_code_flow: The use_device_code_flow of this MicrosoftOAuthConfig.  # noqa: E501
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
        if issubclass(MicrosoftOAuthConfig, dict):
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
        if not isinstance(other, MicrosoftOAuthConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MicrosoftOAuthConfig):
            return True

        return self.to_dict() != other.to_dict()
