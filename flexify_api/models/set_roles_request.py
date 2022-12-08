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


class SetRolesRequest(object):
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
        'roles': 'list[str]'
    }

    attribute_map = {
        'roles': 'roles'
    }

    def __init__(self, roles=None, _configuration=None):  # noqa: E501
        """SetRolesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._roles = None
        self.discriminator = None

        if roles is not None:
            self.roles = roles

    @property
    def roles(self):
        """Gets the roles of this SetRolesRequest.  # noqa: E501


        :return: The roles of this SetRolesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this SetRolesRequest.


        :param roles: The roles of this SetRolesRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ROLE_ACTUATOR", "ROLE_ADMIN", "ROLE_BILLING", "ROLE_DISTRIBUTOR", "ROLE_IMPERSONATOR", "ROLE_PARTNER_ADMIN", "ROLE_USER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(roles).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

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
        if issubclass(SetRolesRequest, dict):
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
        if not isinstance(other, SetRolesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetRolesRequest):
            return True

        return self.to_dict() != other.to_dict()
