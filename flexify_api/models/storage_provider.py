# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.19-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class StorageProvider(object):
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
        'bucket_dot_encode': 'bool',
        'can_create_buckets_with_uppercase': 'bool',
        'code': 'str',
        'default_region': 'str',
        'disabled_as_destination': 'bool',
        'endpoint': 'str',
        'endpoint_pattern': 'str',
        'id': 'int',
        'max_upload_size': 'int',
        'multi_regional': 'bool',
        'name': 'str',
        'port_http': 'int',
        'port_https': 'int',
        'private_endpoint': 'str',
        'private_endpoint_pattern': 'str',
        'product_name': 'str',
        'protocol': 'str',
        'supports_credential': 'bool',
        'supports_http': 'bool',
        'supports_https': 'bool',
        'supports_multipart_upload': 'bool',
        'supports_o_auth': 'bool',
        'supports_o_auth_name': 'str'
    }

    attribute_map = {
        'bucket_dot_encode': 'bucketDotEncode',
        'can_create_buckets_with_uppercase': 'canCreateBucketsWithUppercase',
        'code': 'code',
        'default_region': 'defaultRegion',
        'disabled_as_destination': 'disabledAsDestination',
        'endpoint': 'endpoint',
        'endpoint_pattern': 'endpointPattern',
        'id': 'id',
        'max_upload_size': 'maxUploadSize',
        'multi_regional': 'multiRegional',
        'name': 'name',
        'port_http': 'portHttp',
        'port_https': 'portHttps',
        'private_endpoint': 'privateEndpoint',
        'private_endpoint_pattern': 'privateEndpointPattern',
        'product_name': 'productName',
        'protocol': 'protocol',
        'supports_credential': 'supportsCredential',
        'supports_http': 'supportsHttp',
        'supports_https': 'supportsHttps',
        'supports_multipart_upload': 'supportsMultipartUpload',
        'supports_o_auth': 'supportsOAuth',
        'supports_o_auth_name': 'supportsOAuthName'
    }

    def __init__(self, bucket_dot_encode=None, can_create_buckets_with_uppercase=None, code=None, default_region=None, disabled_as_destination=None, endpoint=None, endpoint_pattern=None, id=None, max_upload_size=None, multi_regional=None, name=None, port_http=None, port_https=None, private_endpoint=None, private_endpoint_pattern=None, product_name=None, protocol=None, supports_credential=None, supports_http=None, supports_https=None, supports_multipart_upload=None, supports_o_auth=None, supports_o_auth_name=None, _configuration=None):  # noqa: E501
        """StorageProvider - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_dot_encode = None
        self._can_create_buckets_with_uppercase = None
        self._code = None
        self._default_region = None
        self._disabled_as_destination = None
        self._endpoint = None
        self._endpoint_pattern = None
        self._id = None
        self._max_upload_size = None
        self._multi_regional = None
        self._name = None
        self._port_http = None
        self._port_https = None
        self._private_endpoint = None
        self._private_endpoint_pattern = None
        self._product_name = None
        self._protocol = None
        self._supports_credential = None
        self._supports_http = None
        self._supports_https = None
        self._supports_multipart_upload = None
        self._supports_o_auth = None
        self._supports_o_auth_name = None
        self.discriminator = None

        if bucket_dot_encode is not None:
            self.bucket_dot_encode = bucket_dot_encode
        if can_create_buckets_with_uppercase is not None:
            self.can_create_buckets_with_uppercase = can_create_buckets_with_uppercase
        if code is not None:
            self.code = code
        if default_region is not None:
            self.default_region = default_region
        if disabled_as_destination is not None:
            self.disabled_as_destination = disabled_as_destination
        if endpoint is not None:
            self.endpoint = endpoint
        if endpoint_pattern is not None:
            self.endpoint_pattern = endpoint_pattern
        if id is not None:
            self.id = id
        if max_upload_size is not None:
            self.max_upload_size = max_upload_size
        if multi_regional is not None:
            self.multi_regional = multi_regional
        if name is not None:
            self.name = name
        if port_http is not None:
            self.port_http = port_http
        if port_https is not None:
            self.port_https = port_https
        if private_endpoint is not None:
            self.private_endpoint = private_endpoint
        if private_endpoint_pattern is not None:
            self.private_endpoint_pattern = private_endpoint_pattern
        if product_name is not None:
            self.product_name = product_name
        if protocol is not None:
            self.protocol = protocol
        if supports_credential is not None:
            self.supports_credential = supports_credential
        if supports_http is not None:
            self.supports_http = supports_http
        if supports_https is not None:
            self.supports_https = supports_https
        if supports_multipart_upload is not None:
            self.supports_multipart_upload = supports_multipart_upload
        if supports_o_auth is not None:
            self.supports_o_auth = supports_o_auth
        if supports_o_auth_name is not None:
            self.supports_o_auth_name = supports_o_auth_name

    @property
    def bucket_dot_encode(self):
        """Gets the bucket_dot_encode of this StorageProvider.  # noqa: E501

        Indicates that the provider does not support dots in bucket names and how dots should be encoded  # noqa: E501

        :return: The bucket_dot_encode of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._bucket_dot_encode

    @bucket_dot_encode.setter
    def bucket_dot_encode(self, bucket_dot_encode):
        """Sets the bucket_dot_encode of this StorageProvider.

        Indicates that the provider does not support dots in bucket names and how dots should be encoded  # noqa: E501

        :param bucket_dot_encode: The bucket_dot_encode of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._bucket_dot_encode = bucket_dot_encode

    @property
    def can_create_buckets_with_uppercase(self):
        """Gets the can_create_buckets_with_uppercase of this StorageProvider.  # noqa: E501

        Indicates that this provider allow creating bucket with uppercase in names  # noqa: E501

        :return: The can_create_buckets_with_uppercase of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_buckets_with_uppercase

    @can_create_buckets_with_uppercase.setter
    def can_create_buckets_with_uppercase(self, can_create_buckets_with_uppercase):
        """Sets the can_create_buckets_with_uppercase of this StorageProvider.

        Indicates that this provider allow creating bucket with uppercase in names  # noqa: E501

        :param can_create_buckets_with_uppercase: The can_create_buckets_with_uppercase of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._can_create_buckets_with_uppercase = can_create_buckets_with_uppercase

    @property
    def code(self):
        """Gets the code of this StorageProvider.  # noqa: E501

        Code of this cloud provider  # noqa: E501

        :return: The code of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StorageProvider.

        Code of this cloud provider  # noqa: E501

        :param code: The code of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def default_region(self):
        """Gets the default_region of this StorageProvider.  # noqa: E501

        Default region for this provider  # noqa: E501

        :return: The default_region of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._default_region

    @default_region.setter
    def default_region(self, default_region):
        """Sets the default_region of this StorageProvider.

        Default region for this provider  # noqa: E501

        :param default_region: The default_region of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._default_region = default_region

    @property
    def disabled_as_destination(self):
        """Gets the disabled_as_destination of this StorageProvider.  # noqa: E501

        Storage is not allowed to be used as a default storage in endpoint or as a migration destination)  # noqa: E501

        :return: The disabled_as_destination of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._disabled_as_destination

    @disabled_as_destination.setter
    def disabled_as_destination(self, disabled_as_destination):
        """Sets the disabled_as_destination of this StorageProvider.

        Storage is not allowed to be used as a default storage in endpoint or as a migration destination)  # noqa: E501

        :param disabled_as_destination: The disabled_as_destination of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._disabled_as_destination = disabled_as_destination

    @property
    def endpoint(self):
        """Gets the endpoint of this StorageProvider.  # noqa: E501

        Endpoint to access this provider or null for custom providers  # noqa: E501

        :return: The endpoint of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this StorageProvider.

        Endpoint to access this provider or null for custom providers  # noqa: E501

        :param endpoint: The endpoint of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def endpoint_pattern(self):
        """Gets the endpoint_pattern of this StorageProvider.  # noqa: E501

        Endpoint pattern to access specific region of this provider  # noqa: E501

        :return: The endpoint_pattern of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_pattern

    @endpoint_pattern.setter
    def endpoint_pattern(self, endpoint_pattern):
        """Sets the endpoint_pattern of this StorageProvider.

        Endpoint pattern to access specific region of this provider  # noqa: E501

        :param endpoint_pattern: The endpoint_pattern of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._endpoint_pattern = endpoint_pattern

    @property
    def id(self):
        """Gets the id of this StorageProvider.  # noqa: E501

        Id of the provider in the system  # noqa: E501

        :return: The id of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageProvider.

        Id of the provider in the system  # noqa: E501

        :param id: The id of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_upload_size(self):
        """Gets the max_upload_size of this StorageProvider.  # noqa: E501

        Maximum size of a single upload w/o multipart  # noqa: E501

        :return: The max_upload_size of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._max_upload_size

    @max_upload_size.setter
    def max_upload_size(self, max_upload_size):
        """Sets the max_upload_size of this StorageProvider.

        Maximum size of a single upload w/o multipart  # noqa: E501

        :param max_upload_size: The max_upload_size of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._max_upload_size = max_upload_size

    @property
    def multi_regional(self):
        """Gets the multi_regional of this StorageProvider.  # noqa: E501

        This cloud provider supports multiple regions  # noqa: E501

        :return: The multi_regional of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._multi_regional

    @multi_regional.setter
    def multi_regional(self, multi_regional):
        """Sets the multi_regional of this StorageProvider.

        This cloud provider supports multiple regions  # noqa: E501

        :param multi_regional: The multi_regional of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._multi_regional = multi_regional

    @property
    def name(self):
        """Gets the name of this StorageProvider.  # noqa: E501

        Name of the provider  # noqa: E501

        :return: The name of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageProvider.

        Name of the provider  # noqa: E501

        :param name: The name of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port_http(self):
        """Gets the port_http of this StorageProvider.  # noqa: E501

        Port for HTTP request (null for default 80)  # noqa: E501

        :return: The port_http of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._port_http

    @port_http.setter
    def port_http(self, port_http):
        """Sets the port_http of this StorageProvider.

        Port for HTTP request (null for default 80)  # noqa: E501

        :param port_http: The port_http of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._port_http = port_http

    @property
    def port_https(self):
        """Gets the port_https of this StorageProvider.  # noqa: E501

        Port for HTTPS request (null for default 443)  # noqa: E501

        :return: The port_https of this StorageProvider.  # noqa: E501
        :rtype: int
        """
        return self._port_https

    @port_https.setter
    def port_https(self, port_https):
        """Sets the port_https of this StorageProvider.

        Port for HTTPS request (null for default 443)  # noqa: E501

        :param port_https: The port_https of this StorageProvider.  # noqa: E501
        :type: int
        """

        self._port_https = port_https

    @property
    def private_endpoint(self):
        """Gets the private_endpoint of this StorageProvider.  # noqa: E501

        Endpoint used by engines (or null if only public endpoint is used)  # noqa: E501

        :return: The private_endpoint of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """Sets the private_endpoint of this StorageProvider.

        Endpoint used by engines (or null if only public endpoint is used)  # noqa: E501

        :param private_endpoint: The private_endpoint of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._private_endpoint = private_endpoint

    @property
    def private_endpoint_pattern(self):
        """Gets the private_endpoint_pattern of this StorageProvider.  # noqa: E501

        Endpoint pattern used by engines for specific region  # noqa: E501

        :return: The private_endpoint_pattern of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._private_endpoint_pattern

    @private_endpoint_pattern.setter
    def private_endpoint_pattern(self, private_endpoint_pattern):
        """Sets the private_endpoint_pattern of this StorageProvider.

        Endpoint pattern used by engines for specific region  # noqa: E501

        :param private_endpoint_pattern: The private_endpoint_pattern of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._private_endpoint_pattern = private_endpoint_pattern

    @property
    def product_name(self):
        """Gets the product_name of this StorageProvider.  # noqa: E501

        Name of product/region for this provider  # noqa: E501

        :return: The product_name of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this StorageProvider.

        Name of product/region for this provider  # noqa: E501

        :param product_name: The product_name of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def protocol(self):
        """Gets the protocol of this StorageProvider.  # noqa: E501

        Storage protocol this provider uses  # noqa: E501

        :return: The protocol of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this StorageProvider.

        Storage protocol this provider uses  # noqa: E501

        :param protocol: The protocol of this StorageProvider.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "B2", "DROPBOX", "DROPBOX_TEAM", "S3"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def supports_credential(self):
        """Gets the supports_credential of this StorageProvider.  # noqa: E501

        If the provider supports auth with credential (storage keys)  # noqa: E501

        :return: The supports_credential of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_credential

    @supports_credential.setter
    def supports_credential(self, supports_credential):
        """Sets the supports_credential of this StorageProvider.

        If the provider supports auth with credential (storage keys)  # noqa: E501

        :param supports_credential: The supports_credential of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_credential = supports_credential

    @property
    def supports_http(self):
        """Gets the supports_http of this StorageProvider.  # noqa: E501

        Indicates that HTTP is supported  # noqa: E501

        :return: The supports_http of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_http

    @supports_http.setter
    def supports_http(self, supports_http):
        """Sets the supports_http of this StorageProvider.

        Indicates that HTTP is supported  # noqa: E501

        :param supports_http: The supports_http of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_http = supports_http

    @property
    def supports_https(self):
        """Gets the supports_https of this StorageProvider.  # noqa: E501

        Indicates that HTTPS (SSL) is supported  # noqa: E501

        :return: The supports_https of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_https

    @supports_https.setter
    def supports_https(self, supports_https):
        """Sets the supports_https of this StorageProvider.

        Indicates that HTTPS (SSL) is supported  # noqa: E501

        :param supports_https: The supports_https of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_https = supports_https

    @property
    def supports_multipart_upload(self):
        """Gets the supports_multipart_upload of this StorageProvider.  # noqa: E501

        Indicates that the provider supports multipart upload  # noqa: E501

        :return: The supports_multipart_upload of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_multipart_upload

    @supports_multipart_upload.setter
    def supports_multipart_upload(self, supports_multipart_upload):
        """Sets the supports_multipart_upload of this StorageProvider.

        Indicates that the provider supports multipart upload  # noqa: E501

        :param supports_multipart_upload: The supports_multipart_upload of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_multipart_upload = supports_multipart_upload

    @property
    def supports_o_auth(self):
        """Gets the supports_o_auth of this StorageProvider.  # noqa: E501

        If the provider supports OAuth (instead of storage keys)  # noqa: E501

        :return: The supports_o_auth of this StorageProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_o_auth

    @supports_o_auth.setter
    def supports_o_auth(self, supports_o_auth):
        """Sets the supports_o_auth of this StorageProvider.

        If the provider supports OAuth (instead of storage keys)  # noqa: E501

        :param supports_o_auth: The supports_o_auth of this StorageProvider.  # noqa: E501
        :type: bool
        """

        self._supports_o_auth = supports_o_auth

    @property
    def supports_o_auth_name(self):
        """Gets the supports_o_auth_name of this StorageProvider.  # noqa: E501

        Name the provider is using his variation of OAuth  # noqa: E501

        :return: The supports_o_auth_name of this StorageProvider.  # noqa: E501
        :rtype: str
        """
        return self._supports_o_auth_name

    @supports_o_auth_name.setter
    def supports_o_auth_name(self, supports_o_auth_name):
        """Sets the supports_o_auth_name of this StorageProvider.

        Name the provider is using his variation of OAuth  # noqa: E501

        :param supports_o_auth_name: The supports_o_auth_name of this StorageProvider.  # noqa: E501
        :type: str
        """

        self._supports_o_auth_name = supports_o_auth_name

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
        if issubclass(StorageProvider, dict):
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
        if not isinstance(other, StorageProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageProvider):
            return True

        return self.to_dict() != other.to_dict()
