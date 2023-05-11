# coding: utf-8

"""
    Flexify IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.15
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flexify_api.configuration import Configuration


class MigrationSettingsRes(object):
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
        'auto_restore_if_archived': 'bool',
        'comparison_method': 'str',
        'conflict_resolution': 'str',
        'deployment_type': 'str',
        'dry_run': 'bool',
        'engines_location': 'CloudLocationRes',
        'existing_data_in_destination': 'str',
        'last_modified_from': 'datetime',
        'log_level': 'str',
        'max_engines': 'int',
        'max_retries': 'int',
        'max_retries_for_copy': 'int',
        'max_retry_timeout': 'int',
        'max_streams': 'int',
        'migration_mode': 'str',
        'multipart_concurrency': 'int',
        'multipart_limit': 'int',
        'multipart_part_size': 'int',
        'name': 'str',
        'object_key_filter': 'str',
        'restore_days': 'int',
        'restore_max_size': 'int',
        'restore_tier': 'str',
        'retry_timeout': 'int',
        'skip_if_hash_matches': 'bool',
        'slots_per_mapping': 'int',
        'upload_timestamp_mode': 'str',
        'upload_timestamp_value': 'datetime'
    }

    attribute_map = {
        'auto_restore_if_archived': 'autoRestoreIfArchived',
        'comparison_method': 'comparisonMethod',
        'conflict_resolution': 'conflictResolution',
        'deployment_type': 'deploymentType',
        'dry_run': 'dryRun',
        'engines_location': 'enginesLocation',
        'existing_data_in_destination': 'existingDataInDestination',
        'last_modified_from': 'lastModifiedFrom',
        'log_level': 'logLevel',
        'max_engines': 'maxEngines',
        'max_retries': 'maxRetries',
        'max_retries_for_copy': 'maxRetriesForCopy',
        'max_retry_timeout': 'maxRetryTimeout',
        'max_streams': 'maxStreams',
        'migration_mode': 'migrationMode',
        'multipart_concurrency': 'multipartConcurrency',
        'multipart_limit': 'multipartLimit',
        'multipart_part_size': 'multipartPartSize',
        'name': 'name',
        'object_key_filter': 'objectKeyFilter',
        'restore_days': 'restoreDays',
        'restore_max_size': 'restoreMaxSize',
        'restore_tier': 'restoreTier',
        'retry_timeout': 'retryTimeout',
        'skip_if_hash_matches': 'skipIfHashMatches',
        'slots_per_mapping': 'slotsPerMapping',
        'upload_timestamp_mode': 'uploadTimestampMode',
        'upload_timestamp_value': 'uploadTimestampValue'
    }

    def __init__(self, auto_restore_if_archived=None, comparison_method=None, conflict_resolution=None, deployment_type=None, dry_run=None, engines_location=None, existing_data_in_destination=None, last_modified_from=None, log_level=None, max_engines=None, max_retries=None, max_retries_for_copy=None, max_retry_timeout=None, max_streams=None, migration_mode=None, multipart_concurrency=None, multipart_limit=None, multipart_part_size=None, name=None, object_key_filter=None, restore_days=None, restore_max_size=None, restore_tier=None, retry_timeout=None, skip_if_hash_matches=None, slots_per_mapping=None, upload_timestamp_mode=None, upload_timestamp_value=None, _configuration=None):  # noqa: E501
        """MigrationSettingsRes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_restore_if_archived = None
        self._comparison_method = None
        self._conflict_resolution = None
        self._deployment_type = None
        self._dry_run = None
        self._engines_location = None
        self._existing_data_in_destination = None
        self._last_modified_from = None
        self._log_level = None
        self._max_engines = None
        self._max_retries = None
        self._max_retries_for_copy = None
        self._max_retry_timeout = None
        self._max_streams = None
        self._migration_mode = None
        self._multipart_concurrency = None
        self._multipart_limit = None
        self._multipart_part_size = None
        self._name = None
        self._object_key_filter = None
        self._restore_days = None
        self._restore_max_size = None
        self._restore_tier = None
        self._retry_timeout = None
        self._skip_if_hash_matches = None
        self._slots_per_mapping = None
        self._upload_timestamp_mode = None
        self._upload_timestamp_value = None
        self.discriminator = None

        if auto_restore_if_archived is not None:
            self.auto_restore_if_archived = auto_restore_if_archived
        if comparison_method is not None:
            self.comparison_method = comparison_method
        if conflict_resolution is not None:
            self.conflict_resolution = conflict_resolution
        if deployment_type is not None:
            self.deployment_type = deployment_type
        if dry_run is not None:
            self.dry_run = dry_run
        if engines_location is not None:
            self.engines_location = engines_location
        if existing_data_in_destination is not None:
            self.existing_data_in_destination = existing_data_in_destination
        if last_modified_from is not None:
            self.last_modified_from = last_modified_from
        if log_level is not None:
            self.log_level = log_level
        if max_engines is not None:
            self.max_engines = max_engines
        if max_retries is not None:
            self.max_retries = max_retries
        if max_retries_for_copy is not None:
            self.max_retries_for_copy = max_retries_for_copy
        if max_retry_timeout is not None:
            self.max_retry_timeout = max_retry_timeout
        if max_streams is not None:
            self.max_streams = max_streams
        if migration_mode is not None:
            self.migration_mode = migration_mode
        if multipart_concurrency is not None:
            self.multipart_concurrency = multipart_concurrency
        if multipart_limit is not None:
            self.multipart_limit = multipart_limit
        if multipart_part_size is not None:
            self.multipart_part_size = multipart_part_size
        if name is not None:
            self.name = name
        if object_key_filter is not None:
            self.object_key_filter = object_key_filter
        if restore_days is not None:
            self.restore_days = restore_days
        if restore_max_size is not None:
            self.restore_max_size = restore_max_size
        if restore_tier is not None:
            self.restore_tier = restore_tier
        if retry_timeout is not None:
            self.retry_timeout = retry_timeout
        if skip_if_hash_matches is not None:
            self.skip_if_hash_matches = skip_if_hash_matches
        if slots_per_mapping is not None:
            self.slots_per_mapping = slots_per_mapping
        if upload_timestamp_mode is not None:
            self.upload_timestamp_mode = upload_timestamp_mode
        if upload_timestamp_value is not None:
            self.upload_timestamp_value = upload_timestamp_value

    @property
    def auto_restore_if_archived(self):
        """Gets the auto_restore_if_archived of this MigrationSettingsRes.  # noqa: E501

        Automatically restore objects from archival tier  # noqa: E501

        :return: The auto_restore_if_archived of this MigrationSettingsRes.  # noqa: E501
        :rtype: bool
        """
        return self._auto_restore_if_archived

    @auto_restore_if_archived.setter
    def auto_restore_if_archived(self, auto_restore_if_archived):
        """Sets the auto_restore_if_archived of this MigrationSettingsRes.

        Automatically restore objects from archival tier  # noqa: E501

        :param auto_restore_if_archived: The auto_restore_if_archived of this MigrationSettingsRes.  # noqa: E501
        :type: bool
        """

        self._auto_restore_if_archived = auto_restore_if_archived

    @property
    def comparison_method(self):
        """Gets the comparison_method of this MigrationSettingsRes.  # noqa: E501

        Destination comparison method  # noqa: E501

        :return: The comparison_method of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._comparison_method

    @comparison_method.setter
    def comparison_method(self, comparison_method):
        """Sets the comparison_method of this MigrationSettingsRes.

        Destination comparison method  # noqa: E501

        :param comparison_method: The comparison_method of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO", "LIST_ONLY", "LIST_PROBE", "PROBE_ONLY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                comparison_method not in allowed_values):
            raise ValueError(
                "Invalid value for `comparison_method` ({0}), must be one of {1}"  # noqa: E501
                .format(comparison_method, allowed_values)
            )

        self._comparison_method = comparison_method

    @property
    def conflict_resolution(self):
        """Gets the conflict_resolution of this MigrationSettingsRes.  # noqa: E501

        Conflict resolution  # noqa: E501

        :return: The conflict_resolution of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._conflict_resolution

    @conflict_resolution.setter
    def conflict_resolution(self, conflict_resolution):
        """Sets the conflict_resolution of this MigrationSettingsRes.

        Conflict resolution  # noqa: E501

        :param conflict_resolution: The conflict_resolution of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOTH", "DESTINATION", "NEWER", "SOURCE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                conflict_resolution not in allowed_values):
            raise ValueError(
                "Invalid value for `conflict_resolution` ({0}), must be one of {1}"  # noqa: E501
                .format(conflict_resolution, allowed_values)
            )

        self._conflict_resolution = conflict_resolution

    @property
    def deployment_type(self):
        """Gets the deployment_type of this MigrationSettingsRes.  # noqa: E501

        The type of engine deployment  # noqa: E501

        :return: The deployment_type of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this MigrationSettingsRes.

        The type of engine deployment  # noqa: E501

        :param deployment_type: The deployment_type of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO", "DEPLOYMENT", "SELECTION"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deployment_type not in allowed_values):
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

    @property
    def dry_run(self):
        """Gets the dry_run of this MigrationSettingsRes.  # noqa: E501

        Dry run mode  # noqa: E501

        :return: The dry_run of this MigrationSettingsRes.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this MigrationSettingsRes.

        Dry run mode  # noqa: E501

        :param dry_run: The dry_run of this MigrationSettingsRes.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def engines_location(self):
        """Gets the engines_location of this MigrationSettingsRes.  # noqa: E501

        Location of the engines to migrate  # noqa: E501

        :return: The engines_location of this MigrationSettingsRes.  # noqa: E501
        :rtype: CloudLocationRes
        """
        return self._engines_location

    @engines_location.setter
    def engines_location(self, engines_location):
        """Sets the engines_location of this MigrationSettingsRes.

        Location of the engines to migrate  # noqa: E501

        :param engines_location: The engines_location of this MigrationSettingsRes.  # noqa: E501
        :type: CloudLocationRes
        """

        self._engines_location = engines_location

    @property
    def existing_data_in_destination(self):
        """Gets the existing_data_in_destination of this MigrationSettingsRes.  # noqa: E501

        Keep or clean data in destination before migration (identical with source objects keep in any cases)  # noqa: E501

        :return: The existing_data_in_destination of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._existing_data_in_destination

    @existing_data_in_destination.setter
    def existing_data_in_destination(self, existing_data_in_destination):
        """Sets the existing_data_in_destination of this MigrationSettingsRes.

        Keep or clean data in destination before migration (identical with source objects keep in any cases)  # noqa: E501

        :param existing_data_in_destination: The existing_data_in_destination of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLEAN", "KEEP"]  # noqa: E501
        if (self._configuration.client_side_validation and
                existing_data_in_destination not in allowed_values):
            raise ValueError(
                "Invalid value for `existing_data_in_destination` ({0}), must be one of {1}"  # noqa: E501
                .format(existing_data_in_destination, allowed_values)
            )

        self._existing_data_in_destination = existing_data_in_destination

    @property
    def last_modified_from(self):
        """Gets the last_modified_from of this MigrationSettingsRes.  # noqa: E501

        Migrate objects modified on or after specified date  # noqa: E501

        :return: The last_modified_from of this MigrationSettingsRes.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_from

    @last_modified_from.setter
    def last_modified_from(self, last_modified_from):
        """Sets the last_modified_from of this MigrationSettingsRes.

        Migrate objects modified on or after specified date  # noqa: E501

        :param last_modified_from: The last_modified_from of this MigrationSettingsRes.  # noqa: E501
        :type: datetime
        """

        self._last_modified_from = last_modified_from

    @property
    def log_level(self):
        """Gets the log_level of this MigrationSettingsRes.  # noqa: E501

        Log level  # noqa: E501

        :return: The log_level of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this MigrationSettingsRes.

        Log level  # noqa: E501

        :param log_level: The log_level of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEBUG", "ERROR", "INFO", "TRACE", "WARNING"]  # noqa: E501
        if (self._configuration.client_side_validation and
                log_level not in allowed_values):
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

    @property
    def max_engines(self):
        """Gets the max_engines of this MigrationSettingsRes.  # noqa: E501

        Maximum number of engines this migration uses (experimental)  # noqa: E501

        :return: The max_engines of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._max_engines

    @max_engines.setter
    def max_engines(self, max_engines):
        """Sets the max_engines of this MigrationSettingsRes.

        Maximum number of engines this migration uses (experimental)  # noqa: E501

        :param max_engines: The max_engines of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._max_engines = max_engines

    @property
    def max_retries(self):
        """Gets the max_retries of this MigrationSettingsRes.  # noqa: E501

        Maximum number of retries  # noqa: E501

        :return: The max_retries of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this MigrationSettingsRes.

        Maximum number of retries  # noqa: E501

        :param max_retries: The max_retries of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._max_retries = max_retries

    @property
    def max_retries_for_copy(self):
        """Gets the max_retries_for_copy of this MigrationSettingsRes.  # noqa: E501

        Maximum number of retries after copy started  # noqa: E501

        :return: The max_retries_for_copy of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._max_retries_for_copy

    @max_retries_for_copy.setter
    def max_retries_for_copy(self, max_retries_for_copy):
        """Sets the max_retries_for_copy of this MigrationSettingsRes.

        Maximum number of retries after copy started  # noqa: E501

        :param max_retries_for_copy: The max_retries_for_copy of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._max_retries_for_copy = max_retries_for_copy

    @property
    def max_retry_timeout(self):
        """Gets the max_retry_timeout of this MigrationSettingsRes.  # noqa: E501

        Maximum timeout between retries in seconds  # noqa: E501

        :return: The max_retry_timeout of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._max_retry_timeout

    @max_retry_timeout.setter
    def max_retry_timeout(self, max_retry_timeout):
        """Sets the max_retry_timeout of this MigrationSettingsRes.

        Maximum timeout between retries in seconds  # noqa: E501

        :param max_retry_timeout: The max_retry_timeout of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._max_retry_timeout = max_retry_timeout

    @property
    def max_streams(self):
        """Gets the max_streams of this MigrationSettingsRes.  # noqa: E501

        Maximum streams that migration will use across all engines  # noqa: E501

        :return: The max_streams of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._max_streams

    @max_streams.setter
    def max_streams(self, max_streams):
        """Sets the max_streams of this MigrationSettingsRes.

        Maximum streams that migration will use across all engines  # noqa: E501

        :param max_streams: The max_streams of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._max_streams = max_streams

    @property
    def migration_mode(self):
        """Gets the migration_mode of this MigrationSettingsRes.  # noqa: E501

        Migration mode  # noqa: E501

        :return: The migration_mode of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._migration_mode

    @migration_mode.setter
    def migration_mode(self, migration_mode):
        """Sets the migration_mode of this MigrationSettingsRes.

        Migration mode  # noqa: E501

        :param migration_mode: The migration_mode of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["COPY", "MOVE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                migration_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `migration_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(migration_mode, allowed_values)
            )

        self._migration_mode = migration_mode

    @property
    def multipart_concurrency(self):
        """Gets the multipart_concurrency of this MigrationSettingsRes.  # noqa: E501

        Maximum parts for parallel upload for a single object  # noqa: E501

        :return: The multipart_concurrency of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._multipart_concurrency

    @multipart_concurrency.setter
    def multipart_concurrency(self, multipart_concurrency):
        """Sets the multipart_concurrency of this MigrationSettingsRes.

        Maximum parts for parallel upload for a single object  # noqa: E501

        :param multipart_concurrency: The multipart_concurrency of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._multipart_concurrency = multipart_concurrency

    @property
    def multipart_limit(self):
        """Gets the multipart_limit of this MigrationSettingsRes.  # noqa: E501

        Minimum size in bytes for multipart upload  # noqa: E501

        :return: The multipart_limit of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._multipart_limit

    @multipart_limit.setter
    def multipart_limit(self, multipart_limit):
        """Sets the multipart_limit of this MigrationSettingsRes.

        Minimum size in bytes for multipart upload  # noqa: E501

        :param multipart_limit: The multipart_limit of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._multipart_limit = multipart_limit

    @property
    def multipart_part_size(self):
        """Gets the multipart_part_size of this MigrationSettingsRes.  # noqa: E501

        Part size for multipart upload  # noqa: E501

        :return: The multipart_part_size of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._multipart_part_size

    @multipart_part_size.setter
    def multipart_part_size(self, multipart_part_size):
        """Sets the multipart_part_size of this MigrationSettingsRes.

        Part size for multipart upload  # noqa: E501

        :param multipart_part_size: The multipart_part_size of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._multipart_part_size = multipart_part_size

    @property
    def name(self):
        """Gets the name of this MigrationSettingsRes.  # noqa: E501

        Name of the migration  # noqa: E501

        :return: The name of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationSettingsRes.

        Name of the migration  # noqa: E501

        :param name: The name of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object_key_filter(self):
        """Gets the object_key_filter of this MigrationSettingsRes.  # noqa: E501

        Migrate objects matching pattern  # noqa: E501

        :return: The object_key_filter of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._object_key_filter

    @object_key_filter.setter
    def object_key_filter(self, object_key_filter):
        """Sets the object_key_filter of this MigrationSettingsRes.

        Migrate objects matching pattern  # noqa: E501

        :param object_key_filter: The object_key_filter of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """

        self._object_key_filter = object_key_filter

    @property
    def restore_days(self):
        """Gets the restore_days of this MigrationSettingsRes.  # noqa: E501

        Number of days to keep restored objects when automatically restoring objects from archival tier  # noqa: E501

        :return: The restore_days of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._restore_days

    @restore_days.setter
    def restore_days(self, restore_days):
        """Sets the restore_days of this MigrationSettingsRes.

        Number of days to keep restored objects when automatically restoring objects from archival tier  # noqa: E501

        :param restore_days: The restore_days of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._restore_days = restore_days

    @property
    def restore_max_size(self):
        """Gets the restore_max_size of this MigrationSettingsRes.  # noqa: E501

        Maximum total size of objects to restore when automatically restoring objects from archival tier  # noqa: E501

        :return: The restore_max_size of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._restore_max_size

    @restore_max_size.setter
    def restore_max_size(self, restore_max_size):
        """Sets the restore_max_size of this MigrationSettingsRes.

        Maximum total size of objects to restore when automatically restoring objects from archival tier  # noqa: E501

        :param restore_max_size: The restore_max_size of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._restore_max_size = restore_max_size

    @property
    def restore_tier(self):
        """Gets the restore_tier of this MigrationSettingsRes.  # noqa: E501

        Restore tier when automatically restoring objects from archival tier  # noqa: E501

        :return: The restore_tier of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._restore_tier

    @restore_tier.setter
    def restore_tier(self, restore_tier):
        """Sets the restore_tier of this MigrationSettingsRes.

        Restore tier when automatically restoring objects from archival tier  # noqa: E501

        :param restore_tier: The restore_tier of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["BULK", "EXPEDITED", "STANDARD"]  # noqa: E501
        if (self._configuration.client_side_validation and
                restore_tier not in allowed_values):
            raise ValueError(
                "Invalid value for `restore_tier` ({0}), must be one of {1}"  # noqa: E501
                .format(restore_tier, allowed_values)
            )

        self._restore_tier = restore_tier

    @property
    def retry_timeout(self):
        """Gets the retry_timeout of this MigrationSettingsRes.  # noqa: E501

        Initial timeout between retries in seconds  # noqa: E501

        :return: The retry_timeout of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._retry_timeout

    @retry_timeout.setter
    def retry_timeout(self, retry_timeout):
        """Sets the retry_timeout of this MigrationSettingsRes.

        Initial timeout between retries in seconds  # noqa: E501

        :param retry_timeout: The retry_timeout of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._retry_timeout = retry_timeout

    @property
    def skip_if_hash_matches(self):
        """Gets the skip_if_hash_matches of this MigrationSettingsRes.  # noqa: E501

        Skip migration if source and destination object hash match  # noqa: E501

        :return: The skip_if_hash_matches of this MigrationSettingsRes.  # noqa: E501
        :rtype: bool
        """
        return self._skip_if_hash_matches

    @skip_if_hash_matches.setter
    def skip_if_hash_matches(self, skip_if_hash_matches):
        """Sets the skip_if_hash_matches of this MigrationSettingsRes.

        Skip migration if source and destination object hash match  # noqa: E501

        :param skip_if_hash_matches: The skip_if_hash_matches of this MigrationSettingsRes.  # noqa: E501
        :type: bool
        """

        self._skip_if_hash_matches = skip_if_hash_matches

    @property
    def slots_per_mapping(self):
        """Gets the slots_per_mapping of this MigrationSettingsRes.  # noqa: E501

        Number of slots of storage mapping (bucket)  # noqa: E501

        :return: The slots_per_mapping of this MigrationSettingsRes.  # noqa: E501
        :rtype: int
        """
        return self._slots_per_mapping

    @slots_per_mapping.setter
    def slots_per_mapping(self, slots_per_mapping):
        """Sets the slots_per_mapping of this MigrationSettingsRes.

        Number of slots of storage mapping (bucket)  # noqa: E501

        :param slots_per_mapping: The slots_per_mapping of this MigrationSettingsRes.  # noqa: E501
        :type: int
        """

        self._slots_per_mapping = slots_per_mapping

    @property
    def upload_timestamp_mode(self):
        """Gets the upload_timestamp_mode of this MigrationSettingsRes.  # noqa: E501

        Specify if to copy original or set specified timestamp when migration to B2  # noqa: E501

        :return: The upload_timestamp_mode of this MigrationSettingsRes.  # noqa: E501
        :rtype: str
        """
        return self._upload_timestamp_mode

    @upload_timestamp_mode.setter
    def upload_timestamp_mode(self, upload_timestamp_mode):
        """Sets the upload_timestamp_mode of this MigrationSettingsRes.

        Specify if to copy original or set specified timestamp when migration to B2  # noqa: E501

        :param upload_timestamp_mode: The upload_timestamp_mode of this MigrationSettingsRes.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTUAL", "CUSTOM", "ORIGINAL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                upload_timestamp_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `upload_timestamp_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(upload_timestamp_mode, allowed_values)
            )

        self._upload_timestamp_mode = upload_timestamp_mode

    @property
    def upload_timestamp_value(self):
        """Gets the upload_timestamp_value of this MigrationSettingsRes.  # noqa: E501

        The B2 timestamp value to set if uploadTimestampMode is CUSTOM  # noqa: E501

        :return: The upload_timestamp_value of this MigrationSettingsRes.  # noqa: E501
        :rtype: datetime
        """
        return self._upload_timestamp_value

    @upload_timestamp_value.setter
    def upload_timestamp_value(self, upload_timestamp_value):
        """Sets the upload_timestamp_value of this MigrationSettingsRes.

        The B2 timestamp value to set if uploadTimestampMode is CUSTOM  # noqa: E501

        :param upload_timestamp_value: The upload_timestamp_value of this MigrationSettingsRes.  # noqa: E501
        :type: datetime
        """

        self._upload_timestamp_value = upload_timestamp_value

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
        if issubclass(MigrationSettingsRes, dict):
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
        if not isinstance(other, MigrationSettingsRes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationSettingsRes):
            return True

        return self.to_dict() != other.to_dict()
