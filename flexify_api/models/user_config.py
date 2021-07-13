# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.6
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserConfig(object):
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
        'max_active_migrations': 'int',
        'max_auto_deploy_engines_count': 'int',
        'max_endpoints': 'int',
        'max_migration_copy_retries': 'int',
        'max_migration_engines': 'int',
        'max_migration_mappings': 'int',
        'max_migration_ram_mb': 'int',
        'max_migration_retries': 'int',
        'max_migration_slots': 'int',
        'max_migration_stream_ram_kb': 'int',
        'max_migration_streams': 'int',
        'max_migrations_in_queue': 'int',
        'max_storage_accounts_per_endpoint': 'int',
        'max_storages': 'int',
        'max_storages_per_virtual_bucket': 'int',
        'max_virtual_buckets_per_endpoint': 'int',
        'skip_auto_undeploy': 'int'
    }

    attribute_map = {
        'max_active_migrations': 'maxActiveMigrations',
        'max_auto_deploy_engines_count': 'maxAutoDeployEnginesCount',
        'max_endpoints': 'maxEndpoints',
        'max_migration_copy_retries': 'maxMigrationCopyRetries',
        'max_migration_engines': 'maxMigrationEngines',
        'max_migration_mappings': 'maxMigrationMappings',
        'max_migration_ram_mb': 'maxMigrationRamMb',
        'max_migration_retries': 'maxMigrationRetries',
        'max_migration_slots': 'maxMigrationSlots',
        'max_migration_stream_ram_kb': 'maxMigrationStreamRamKb',
        'max_migration_streams': 'maxMigrationStreams',
        'max_migrations_in_queue': 'maxMigrationsInQueue',
        'max_storage_accounts_per_endpoint': 'maxStorageAccountsPerEndpoint',
        'max_storages': 'maxStorages',
        'max_storages_per_virtual_bucket': 'maxStoragesPerVirtualBucket',
        'max_virtual_buckets_per_endpoint': 'maxVirtualBucketsPerEndpoint',
        'skip_auto_undeploy': 'skipAutoUndeploy'
    }

    def __init__(self, max_active_migrations=None, max_auto_deploy_engines_count=None, max_endpoints=None, max_migration_copy_retries=None, max_migration_engines=None, max_migration_mappings=None, max_migration_ram_mb=None, max_migration_retries=None, max_migration_slots=None, max_migration_stream_ram_kb=None, max_migration_streams=None, max_migrations_in_queue=None, max_storage_accounts_per_endpoint=None, max_storages=None, max_storages_per_virtual_bucket=None, max_virtual_buckets_per_endpoint=None, skip_auto_undeploy=None):  # noqa: E501
        """UserConfig - a model defined in Swagger"""  # noqa: E501

        self._max_active_migrations = None
        self._max_auto_deploy_engines_count = None
        self._max_endpoints = None
        self._max_migration_copy_retries = None
        self._max_migration_engines = None
        self._max_migration_mappings = None
        self._max_migration_ram_mb = None
        self._max_migration_retries = None
        self._max_migration_slots = None
        self._max_migration_stream_ram_kb = None
        self._max_migration_streams = None
        self._max_migrations_in_queue = None
        self._max_storage_accounts_per_endpoint = None
        self._max_storages = None
        self._max_storages_per_virtual_bucket = None
        self._max_virtual_buckets_per_endpoint = None
        self._skip_auto_undeploy = None
        self.discriminator = None

        if max_active_migrations is not None:
            self.max_active_migrations = max_active_migrations
        if max_auto_deploy_engines_count is not None:
            self.max_auto_deploy_engines_count = max_auto_deploy_engines_count
        if max_endpoints is not None:
            self.max_endpoints = max_endpoints
        if max_migration_copy_retries is not None:
            self.max_migration_copy_retries = max_migration_copy_retries
        if max_migration_engines is not None:
            self.max_migration_engines = max_migration_engines
        if max_migration_mappings is not None:
            self.max_migration_mappings = max_migration_mappings
        if max_migration_ram_mb is not None:
            self.max_migration_ram_mb = max_migration_ram_mb
        if max_migration_retries is not None:
            self.max_migration_retries = max_migration_retries
        if max_migration_slots is not None:
            self.max_migration_slots = max_migration_slots
        if max_migration_stream_ram_kb is not None:
            self.max_migration_stream_ram_kb = max_migration_stream_ram_kb
        if max_migration_streams is not None:
            self.max_migration_streams = max_migration_streams
        if max_migrations_in_queue is not None:
            self.max_migrations_in_queue = max_migrations_in_queue
        if max_storage_accounts_per_endpoint is not None:
            self.max_storage_accounts_per_endpoint = max_storage_accounts_per_endpoint
        if max_storages is not None:
            self.max_storages = max_storages
        if max_storages_per_virtual_bucket is not None:
            self.max_storages_per_virtual_bucket = max_storages_per_virtual_bucket
        if max_virtual_buckets_per_endpoint is not None:
            self.max_virtual_buckets_per_endpoint = max_virtual_buckets_per_endpoint
        if skip_auto_undeploy is not None:
            self.skip_auto_undeploy = skip_auto_undeploy

    @property
    def max_active_migrations(self):
        """Gets the max_active_migrations of this UserConfig.  # noqa: E501


        :return: The max_active_migrations of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_active_migrations

    @max_active_migrations.setter
    def max_active_migrations(self, max_active_migrations):
        """Sets the max_active_migrations of this UserConfig.


        :param max_active_migrations: The max_active_migrations of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_active_migrations = max_active_migrations

    @property
    def max_auto_deploy_engines_count(self):
        """Gets the max_auto_deploy_engines_count of this UserConfig.  # noqa: E501


        :return: The max_auto_deploy_engines_count of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_auto_deploy_engines_count

    @max_auto_deploy_engines_count.setter
    def max_auto_deploy_engines_count(self, max_auto_deploy_engines_count):
        """Sets the max_auto_deploy_engines_count of this UserConfig.


        :param max_auto_deploy_engines_count: The max_auto_deploy_engines_count of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_auto_deploy_engines_count = max_auto_deploy_engines_count

    @property
    def max_endpoints(self):
        """Gets the max_endpoints of this UserConfig.  # noqa: E501


        :return: The max_endpoints of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_endpoints

    @max_endpoints.setter
    def max_endpoints(self, max_endpoints):
        """Sets the max_endpoints of this UserConfig.


        :param max_endpoints: The max_endpoints of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_endpoints = max_endpoints

    @property
    def max_migration_copy_retries(self):
        """Gets the max_migration_copy_retries of this UserConfig.  # noqa: E501


        :return: The max_migration_copy_retries of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_copy_retries

    @max_migration_copy_retries.setter
    def max_migration_copy_retries(self, max_migration_copy_retries):
        """Sets the max_migration_copy_retries of this UserConfig.


        :param max_migration_copy_retries: The max_migration_copy_retries of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_copy_retries = max_migration_copy_retries

    @property
    def max_migration_engines(self):
        """Gets the max_migration_engines of this UserConfig.  # noqa: E501


        :return: The max_migration_engines of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_engines

    @max_migration_engines.setter
    def max_migration_engines(self, max_migration_engines):
        """Sets the max_migration_engines of this UserConfig.


        :param max_migration_engines: The max_migration_engines of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_engines = max_migration_engines

    @property
    def max_migration_mappings(self):
        """Gets the max_migration_mappings of this UserConfig.  # noqa: E501


        :return: The max_migration_mappings of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_mappings

    @max_migration_mappings.setter
    def max_migration_mappings(self, max_migration_mappings):
        """Sets the max_migration_mappings of this UserConfig.


        :param max_migration_mappings: The max_migration_mappings of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_mappings = max_migration_mappings

    @property
    def max_migration_ram_mb(self):
        """Gets the max_migration_ram_mb of this UserConfig.  # noqa: E501


        :return: The max_migration_ram_mb of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_ram_mb

    @max_migration_ram_mb.setter
    def max_migration_ram_mb(self, max_migration_ram_mb):
        """Sets the max_migration_ram_mb of this UserConfig.


        :param max_migration_ram_mb: The max_migration_ram_mb of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_ram_mb = max_migration_ram_mb

    @property
    def max_migration_retries(self):
        """Gets the max_migration_retries of this UserConfig.  # noqa: E501


        :return: The max_migration_retries of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_retries

    @max_migration_retries.setter
    def max_migration_retries(self, max_migration_retries):
        """Sets the max_migration_retries of this UserConfig.


        :param max_migration_retries: The max_migration_retries of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_retries = max_migration_retries

    @property
    def max_migration_slots(self):
        """Gets the max_migration_slots of this UserConfig.  # noqa: E501


        :return: The max_migration_slots of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_slots

    @max_migration_slots.setter
    def max_migration_slots(self, max_migration_slots):
        """Sets the max_migration_slots of this UserConfig.


        :param max_migration_slots: The max_migration_slots of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_slots = max_migration_slots

    @property
    def max_migration_stream_ram_kb(self):
        """Gets the max_migration_stream_ram_kb of this UserConfig.  # noqa: E501


        :return: The max_migration_stream_ram_kb of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_stream_ram_kb

    @max_migration_stream_ram_kb.setter
    def max_migration_stream_ram_kb(self, max_migration_stream_ram_kb):
        """Sets the max_migration_stream_ram_kb of this UserConfig.


        :param max_migration_stream_ram_kb: The max_migration_stream_ram_kb of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_stream_ram_kb = max_migration_stream_ram_kb

    @property
    def max_migration_streams(self):
        """Gets the max_migration_streams of this UserConfig.  # noqa: E501


        :return: The max_migration_streams of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migration_streams

    @max_migration_streams.setter
    def max_migration_streams(self, max_migration_streams):
        """Sets the max_migration_streams of this UserConfig.


        :param max_migration_streams: The max_migration_streams of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migration_streams = max_migration_streams

    @property
    def max_migrations_in_queue(self):
        """Gets the max_migrations_in_queue of this UserConfig.  # noqa: E501


        :return: The max_migrations_in_queue of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_migrations_in_queue

    @max_migrations_in_queue.setter
    def max_migrations_in_queue(self, max_migrations_in_queue):
        """Sets the max_migrations_in_queue of this UserConfig.


        :param max_migrations_in_queue: The max_migrations_in_queue of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_migrations_in_queue = max_migrations_in_queue

    @property
    def max_storage_accounts_per_endpoint(self):
        """Gets the max_storage_accounts_per_endpoint of this UserConfig.  # noqa: E501


        :return: The max_storage_accounts_per_endpoint of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_storage_accounts_per_endpoint

    @max_storage_accounts_per_endpoint.setter
    def max_storage_accounts_per_endpoint(self, max_storage_accounts_per_endpoint):
        """Sets the max_storage_accounts_per_endpoint of this UserConfig.


        :param max_storage_accounts_per_endpoint: The max_storage_accounts_per_endpoint of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_storage_accounts_per_endpoint = max_storage_accounts_per_endpoint

    @property
    def max_storages(self):
        """Gets the max_storages of this UserConfig.  # noqa: E501


        :return: The max_storages of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_storages

    @max_storages.setter
    def max_storages(self, max_storages):
        """Sets the max_storages of this UserConfig.


        :param max_storages: The max_storages of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_storages = max_storages

    @property
    def max_storages_per_virtual_bucket(self):
        """Gets the max_storages_per_virtual_bucket of this UserConfig.  # noqa: E501


        :return: The max_storages_per_virtual_bucket of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_storages_per_virtual_bucket

    @max_storages_per_virtual_bucket.setter
    def max_storages_per_virtual_bucket(self, max_storages_per_virtual_bucket):
        """Sets the max_storages_per_virtual_bucket of this UserConfig.


        :param max_storages_per_virtual_bucket: The max_storages_per_virtual_bucket of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_storages_per_virtual_bucket = max_storages_per_virtual_bucket

    @property
    def max_virtual_buckets_per_endpoint(self):
        """Gets the max_virtual_buckets_per_endpoint of this UserConfig.  # noqa: E501


        :return: The max_virtual_buckets_per_endpoint of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_virtual_buckets_per_endpoint

    @max_virtual_buckets_per_endpoint.setter
    def max_virtual_buckets_per_endpoint(self, max_virtual_buckets_per_endpoint):
        """Sets the max_virtual_buckets_per_endpoint of this UserConfig.


        :param max_virtual_buckets_per_endpoint: The max_virtual_buckets_per_endpoint of this UserConfig.  # noqa: E501
        :type: int
        """

        self._max_virtual_buckets_per_endpoint = max_virtual_buckets_per_endpoint

    @property
    def skip_auto_undeploy(self):
        """Gets the skip_auto_undeploy of this UserConfig.  # noqa: E501


        :return: The skip_auto_undeploy of this UserConfig.  # noqa: E501
        :rtype: int
        """
        return self._skip_auto_undeploy

    @skip_auto_undeploy.setter
    def skip_auto_undeploy(self, skip_auto_undeploy):
        """Sets the skip_auto_undeploy of this UserConfig.


        :param skip_auto_undeploy: The skip_auto_undeploy of this UserConfig.  # noqa: E501
        :type: int
        """

        self._skip_auto_undeploy = skip_auto_undeploy

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
        if issubclass(UserConfig, dict):
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
        if not isinstance(other, UserConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
