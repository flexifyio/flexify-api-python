# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.14.0
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class UserProfile(object):
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
        'city': 'str',
        'company': 'str',
        'country': 'str',
        'display_name': 'str',
        'email': 'str',
        'phone': 'str',
        'street_first_line': 'str',
        'street_second_line': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'city': 'city',
        'company': 'company',
        'country': 'country',
        'display_name': 'displayName',
        'email': 'email',
        'phone': 'phone',
        'street_first_line': 'streetFirstLine',
        'street_second_line': 'streetSecondLine',
        'zip': 'zip'
    }

    def __init__(self, city=None, company=None, country=None, display_name=None, email=None, phone=None, street_first_line=None, street_second_line=None, zip=None, _configuration=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._city = None
        self._company = None
        self._country = None
        self._display_name = None
        self._email = None
        self._phone = None
        self._street_first_line = None
        self._street_second_line = None
        self._zip = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if company is not None:
            self.company = company
        if country is not None:
            self.country = country
        if display_name is not None:
            self.display_name = display_name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if street_first_line is not None:
            self.street_first_line = street_first_line
        if street_second_line is not None:
            self.street_second_line = street_second_line
        if zip is not None:
            self.zip = zip

    @property
    def city(self):
        """Gets the city of this UserProfile.  # noqa: E501

        City  # noqa: E501

        :return: The city of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this UserProfile.

        City  # noqa: E501

        :param city: The city of this UserProfile.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company(self):
        """Gets the company of this UserProfile.  # noqa: E501

        Company  # noqa: E501

        :return: The company of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UserProfile.

        Company  # noqa: E501

        :param company: The company of this UserProfile.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def country(self):
        """Gets the country of this UserProfile.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserProfile.

        Country  # noqa: E501

        :param country: The country of this UserProfile.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def display_name(self):
        """Gets the display_name of this UserProfile.  # noqa: E501

        Display name (usually first and last name)  # noqa: E501

        :return: The display_name of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserProfile.

        Display name (usually first and last name)  # noqa: E501

        :param display_name: The display_name of this UserProfile.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this UserProfile.  # noqa: E501

        Email address, always matches the username  # noqa: E501

        :return: The email of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfile.

        Email address, always matches the username  # noqa: E501

        :param email: The email of this UserProfile.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this UserProfile.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserProfile.

        Phone number  # noqa: E501

        :param phone: The phone of this UserProfile.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def street_first_line(self):
        """Gets the street_first_line of this UserProfile.  # noqa: E501

        Street address - first line  # noqa: E501

        :return: The street_first_line of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._street_first_line

    @street_first_line.setter
    def street_first_line(self, street_first_line):
        """Sets the street_first_line of this UserProfile.

        Street address - first line  # noqa: E501

        :param street_first_line: The street_first_line of this UserProfile.  # noqa: E501
        :type: str
        """

        self._street_first_line = street_first_line

    @property
    def street_second_line(self):
        """Gets the street_second_line of this UserProfile.  # noqa: E501

        Street address - second line  # noqa: E501

        :return: The street_second_line of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._street_second_line

    @street_second_line.setter
    def street_second_line(self, street_second_line):
        """Sets the street_second_line of this UserProfile.

        Street address - second line  # noqa: E501

        :param street_second_line: The street_second_line of this UserProfile.  # noqa: E501
        :type: str
        """

        self._street_second_line = street_second_line

    @property
    def zip(self):
        """Gets the zip of this UserProfile.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this UserProfile.

        Zip code  # noqa: E501

        :param zip: The zip of this UserProfile.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProfile):
            return True

        return self.to_dict() != other.to_dict()
