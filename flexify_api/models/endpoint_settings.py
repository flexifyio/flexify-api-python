# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EndpointSettings(object):
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
        'protocol': 'str',
        'public_access_read_all_blobs': 'bool',
        'selection_break_timeout': 'int',
        'selection_policy': 'str'
    }

    attribute_map = {
        'credential': 'credential',
        'identity': 'identity',
        'protocol': 'protocol',
        'public_access_read_all_blobs': 'publicAccessReadAllBlobs',
        'selection_break_timeout': 'selectionBreakTimeout',
        'selection_policy': 'selectionPolicy'
    }

    def __init__(self, credential=None, identity=None, protocol=None, public_access_read_all_blobs=None, selection_break_timeout=None, selection_policy=None):  # noqa: E501
        """EndpointSettings - a model defined in Swagger"""  # noqa: E501

        self._credential = None
        self._identity = None
        self._protocol = None
        self._public_access_read_all_blobs = None
        self._selection_break_timeout = None
        self._selection_policy = None
        self.discriminator = None

        if credential is not None:
            self.credential = credential
        if identity is not None:
            self.identity = identity
        if protocol is not None:
            self.protocol = protocol
        if public_access_read_all_blobs is not None:
            self.public_access_read_all_blobs = public_access_read_all_blobs
        if selection_break_timeout is not None:
            self.selection_break_timeout = selection_break_timeout
        if selection_policy is not None:
            self.selection_policy = selection_policy

    @property
    def credential(self):
        """Gets the credential of this EndpointSettings.  # noqa: E501

        Storage Credential (Secret Key)  # noqa: E501

        :return: The credential of this EndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this EndpointSettings.

        Storage Credential (Secret Key)  # noqa: E501

        :param credential: The credential of this EndpointSettings.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def identity(self):
        """Gets the identity of this EndpointSettings.  # noqa: E501

        Storage Identity (Access Key)  # noqa: E501

        :return: The identity of this EndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this EndpointSettings.

        Storage Identity (Access Key)  # noqa: E501

        :param identity: The identity of this EndpointSettings.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def protocol(self):
        """Gets the protocol of this EndpointSettings.  # noqa: E501

        Storage Protocol  # noqa: E501

        :return: The protocol of this EndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this EndpointSettings.

        Storage Protocol  # noqa: E501

        :param protocol: The protocol of this EndpointSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "B2", "DROPBOX", "DROPBOX_TEAM", "S3"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def public_access_read_all_blobs(self):
        """Gets the public_access_read_all_blobs of this EndpointSettings.  # noqa: E501

        Public read access for all objects in virtual buckets  # noqa: E501

        :return: The public_access_read_all_blobs of this EndpointSettings.  # noqa: E501
        :rtype: bool
        """
        return self._public_access_read_all_blobs

    @public_access_read_all_blobs.setter
    def public_access_read_all_blobs(self, public_access_read_all_blobs):
        """Sets the public_access_read_all_blobs of this EndpointSettings.

        Public read access for all objects in virtual buckets  # noqa: E501

        :param public_access_read_all_blobs: The public_access_read_all_blobs of this EndpointSettings.  # noqa: E501
        :type: bool
        """

        self._public_access_read_all_blobs = public_access_read_all_blobs

    @property
    def selection_break_timeout(self):
        """Gets the selection_break_timeout of this EndpointSettings.  # noqa: E501

        Timeout before canceling rqeusts to non-responing clouds in FASTEST selection policy  # noqa: E501

        :return: The selection_break_timeout of this EndpointSettings.  # noqa: E501
        :rtype: int
        """
        return self._selection_break_timeout

    @selection_break_timeout.setter
    def selection_break_timeout(self, selection_break_timeout):
        """Sets the selection_break_timeout of this EndpointSettings.

        Timeout before canceling rqeusts to non-responing clouds in FASTEST selection policy  # noqa: E501

        :param selection_break_timeout: The selection_break_timeout of this EndpointSettings.  # noqa: E501
        :type: int
        """

        self._selection_break_timeout = selection_break_timeout

    @property
    def selection_policy(self):
        """Gets the selection_policy of this EndpointSettings.  # noqa: E501

        Storage selection policy for GET/HEAD object requests  # noqa: E501

        :return: The selection_policy of this EndpointSettings.  # noqa: E501
        :rtype: str
        """
        return self._selection_policy

    @selection_policy.setter
    def selection_policy(self, selection_policy):
        """Sets the selection_policy of this EndpointSettings.

        Storage selection policy for GET/HEAD object requests  # noqa: E501

        :param selection_policy: The selection_policy of this EndpointSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["FASTEST", "NEWEST"]  # noqa: E501
        if selection_policy not in allowed_values:
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
        if issubclass(EndpointSettings, dict):
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
        if not isinstance(other, EndpointSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
