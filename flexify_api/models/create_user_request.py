# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.18.hf1
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class CreateUserRequest(object):
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
        'external_id': 'str',
        'org_id': 'int',
        'price_list_id': 'int',
        'profile': 'UserProfile'
    }

    attribute_map = {
        'external_id': 'externalId',
        'org_id': 'orgId',
        'price_list_id': 'priceListId',
        'profile': 'profile'
    }

    def __init__(self, external_id=None, org_id=None, price_list_id=None, profile=None, _configuration=None):  # noqa: E501
        """CreateUserRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_id = None
        self._org_id = None
        self._price_list_id = None
        self._profile = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        if org_id is not None:
            self.org_id = org_id
        if price_list_id is not None:
            self.price_list_id = price_list_id
        self.profile = profile

    @property
    def external_id(self):
        """Gets the external_id of this CreateUserRequest.  # noqa: E501

        An optional external ID that can be later used to reference this user  # noqa: E501

        :return: The external_id of this CreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateUserRequest.

        An optional external ID that can be later used to reference this user  # noqa: E501

        :param external_id: The external_id of this CreateUserRequest.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def org_id(self):
        """Gets the org_id of this CreateUserRequest.  # noqa: E501

        ID of the organization to assign the user to (or default otherwise)  # noqa: E501

        :return: The org_id of this CreateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CreateUserRequest.

        ID of the organization to assign the user to (or default otherwise)  # noqa: E501

        :param org_id: The org_id of this CreateUserRequest.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def price_list_id(self):
        """Gets the price_list_id of this CreateUserRequest.  # noqa: E501

        ID of the price list to assign to this user (or default otherwise)  # noqa: E501

        :return: The price_list_id of this CreateUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._price_list_id

    @price_list_id.setter
    def price_list_id(self, price_list_id):
        """Sets the price_list_id of this CreateUserRequest.

        ID of the price list to assign to this user (or default otherwise)  # noqa: E501

        :param price_list_id: The price_list_id of this CreateUserRequest.  # noqa: E501
        :type: int
        """

        self._price_list_id = price_list_id

    @property
    def profile(self):
        """Gets the profile of this CreateUserRequest.  # noqa: E501

        New user's profile containing basic information about the user  # noqa: E501

        :return: The profile of this CreateUserRequest.  # noqa: E501
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this CreateUserRequest.

        New user's profile containing basic information about the user  # noqa: E501

        :param profile: The profile of this CreateUserRequest.  # noqa: E501
        :type: UserProfile
        """
        if self._configuration.client_side_validation and profile is None:
            raise ValueError("Invalid value for `profile`, must not be `None`")  # noqa: E501

        self._profile = profile

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
        if issubclass(CreateUserRequest, dict):
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
        if not isinstance(other, CreateUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUserRequest):
            return True

        return self.to_dict() != other.to_dict()
