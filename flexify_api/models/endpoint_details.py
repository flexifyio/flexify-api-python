# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.4
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EndpointDetails(object):
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
        'accounts': 'list[EndpointStorageAccountRes]',
        'hostnames': 'list[str]',
        'id': 'int',
        'settings': 'EndpointSettings',
        'stat': 'EndpointStat',
        'virtual_buckets': 'list[VirtualBucket]'
    }

    attribute_map = {
        'accounts': 'accounts',
        'hostnames': 'hostnames',
        'id': 'id',
        'settings': 'settings',
        'stat': 'stat',
        'virtual_buckets': 'virtualBuckets'
    }

    def __init__(self, accounts=None, hostnames=None, id=None, settings=None, stat=None, virtual_buckets=None):  # noqa: E501
        """EndpointDetails - a model defined in Swagger"""  # noqa: E501

        self._accounts = None
        self._hostnames = None
        self._id = None
        self._settings = None
        self._stat = None
        self._virtual_buckets = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if hostnames is not None:
            self.hostnames = hostnames
        if id is not None:
            self.id = id
        self.settings = settings
        if stat is not None:
            self.stat = stat
        if virtual_buckets is not None:
            self.virtual_buckets = virtual_buckets

    @property
    def accounts(self):
        """Gets the accounts of this EndpointDetails.  # noqa: E501


        :return: The accounts of this EndpointDetails.  # noqa: E501
        :rtype: list[EndpointStorageAccountRes]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this EndpointDetails.


        :param accounts: The accounts of this EndpointDetails.  # noqa: E501
        :type: list[EndpointStorageAccountRes]
        """

        self._accounts = accounts

    @property
    def hostnames(self):
        """Gets the hostnames of this EndpointDetails.  # noqa: E501


        :return: The hostnames of this EndpointDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """Sets the hostnames of this EndpointDetails.


        :param hostnames: The hostnames of this EndpointDetails.  # noqa: E501
        :type: list[str]
        """

        self._hostnames = hostnames

    @property
    def id(self):
        """Gets the id of this EndpointDetails.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this EndpointDetails.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointDetails.

        Id  # noqa: E501

        :param id: The id of this EndpointDetails.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def settings(self):
        """Gets the settings of this EndpointDetails.  # noqa: E501

        Settings of endpoint  # noqa: E501

        :return: The settings of this EndpointDetails.  # noqa: E501
        :rtype: EndpointSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this EndpointDetails.

        Settings of endpoint  # noqa: E501

        :param settings: The settings of this EndpointDetails.  # noqa: E501
        :type: EndpointSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def stat(self):
        """Gets the stat of this EndpointDetails.  # noqa: E501


        :return: The stat of this EndpointDetails.  # noqa: E501
        :rtype: EndpointStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this EndpointDetails.


        :param stat: The stat of this EndpointDetails.  # noqa: E501
        :type: EndpointStat
        """

        self._stat = stat

    @property
    def virtual_buckets(self):
        """Gets the virtual_buckets of this EndpointDetails.  # noqa: E501


        :return: The virtual_buckets of this EndpointDetails.  # noqa: E501
        :rtype: list[VirtualBucket]
        """
        return self._virtual_buckets

    @virtual_buckets.setter
    def virtual_buckets(self, virtual_buckets):
        """Sets the virtual_buckets of this EndpointDetails.


        :param virtual_buckets: The virtual_buckets of this EndpointDetails.  # noqa: E501
        :type: list[VirtualBucket]
        """

        self._virtual_buckets = virtual_buckets

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
        if issubclass(EndpointDetails, dict):
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
        if not isinstance(other, EndpointDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
