# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.10.hf4
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Pageable(object):
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
        'offset': 'int',
        'page_number': 'int',
        'page_size': 'int',
        'paged': 'bool',
        'sort': 'Sort',
        'unpaged': 'bool'
    }

    attribute_map = {
        'offset': 'offset',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'paged': 'paged',
        'sort': 'sort',
        'unpaged': 'unpaged'
    }

    def __init__(self, offset=None, page_number=None, page_size=None, paged=None, sort=None, unpaged=None):  # noqa: E501
        """Pageable - a model defined in Swagger"""  # noqa: E501

        self._offset = None
        self._page_number = None
        self._page_size = None
        self._paged = None
        self._sort = None
        self._unpaged = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if paged is not None:
            self.paged = paged
        if sort is not None:
            self.sort = sort
        if unpaged is not None:
            self.unpaged = unpaged

    @property
    def offset(self):
        """Gets the offset of this Pageable.  # noqa: E501


        :return: The offset of this Pageable.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Pageable.


        :param offset: The offset of this Pageable.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def page_number(self):
        """Gets the page_number of this Pageable.  # noqa: E501


        :return: The page_number of this Pageable.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this Pageable.


        :param page_number: The page_number of this Pageable.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this Pageable.  # noqa: E501


        :return: The page_size of this Pageable.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this Pageable.


        :param page_size: The page_size of this Pageable.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def paged(self):
        """Gets the paged of this Pageable.  # noqa: E501


        :return: The paged of this Pageable.  # noqa: E501
        :rtype: bool
        """
        return self._paged

    @paged.setter
    def paged(self, paged):
        """Sets the paged of this Pageable.


        :param paged: The paged of this Pageable.  # noqa: E501
        :type: bool
        """

        self._paged = paged

    @property
    def sort(self):
        """Gets the sort of this Pageable.  # noqa: E501


        :return: The sort of this Pageable.  # noqa: E501
        :rtype: Sort
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this Pageable.


        :param sort: The sort of this Pageable.  # noqa: E501
        :type: Sort
        """

        self._sort = sort

    @property
    def unpaged(self):
        """Gets the unpaged of this Pageable.  # noqa: E501


        :return: The unpaged of this Pageable.  # noqa: E501
        :rtype: bool
        """
        return self._unpaged

    @unpaged.setter
    def unpaged(self, unpaged):
        """Sets the unpaged of this Pageable.


        :param unpaged: The unpaged of this Pageable.  # noqa: E501
        :type: bool
        """

        self._unpaged = unpaged

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
        if issubclass(Pageable, dict):
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
        if not isinstance(other, Pageable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
