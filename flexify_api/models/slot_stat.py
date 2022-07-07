# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.10-SNAPSHOT
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SlotStat(object):
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
        'active_engines': 'int',
        'active_streams': 'int',
        'bytes_failed': 'int',
        'bytes_glacier_restore_started': 'int',
        'bytes_not_matching_pattern': 'int',
        'bytes_processed': 'int',
        'bytes_skipped': 'int',
        'bytes_skipped_glacier': 'int',
        'bytes_uploaded': 'int',
        'dst_region': 'str',
        'finished': 'datetime',
        'objects_failed': 'int',
        'objects_glacier_restore_started': 'int',
        'objects_not_matching_pattern': 'int',
        'objects_processed': 'int',
        'objects_skipped': 'int',
        'objects_skipped_glacier': 'int',
        'objects_uploaded': 'int',
        'processing_objects_per_second': 'float',
        'retried': 'int',
        'src_region': 'str',
        'started': 'datetime',
        'state': 'str',
        'total_upload': 'int',
        'uploading_bytes_per_second': 'float',
        'uploading_objects_per_second': 'float'
    }

    attribute_map = {
        'active_engines': 'activeEngines',
        'active_streams': 'activeStreams',
        'bytes_failed': 'bytesFailed',
        'bytes_glacier_restore_started': 'bytesGlacierRestoreStarted',
        'bytes_not_matching_pattern': 'bytesNotMatchingPattern',
        'bytes_processed': 'bytesProcessed',
        'bytes_skipped': 'bytesSkipped',
        'bytes_skipped_glacier': 'bytesSkippedGlacier',
        'bytes_uploaded': 'bytesUploaded',
        'dst_region': 'dstRegion',
        'finished': 'finished',
        'objects_failed': 'objectsFailed',
        'objects_glacier_restore_started': 'objectsGlacierRestoreStarted',
        'objects_not_matching_pattern': 'objectsNotMatchingPattern',
        'objects_processed': 'objectsProcessed',
        'objects_skipped': 'objectsSkipped',
        'objects_skipped_glacier': 'objectsSkippedGlacier',
        'objects_uploaded': 'objectsUploaded',
        'processing_objects_per_second': 'processingObjectsPerSecond',
        'retried': 'retried',
        'src_region': 'srcRegion',
        'started': 'started',
        'state': 'state',
        'total_upload': 'totalUpload',
        'uploading_bytes_per_second': 'uploadingBytesPerSecond',
        'uploading_objects_per_second': 'uploadingObjectsPerSecond'
    }

    def __init__(self, active_engines=None, active_streams=None, bytes_failed=None, bytes_glacier_restore_started=None, bytes_not_matching_pattern=None, bytes_processed=None, bytes_skipped=None, bytes_skipped_glacier=None, bytes_uploaded=None, dst_region=None, finished=None, objects_failed=None, objects_glacier_restore_started=None, objects_not_matching_pattern=None, objects_processed=None, objects_skipped=None, objects_skipped_glacier=None, objects_uploaded=None, processing_objects_per_second=None, retried=None, src_region=None, started=None, state=None, total_upload=None, uploading_bytes_per_second=None, uploading_objects_per_second=None):  # noqa: E501
        """SlotStat - a model defined in Swagger"""  # noqa: E501

        self._active_engines = None
        self._active_streams = None
        self._bytes_failed = None
        self._bytes_glacier_restore_started = None
        self._bytes_not_matching_pattern = None
        self._bytes_processed = None
        self._bytes_skipped = None
        self._bytes_skipped_glacier = None
        self._bytes_uploaded = None
        self._dst_region = None
        self._finished = None
        self._objects_failed = None
        self._objects_glacier_restore_started = None
        self._objects_not_matching_pattern = None
        self._objects_processed = None
        self._objects_skipped = None
        self._objects_skipped_glacier = None
        self._objects_uploaded = None
        self._processing_objects_per_second = None
        self._retried = None
        self._src_region = None
        self._started = None
        self._state = None
        self._total_upload = None
        self._uploading_bytes_per_second = None
        self._uploading_objects_per_second = None
        self.discriminator = None

        if active_engines is not None:
            self.active_engines = active_engines
        if active_streams is not None:
            self.active_streams = active_streams
        if bytes_failed is not None:
            self.bytes_failed = bytes_failed
        if bytes_glacier_restore_started is not None:
            self.bytes_glacier_restore_started = bytes_glacier_restore_started
        if bytes_not_matching_pattern is not None:
            self.bytes_not_matching_pattern = bytes_not_matching_pattern
        if bytes_processed is not None:
            self.bytes_processed = bytes_processed
        if bytes_skipped is not None:
            self.bytes_skipped = bytes_skipped
        if bytes_skipped_glacier is not None:
            self.bytes_skipped_glacier = bytes_skipped_glacier
        if bytes_uploaded is not None:
            self.bytes_uploaded = bytes_uploaded
        if dst_region is not None:
            self.dst_region = dst_region
        if finished is not None:
            self.finished = finished
        if objects_failed is not None:
            self.objects_failed = objects_failed
        if objects_glacier_restore_started is not None:
            self.objects_glacier_restore_started = objects_glacier_restore_started
        if objects_not_matching_pattern is not None:
            self.objects_not_matching_pattern = objects_not_matching_pattern
        if objects_processed is not None:
            self.objects_processed = objects_processed
        if objects_skipped is not None:
            self.objects_skipped = objects_skipped
        if objects_skipped_glacier is not None:
            self.objects_skipped_glacier = objects_skipped_glacier
        if objects_uploaded is not None:
            self.objects_uploaded = objects_uploaded
        if processing_objects_per_second is not None:
            self.processing_objects_per_second = processing_objects_per_second
        if retried is not None:
            self.retried = retried
        if src_region is not None:
            self.src_region = src_region
        if started is not None:
            self.started = started
        if state is not None:
            self.state = state
        if total_upload is not None:
            self.total_upload = total_upload
        if uploading_bytes_per_second is not None:
            self.uploading_bytes_per_second = uploading_bytes_per_second
        if uploading_objects_per_second is not None:
            self.uploading_objects_per_second = uploading_objects_per_second

    @property
    def active_engines(self):
        """Gets the active_engines of this SlotStat.  # noqa: E501

        Number of engines that are busy with this  # noqa: E501

        :return: The active_engines of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._active_engines

    @active_engines.setter
    def active_engines(self, active_engines):
        """Sets the active_engines of this SlotStat.

        Number of engines that are busy with this  # noqa: E501

        :param active_engines: The active_engines of this SlotStat.  # noqa: E501
        :type: int
        """

        self._active_engines = active_engines

    @property
    def active_streams(self):
        """Gets the active_streams of this SlotStat.  # noqa: E501

        Number of currently active streams  # noqa: E501

        :return: The active_streams of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._active_streams

    @active_streams.setter
    def active_streams(self, active_streams):
        """Sets the active_streams of this SlotStat.

        Number of currently active streams  # noqa: E501

        :param active_streams: The active_streams of this SlotStat.  # noqa: E501
        :type: int
        """

        self._active_streams = active_streams

    @property
    def bytes_failed(self):
        """Gets the bytes_failed of this SlotStat.  # noqa: E501


        :return: The bytes_failed of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_failed

    @bytes_failed.setter
    def bytes_failed(self, bytes_failed):
        """Sets the bytes_failed of this SlotStat.


        :param bytes_failed: The bytes_failed of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_failed = bytes_failed

    @property
    def bytes_glacier_restore_started(self):
        """Gets the bytes_glacier_restore_started of this SlotStat.  # noqa: E501


        :return: The bytes_glacier_restore_started of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_glacier_restore_started

    @bytes_glacier_restore_started.setter
    def bytes_glacier_restore_started(self, bytes_glacier_restore_started):
        """Sets the bytes_glacier_restore_started of this SlotStat.


        :param bytes_glacier_restore_started: The bytes_glacier_restore_started of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_glacier_restore_started = bytes_glacier_restore_started

    @property
    def bytes_not_matching_pattern(self):
        """Gets the bytes_not_matching_pattern of this SlotStat.  # noqa: E501


        :return: The bytes_not_matching_pattern of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_not_matching_pattern

    @bytes_not_matching_pattern.setter
    def bytes_not_matching_pattern(self, bytes_not_matching_pattern):
        """Sets the bytes_not_matching_pattern of this SlotStat.


        :param bytes_not_matching_pattern: The bytes_not_matching_pattern of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_not_matching_pattern = bytes_not_matching_pattern

    @property
    def bytes_processed(self):
        """Gets the bytes_processed of this SlotStat.  # noqa: E501


        :return: The bytes_processed of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_processed

    @bytes_processed.setter
    def bytes_processed(self, bytes_processed):
        """Sets the bytes_processed of this SlotStat.


        :param bytes_processed: The bytes_processed of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_processed = bytes_processed

    @property
    def bytes_skipped(self):
        """Gets the bytes_skipped of this SlotStat.  # noqa: E501


        :return: The bytes_skipped of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_skipped

    @bytes_skipped.setter
    def bytes_skipped(self, bytes_skipped):
        """Sets the bytes_skipped of this SlotStat.


        :param bytes_skipped: The bytes_skipped of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_skipped = bytes_skipped

    @property
    def bytes_skipped_glacier(self):
        """Gets the bytes_skipped_glacier of this SlotStat.  # noqa: E501


        :return: The bytes_skipped_glacier of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_skipped_glacier

    @bytes_skipped_glacier.setter
    def bytes_skipped_glacier(self, bytes_skipped_glacier):
        """Sets the bytes_skipped_glacier of this SlotStat.


        :param bytes_skipped_glacier: The bytes_skipped_glacier of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_skipped_glacier = bytes_skipped_glacier

    @property
    def bytes_uploaded(self):
        """Gets the bytes_uploaded of this SlotStat.  # noqa: E501


        :return: The bytes_uploaded of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._bytes_uploaded

    @bytes_uploaded.setter
    def bytes_uploaded(self, bytes_uploaded):
        """Sets the bytes_uploaded of this SlotStat.


        :param bytes_uploaded: The bytes_uploaded of this SlotStat.  # noqa: E501
        :type: int
        """

        self._bytes_uploaded = bytes_uploaded

    @property
    def dst_region(self):
        """Gets the dst_region of this SlotStat.  # noqa: E501


        :return: The dst_region of this SlotStat.  # noqa: E501
        :rtype: str
        """
        return self._dst_region

    @dst_region.setter
    def dst_region(self, dst_region):
        """Sets the dst_region of this SlotStat.


        :param dst_region: The dst_region of this SlotStat.  # noqa: E501
        :type: str
        """

        self._dst_region = dst_region

    @property
    def finished(self):
        """Gets the finished of this SlotStat.  # noqa: E501

        Finished time  # noqa: E501

        :return: The finished of this SlotStat.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this SlotStat.

        Finished time  # noqa: E501

        :param finished: The finished of this SlotStat.  # noqa: E501
        :type: datetime
        """

        self._finished = finished

    @property
    def objects_failed(self):
        """Gets the objects_failed of this SlotStat.  # noqa: E501


        :return: The objects_failed of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_failed

    @objects_failed.setter
    def objects_failed(self, objects_failed):
        """Sets the objects_failed of this SlotStat.


        :param objects_failed: The objects_failed of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_failed = objects_failed

    @property
    def objects_glacier_restore_started(self):
        """Gets the objects_glacier_restore_started of this SlotStat.  # noqa: E501


        :return: The objects_glacier_restore_started of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_glacier_restore_started

    @objects_glacier_restore_started.setter
    def objects_glacier_restore_started(self, objects_glacier_restore_started):
        """Sets the objects_glacier_restore_started of this SlotStat.


        :param objects_glacier_restore_started: The objects_glacier_restore_started of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_glacier_restore_started = objects_glacier_restore_started

    @property
    def objects_not_matching_pattern(self):
        """Gets the objects_not_matching_pattern of this SlotStat.  # noqa: E501


        :return: The objects_not_matching_pattern of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_not_matching_pattern

    @objects_not_matching_pattern.setter
    def objects_not_matching_pattern(self, objects_not_matching_pattern):
        """Sets the objects_not_matching_pattern of this SlotStat.


        :param objects_not_matching_pattern: The objects_not_matching_pattern of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_not_matching_pattern = objects_not_matching_pattern

    @property
    def objects_processed(self):
        """Gets the objects_processed of this SlotStat.  # noqa: E501


        :return: The objects_processed of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_processed

    @objects_processed.setter
    def objects_processed(self, objects_processed):
        """Sets the objects_processed of this SlotStat.


        :param objects_processed: The objects_processed of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_processed = objects_processed

    @property
    def objects_skipped(self):
        """Gets the objects_skipped of this SlotStat.  # noqa: E501


        :return: The objects_skipped of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_skipped

    @objects_skipped.setter
    def objects_skipped(self, objects_skipped):
        """Sets the objects_skipped of this SlotStat.


        :param objects_skipped: The objects_skipped of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_skipped = objects_skipped

    @property
    def objects_skipped_glacier(self):
        """Gets the objects_skipped_glacier of this SlotStat.  # noqa: E501


        :return: The objects_skipped_glacier of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_skipped_glacier

    @objects_skipped_glacier.setter
    def objects_skipped_glacier(self, objects_skipped_glacier):
        """Sets the objects_skipped_glacier of this SlotStat.


        :param objects_skipped_glacier: The objects_skipped_glacier of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_skipped_glacier = objects_skipped_glacier

    @property
    def objects_uploaded(self):
        """Gets the objects_uploaded of this SlotStat.  # noqa: E501


        :return: The objects_uploaded of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._objects_uploaded

    @objects_uploaded.setter
    def objects_uploaded(self, objects_uploaded):
        """Sets the objects_uploaded of this SlotStat.


        :param objects_uploaded: The objects_uploaded of this SlotStat.  # noqa: E501
        :type: int
        """

        self._objects_uploaded = objects_uploaded

    @property
    def processing_objects_per_second(self):
        """Gets the processing_objects_per_second of this SlotStat.  # noqa: E501

        Objects/second processed  # noqa: E501

        :return: The processing_objects_per_second of this SlotStat.  # noqa: E501
        :rtype: float
        """
        return self._processing_objects_per_second

    @processing_objects_per_second.setter
    def processing_objects_per_second(self, processing_objects_per_second):
        """Sets the processing_objects_per_second of this SlotStat.

        Objects/second processed  # noqa: E501

        :param processing_objects_per_second: The processing_objects_per_second of this SlotStat.  # noqa: E501
        :type: float
        """

        self._processing_objects_per_second = processing_objects_per_second

    @property
    def retried(self):
        """Gets the retried of this SlotStat.  # noqa: E501

        Number of retries  # noqa: E501

        :return: The retried of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._retried

    @retried.setter
    def retried(self, retried):
        """Sets the retried of this SlotStat.

        Number of retries  # noqa: E501

        :param retried: The retried of this SlotStat.  # noqa: E501
        :type: int
        """

        self._retried = retried

    @property
    def src_region(self):
        """Gets the src_region of this SlotStat.  # noqa: E501


        :return: The src_region of this SlotStat.  # noqa: E501
        :rtype: str
        """
        return self._src_region

    @src_region.setter
    def src_region(self, src_region):
        """Sets the src_region of this SlotStat.


        :param src_region: The src_region of this SlotStat.  # noqa: E501
        :type: str
        """

        self._src_region = src_region

    @property
    def started(self):
        """Gets the started of this SlotStat.  # noqa: E501

        Started time  # noqa: E501

        :return: The started of this SlotStat.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this SlotStat.

        Started time  # noqa: E501

        :param started: The started of this SlotStat.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def state(self):
        """Gets the state of this SlotStat.  # noqa: E501

        State of migration on its part  # noqa: E501

        :return: The state of this SlotStat.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SlotStat.

        State of migration on its part  # noqa: E501

        :param state: The state of this SlotStat.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEPLOYING", "FAILED", "IN_PROGRESS", "NO_CONNECTION_TO_ENGINE", "RESTARTING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "WAITING"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def total_upload(self):
        """Gets the total_upload of this SlotStat.  # noqa: E501


        :return: The total_upload of this SlotStat.  # noqa: E501
        :rtype: int
        """
        return self._total_upload

    @total_upload.setter
    def total_upload(self, total_upload):
        """Sets the total_upload of this SlotStat.


        :param total_upload: The total_upload of this SlotStat.  # noqa: E501
        :type: int
        """

        self._total_upload = total_upload

    @property
    def uploading_bytes_per_second(self):
        """Gets the uploading_bytes_per_second of this SlotStat.  # noqa: E501


        :return: The uploading_bytes_per_second of this SlotStat.  # noqa: E501
        :rtype: float
        """
        return self._uploading_bytes_per_second

    @uploading_bytes_per_second.setter
    def uploading_bytes_per_second(self, uploading_bytes_per_second):
        """Sets the uploading_bytes_per_second of this SlotStat.


        :param uploading_bytes_per_second: The uploading_bytes_per_second of this SlotStat.  # noqa: E501
        :type: float
        """

        self._uploading_bytes_per_second = uploading_bytes_per_second

    @property
    def uploading_objects_per_second(self):
        """Gets the uploading_objects_per_second of this SlotStat.  # noqa: E501


        :return: The uploading_objects_per_second of this SlotStat.  # noqa: E501
        :rtype: float
        """
        return self._uploading_objects_per_second

    @uploading_objects_per_second.setter
    def uploading_objects_per_second(self, uploading_objects_per_second):
        """Sets the uploading_objects_per_second of this SlotStat.


        :param uploading_objects_per_second: The uploading_objects_per_second of this SlotStat.  # noqa: E501
        :type: float
        """

        self._uploading_objects_per_second = uploading_objects_per_second

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
        if issubclass(SlotStat, dict):
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
        if not isinstance(other, SlotStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
