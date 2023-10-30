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


class AddMigrationRequest(object):
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
        'mappings': 'list[AddMigrationRequestMapping]',
        'settings': 'MigrationSettingsReq',
        'verify_buckets': 'bool'
    }

    attribute_map = {
        'mappings': 'mappings',
        'settings': 'settings',
        'verify_buckets': 'verifyBuckets'
    }

    def __init__(self, mappings=None, settings=None, verify_buckets=None, _configuration=None):  # noqa: E501
        """AddMigrationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mappings = None
        self._settings = None
        self._verify_buckets = None
        self.discriminator = None

        if mappings is not None:
            self.mappings = mappings
        if settings is not None:
            self.settings = settings
        if verify_buckets is not None:
            self.verify_buckets = verify_buckets

    @property
    def mappings(self):
        """Gets the mappings of this AddMigrationRequest.  # noqa: E501

        Source storage to destination account/bucket mapping  # noqa: E501

        :return: The mappings of this AddMigrationRequest.  # noqa: E501
        :rtype: list[AddMigrationRequestMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this AddMigrationRequest.

        Source storage to destination account/bucket mapping  # noqa: E501

        :param mappings: The mappings of this AddMigrationRequest.  # noqa: E501
        :type: list[AddMigrationRequestMapping]
        """

        self._mappings = mappings

    @property
    def settings(self):
        """Gets the settings of this AddMigrationRequest.  # noqa: E501

        Migration settings  # noqa: E501

        :return: The settings of this AddMigrationRequest.  # noqa: E501
        :rtype: MigrationSettingsReq
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AddMigrationRequest.

        Migration settings  # noqa: E501

        :param settings: The settings of this AddMigrationRequest.  # noqa: E501
        :type: MigrationSettingsReq
        """

        self._settings = settings

    @property
    def verify_buckets(self):
        """Gets the verify_buckets of this AddMigrationRequest.  # noqa: E501

        If buckets should be verified by HEAD request  # noqa: E501

        :return: The verify_buckets of this AddMigrationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._verify_buckets

    @verify_buckets.setter
    def verify_buckets(self, verify_buckets):
        """Sets the verify_buckets of this AddMigrationRequest.

        If buckets should be verified by HEAD request  # noqa: E501

        :param verify_buckets: The verify_buckets of this AddMigrationRequest.  # noqa: E501
        :type: bool
        """

        self._verify_buckets = verify_buckets

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
        if issubclass(AddMigrationRequest, dict):
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
        if not isinstance(other, AddMigrationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddMigrationRequest):
            return True

        return self.to_dict() != other.to_dict()
