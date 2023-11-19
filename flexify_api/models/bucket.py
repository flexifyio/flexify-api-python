# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.13.1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class Bucket(object):
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
        'display_name': 'str',
        'id': 'int',
        'name': 'str',
        'refresh_requested_time': 'datetime',
        'stat': 'BucketStat'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id',
        'name': 'name',
        'refresh_requested_time': 'refreshRequestedTime',
        'stat': 'stat'
    }

    def __init__(self, display_name=None, id=None, name=None, refresh_requested_time=None, stat=None, _configuration=None):  # noqa: E501
        """Bucket - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._id = None
        self._name = None
        self._refresh_requested_time = None
        self._stat = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        self.name = name
        if refresh_requested_time is not None:
            self.refresh_requested_time = refresh_requested_time
        if stat is not None:
            self.stat = stat

    @property
    def display_name(self):
        """Gets the display_name of this Bucket.  # noqa: E501

        Name to show in the UI when name is not heman-readable  # noqa: E501

        :return: The display_name of this Bucket.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Bucket.

        Name to show in the UI when name is not heman-readable  # noqa: E501

        :param display_name: The display_name of this Bucket.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this Bucket.  # noqa: E501

        Unique identifier if managed  # noqa: E501

        :return: The id of this Bucket.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bucket.

        Unique identifier if managed  # noqa: E501

        :param id: The id of this Bucket.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Bucket.  # noqa: E501

        Bucket, container or namespace name or another id  # noqa: E501

        :return: The name of this Bucket.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bucket.

        Bucket, container or namespace name or another id  # noqa: E501

        :param name: The name of this Bucket.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def refresh_requested_time(self):
        """Gets the refresh_requested_time of this Bucket.  # noqa: E501

        Last time refresh of this bucket was requested  # noqa: E501

        :return: The refresh_requested_time of this Bucket.  # noqa: E501
        :rtype: datetime
        """
        return self._refresh_requested_time

    @refresh_requested_time.setter
    def refresh_requested_time(self, refresh_requested_time):
        """Sets the refresh_requested_time of this Bucket.

        Last time refresh of this bucket was requested  # noqa: E501

        :param refresh_requested_time: The refresh_requested_time of this Bucket.  # noqa: E501
        :type: datetime
        """

        self._refresh_requested_time = refresh_requested_time

    @property
    def stat(self):
        """Gets the stat of this Bucket.  # noqa: E501

        Storage statistics  # noqa: E501

        :return: The stat of this Bucket.  # noqa: E501
        :rtype: BucketStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this Bucket.

        Storage statistics  # noqa: E501

        :param stat: The stat of this Bucket.  # noqa: E501
        :type: BucketStat
        """

        self._stat = stat

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
        if issubclass(Bucket, dict):
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
        if not isinstance(other, Bucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bucket):
            return True

        return self.to_dict() != other.to_dict()
