# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class FinishOAuthParams(object):
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
        'code': 'str',
        'flow': 'str',
        'oauth_provider_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'flow': 'flow',
        'oauth_provider_id': 'oauthProviderId'
    }

    def __init__(self, code=None, flow=None, oauth_provider_id=None, _configuration=None):  # noqa: E501
        """FinishOAuthParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._flow = None
        self._oauth_provider_id = None
        self.discriminator = None

        self.code = code
        self.flow = flow
        self.oauth_provider_id = oauth_provider_id

    @property
    def code(self):
        """Gets the code of this FinishOAuthParams.  # noqa: E501


        :return: The code of this FinishOAuthParams.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FinishOAuthParams.


        :param code: The code of this FinishOAuthParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def flow(self):
        """Gets the flow of this FinishOAuthParams.  # noqa: E501


        :return: The flow of this FinishOAuthParams.  # noqa: E501
        :rtype: str
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this FinishOAuthParams.


        :param flow: The flow of this FinishOAuthParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and flow is None:
            raise ValueError("Invalid value for `flow`, must not be `None`")  # noqa: E501
        allowed_values = ["AUTH_CODE", "DEVICE_CODE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                flow not in allowed_values):
            raise ValueError(
                "Invalid value for `flow` ({0}), must be one of {1}"  # noqa: E501
                .format(flow, allowed_values)
            )

        self._flow = flow

    @property
    def oauth_provider_id(self):
        """Gets the oauth_provider_id of this FinishOAuthParams.  # noqa: E501


        :return: The oauth_provider_id of this FinishOAuthParams.  # noqa: E501
        :rtype: str
        """
        return self._oauth_provider_id

    @oauth_provider_id.setter
    def oauth_provider_id(self, oauth_provider_id):
        """Sets the oauth_provider_id of this FinishOAuthParams.


        :param oauth_provider_id: The oauth_provider_id of this FinishOAuthParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and oauth_provider_id is None:
            raise ValueError("Invalid value for `oauth_provider_id`, must not be `None`")  # noqa: E501
        allowed_values = ["DROPBOX", "DROPBOX_TEAM", "MICROSOFT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                oauth_provider_id not in allowed_values):
            raise ValueError(
                "Invalid value for `oauth_provider_id` ({0}), must be one of {1}"  # noqa: E501
                .format(oauth_provider_id, allowed_values)
            )

        self._oauth_provider_id = oauth_provider_id

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
        if issubclass(FinishOAuthParams, dict):
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
        if not isinstance(other, FinishOAuthParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FinishOAuthParams):
            return True

        return self.to_dict() != other.to_dict()
