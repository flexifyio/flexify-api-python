# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.17-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class EndpointSettingsReq(object):
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
        'credential': 'str',
        'identity': 'str',
        'name': 'str',
        'protocol': 'str',
        'selection_break_timeout': 'int',
        'selection_policy': 'str'
    }

    attribute_map = {
        'credential': 'credential',
        'identity': 'identity',
        'name': 'name',
        'protocol': 'protocol',
        'selection_break_timeout': 'selectionBreakTimeout',
        'selection_policy': 'selectionPolicy'
    }

    def __init__(self, credential=None, identity=None, name=None, protocol=None, selection_break_timeout=None, selection_policy=None, _configuration=None):  # noqa: E501
        """EndpointSettingsReq - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential = None
        self._identity = None
        self._name = None
        self._protocol = None
        self._selection_break_timeout = None
        self._selection_policy = None
        self.discriminator = None

        if credential is not None:
            self.credential = credential
        if identity is not None:
            self.identity = identity
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if selection_break_timeout is not None:
            self.selection_break_timeout = selection_break_timeout
        if selection_policy is not None:
            self.selection_policy = selection_policy

    @property
    def credential(self):
        """Gets the credential of this EndpointSettingsReq.  # noqa: E501

        Storage Credential (Secret Key)  # noqa: E501

        :return: The credential of this EndpointSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this EndpointSettingsReq.

        Storage Credential (Secret Key)  # noqa: E501

        :param credential: The credential of this EndpointSettingsReq.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def identity(self):
        """Gets the identity of this EndpointSettingsReq.  # noqa: E501

        Storage Identity (Access Key)  # noqa: E501

        :return: The identity of this EndpointSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this EndpointSettingsReq.

        Storage Identity (Access Key)  # noqa: E501

        :param identity: The identity of this EndpointSettingsReq.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def name(self):
        """Gets the name of this EndpointSettingsReq.  # noqa: E501

        User-define name of the endpoint  # noqa: E501

        :return: The name of this EndpointSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointSettingsReq.

        User-define name of the endpoint  # noqa: E501

        :param name: The name of this EndpointSettingsReq.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this EndpointSettingsReq.  # noqa: E501

        Storage Protocol  # noqa: E501

        :return: The protocol of this EndpointSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this EndpointSettingsReq.

        Storage Protocol  # noqa: E501

        :param protocol: The protocol of this EndpointSettingsReq.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "B2", "DROPBOX", "DROPBOX_TEAM", "S3"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def selection_break_timeout(self):
        """Gets the selection_break_timeout of this EndpointSettingsReq.  # noqa: E501

        Timeout before canceling requests to non-responding clouds in FASTEST selection policy  # noqa: E501

        :return: The selection_break_timeout of this EndpointSettingsReq.  # noqa: E501
        :rtype: int
        """
        return self._selection_break_timeout

    @selection_break_timeout.setter
    def selection_break_timeout(self, selection_break_timeout):
        """Sets the selection_break_timeout of this EndpointSettingsReq.

        Timeout before canceling requests to non-responding clouds in FASTEST selection policy  # noqa: E501

        :param selection_break_timeout: The selection_break_timeout of this EndpointSettingsReq.  # noqa: E501
        :type: int
        """

        self._selection_break_timeout = selection_break_timeout

    @property
    def selection_policy(self):
        """Gets the selection_policy of this EndpointSettingsReq.  # noqa: E501

        Storage selection policy for GET/HEAD object requests  # noqa: E501

        :return: The selection_policy of this EndpointSettingsReq.  # noqa: E501
        :rtype: str
        """
        return self._selection_policy

    @selection_policy.setter
    def selection_policy(self, selection_policy):
        """Sets the selection_policy of this EndpointSettingsReq.

        Storage selection policy for GET/HEAD object requests  # noqa: E501

        :param selection_policy: The selection_policy of this EndpointSettingsReq.  # noqa: E501
        :type: str
        """
        allowed_values = ["FASTEST", "NEWEST", "PRIORITY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                selection_policy not in allowed_values):
            raise ValueError(
                "Invalid value for `selection_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(selection_policy, allowed_values)
            )

        self._selection_policy = selection_policy

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
        if issubclass(EndpointSettingsReq, dict):
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
        if not isinstance(other, EndpointSettingsReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointSettingsReq):
            return True

        return self.to_dict() != other.to_dict()