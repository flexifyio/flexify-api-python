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


class SignupCodeRes(object):
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
        'roles': 'list[str]',
        'single_use': 'bool',
        'stat': 'SignupCodeStat'
    }

    attribute_map = {
        'code': 'code',
        'roles': 'roles',
        'single_use': 'singleUse',
        'stat': 'stat'
    }

    def __init__(self, code=None, roles=None, single_use=None, stat=None, _configuration=None):  # noqa: E501
        """SignupCodeRes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._roles = None
        self._single_use = None
        self._stat = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if roles is not None:
            self.roles = roles
        if single_use is not None:
            self.single_use = single_use
        if stat is not None:
            self.stat = stat

    @property
    def code(self):
        """Gets the code of this SignupCodeRes.  # noqa: E501


        :return: The code of this SignupCodeRes.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SignupCodeRes.


        :param code: The code of this SignupCodeRes.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def roles(self):
        """Gets the roles of this SignupCodeRes.  # noqa: E501


        :return: The roles of this SignupCodeRes.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this SignupCodeRes.


        :param roles: The roles of this SignupCodeRes.  # noqa: E501
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

    @property
    def single_use(self):
        """Gets the single_use of this SignupCodeRes.  # noqa: E501


        :return: The single_use of this SignupCodeRes.  # noqa: E501
        :rtype: bool
        """
        return self._single_use

    @single_use.setter
    def single_use(self, single_use):
        """Sets the single_use of this SignupCodeRes.


        :param single_use: The single_use of this SignupCodeRes.  # noqa: E501
        :type: bool
        """

        self._single_use = single_use

    @property
    def stat(self):
        """Gets the stat of this SignupCodeRes.  # noqa: E501


        :return: The stat of this SignupCodeRes.  # noqa: E501
        :rtype: SignupCodeStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this SignupCodeRes.


        :param stat: The stat of this SignupCodeRes.  # noqa: E501
        :type: SignupCodeStat
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
        if issubclass(SignupCodeRes, dict):
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
        if not isinstance(other, SignupCodeRes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignupCodeRes):
            return True

        return self.to_dict() != other.to_dict()
