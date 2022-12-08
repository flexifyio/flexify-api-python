# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.12-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class UserSettings(object):
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
        'allow_partner_manage': 'bool',
        'send_news': 'bool',
        'send_notifications': 'bool'
    }

    attribute_map = {
        'allow_partner_manage': 'allowPartnerManage',
        'send_news': 'sendNews',
        'send_notifications': 'sendNotifications'
    }

    def __init__(self, allow_partner_manage=None, send_news=None, send_notifications=None, _configuration=None):  # noqa: E501
        """UserSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_partner_manage = None
        self._send_news = None
        self._send_notifications = None
        self.discriminator = None

        if allow_partner_manage is not None:
            self.allow_partner_manage = allow_partner_manage
        if send_news is not None:
            self.send_news = send_news
        if send_notifications is not None:
            self.send_notifications = send_notifications

    @property
    def allow_partner_manage(self):
        """Gets the allow_partner_manage of this UserSettings.  # noqa: E501

        Indicates that the user allowed his or her partner to impersonate and manage user's account  # noqa: E501

        :return: The allow_partner_manage of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_partner_manage

    @allow_partner_manage.setter
    def allow_partner_manage(self, allow_partner_manage):
        """Sets the allow_partner_manage of this UserSettings.

        Indicates that the user allowed his or her partner to impersonate and manage user's account  # noqa: E501

        :param allow_partner_manage: The allow_partner_manage of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._allow_partner_manage = allow_partner_manage

    @property
    def send_news(self):
        """Gets the send_news of this UserSettings.  # noqa: E501

        Indicates tha the user agreed to receive news and updates  # noqa: E501

        :return: The send_news of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._send_news

    @send_news.setter
    def send_news(self, send_news):
        """Sets the send_news of this UserSettings.

        Indicates tha the user agreed to receive news and updates  # noqa: E501

        :param send_news: The send_news of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._send_news = send_news

    @property
    def send_notifications(self):
        """Gets the send_notifications of this UserSettings.  # noqa: E501

        Indicates that we should send system notifications to the user  # noqa: E501

        :return: The send_notifications of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._send_notifications

    @send_notifications.setter
    def send_notifications(self, send_notifications):
        """Sets the send_notifications of this UserSettings.

        Indicates that we should send system notifications to the user  # noqa: E501

        :param send_notifications: The send_notifications of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._send_notifications = send_notifications

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
        if issubclass(UserSettings, dict):
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
        if not isinstance(other, UserSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSettings):
            return True

        return self.to_dict() != other.to_dict()
