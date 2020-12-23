# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.1-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EndpointStat(object):
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
        'cloud_download_bytes': 'int',
        'cloud_upload_bytes': 'int',
        'error_engines': 'int',
        'health': 'str',
        'state': 'str',
        'total_engines': 'int',
        'up_to_date_engines': 'int',
        'user_download_bytes': 'int',
        'user_speed_download': 'int',
        'user_speed_upload': 'int',
        'user_upload_bytes': 'int',
        'warning_engines': 'int'
    }

    attribute_map = {
        'cloud_download_bytes': 'cloudDownloadBytes',
        'cloud_upload_bytes': 'cloudUploadBytes',
        'error_engines': 'errorEngines',
        'health': 'health',
        'state': 'state',
        'total_engines': 'totalEngines',
        'up_to_date_engines': 'upToDateEngines',
        'user_download_bytes': 'userDownloadBytes',
        'user_speed_download': 'userSpeedDownload',
        'user_speed_upload': 'userSpeedUpload',
        'user_upload_bytes': 'userUploadBytes',
        'warning_engines': 'warningEngines'
    }

    def __init__(self, cloud_download_bytes=None, cloud_upload_bytes=None, error_engines=None, health=None, state=None, total_engines=None, up_to_date_engines=None, user_download_bytes=None, user_speed_download=None, user_speed_upload=None, user_upload_bytes=None, warning_engines=None):  # noqa: E501
        """EndpointStat - a model defined in Swagger"""  # noqa: E501

        self._cloud_download_bytes = None
        self._cloud_upload_bytes = None
        self._error_engines = None
        self._health = None
        self._state = None
        self._total_engines = None
        self._up_to_date_engines = None
        self._user_download_bytes = None
        self._user_speed_download = None
        self._user_speed_upload = None
        self._user_upload_bytes = None
        self._warning_engines = None
        self.discriminator = None

        if cloud_download_bytes is not None:
            self.cloud_download_bytes = cloud_download_bytes
        if cloud_upload_bytes is not None:
            self.cloud_upload_bytes = cloud_upload_bytes
        if error_engines is not None:
            self.error_engines = error_engines
        if health is not None:
            self.health = health
        if state is not None:
            self.state = state
        if total_engines is not None:
            self.total_engines = total_engines
        if up_to_date_engines is not None:
            self.up_to_date_engines = up_to_date_engines
        if user_download_bytes is not None:
            self.user_download_bytes = user_download_bytes
        if user_speed_download is not None:
            self.user_speed_download = user_speed_download
        if user_speed_upload is not None:
            self.user_speed_upload = user_speed_upload
        if user_upload_bytes is not None:
            self.user_upload_bytes = user_upload_bytes
        if warning_engines is not None:
            self.warning_engines = warning_engines

    @property
    def cloud_download_bytes(self):
        """Gets the cloud_download_bytes of this EndpointStat.  # noqa: E501


        :return: The cloud_download_bytes of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._cloud_download_bytes

    @cloud_download_bytes.setter
    def cloud_download_bytes(self, cloud_download_bytes):
        """Sets the cloud_download_bytes of this EndpointStat.


        :param cloud_download_bytes: The cloud_download_bytes of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._cloud_download_bytes = cloud_download_bytes

    @property
    def cloud_upload_bytes(self):
        """Gets the cloud_upload_bytes of this EndpointStat.  # noqa: E501


        :return: The cloud_upload_bytes of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._cloud_upload_bytes

    @cloud_upload_bytes.setter
    def cloud_upload_bytes(self, cloud_upload_bytes):
        """Sets the cloud_upload_bytes of this EndpointStat.


        :param cloud_upload_bytes: The cloud_upload_bytes of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._cloud_upload_bytes = cloud_upload_bytes

    @property
    def error_engines(self):
        """Gets the error_engines of this EndpointStat.  # noqa: E501


        :return: The error_engines of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._error_engines

    @error_engines.setter
    def error_engines(self, error_engines):
        """Sets the error_engines of this EndpointStat.


        :param error_engines: The error_engines of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._error_engines = error_engines

    @property
    def health(self):
        """Gets the health of this EndpointStat.  # noqa: E501


        :return: The health of this EndpointStat.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this EndpointStat.


        :param health: The health of this EndpointStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "HEALTHY", "WARNING"]  # noqa: E501
        if health not in allowed_values:
            raise ValueError(
                "Invalid value for `health` ({0}), must be one of {1}"  # noqa: E501
                .format(health, allowed_values)
            )

        self._health = health

    @property
    def state(self):
        """Gets the state of this EndpointStat.  # noqa: E501


        :return: The state of this EndpointStat.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EndpointStat.


        :param state: The state of this EndpointStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETING", "DISABLED", "DISABLING", "ENABLED", "ENABLING", "ERROR", "NOT_ASSIGNED", "UPDATING", "WARNING"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def total_engines(self):
        """Gets the total_engines of this EndpointStat.  # noqa: E501


        :return: The total_engines of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._total_engines

    @total_engines.setter
    def total_engines(self, total_engines):
        """Sets the total_engines of this EndpointStat.


        :param total_engines: The total_engines of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._total_engines = total_engines

    @property
    def up_to_date_engines(self):
        """Gets the up_to_date_engines of this EndpointStat.  # noqa: E501


        :return: The up_to_date_engines of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._up_to_date_engines

    @up_to_date_engines.setter
    def up_to_date_engines(self, up_to_date_engines):
        """Sets the up_to_date_engines of this EndpointStat.


        :param up_to_date_engines: The up_to_date_engines of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._up_to_date_engines = up_to_date_engines

    @property
    def user_download_bytes(self):
        """Gets the user_download_bytes of this EndpointStat.  # noqa: E501


        :return: The user_download_bytes of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._user_download_bytes

    @user_download_bytes.setter
    def user_download_bytes(self, user_download_bytes):
        """Sets the user_download_bytes of this EndpointStat.


        :param user_download_bytes: The user_download_bytes of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._user_download_bytes = user_download_bytes

    @property
    def user_speed_download(self):
        """Gets the user_speed_download of this EndpointStat.  # noqa: E501


        :return: The user_speed_download of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._user_speed_download

    @user_speed_download.setter
    def user_speed_download(self, user_speed_download):
        """Sets the user_speed_download of this EndpointStat.


        :param user_speed_download: The user_speed_download of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._user_speed_download = user_speed_download

    @property
    def user_speed_upload(self):
        """Gets the user_speed_upload of this EndpointStat.  # noqa: E501


        :return: The user_speed_upload of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._user_speed_upload

    @user_speed_upload.setter
    def user_speed_upload(self, user_speed_upload):
        """Sets the user_speed_upload of this EndpointStat.


        :param user_speed_upload: The user_speed_upload of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._user_speed_upload = user_speed_upload

    @property
    def user_upload_bytes(self):
        """Gets the user_upload_bytes of this EndpointStat.  # noqa: E501


        :return: The user_upload_bytes of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._user_upload_bytes

    @user_upload_bytes.setter
    def user_upload_bytes(self, user_upload_bytes):
        """Sets the user_upload_bytes of this EndpointStat.


        :param user_upload_bytes: The user_upload_bytes of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._user_upload_bytes = user_upload_bytes

    @property
    def warning_engines(self):
        """Gets the warning_engines of this EndpointStat.  # noqa: E501


        :return: The warning_engines of this EndpointStat.  # noqa: E501
        :rtype: int
        """
        return self._warning_engines

    @warning_engines.setter
    def warning_engines(self, warning_engines):
        """Sets the warning_engines of this EndpointStat.


        :param warning_engines: The warning_engines of this EndpointStat.  # noqa: E501
        :type: int
        """

        self._warning_engines = warning_engines

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
        if issubclass(EndpointStat, dict):
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
        if not isinstance(other, EndpointStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
