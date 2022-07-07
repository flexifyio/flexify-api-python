# MigrationStat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_engines** | **int** | Number of engines that are busy with this | [optional] 
**active_slots** | **int** | Number fo currently active slots | [optional] 
**active_streams** | **int** | Number of currently active streams | [optional] 
**bytes_failed** | **int** |  | [optional] 
**bytes_glacier_restore_started** | **int** |  | [optional] 
**bytes_not_matching_pattern** | **int** |  | [optional] 
**bytes_processed** | **int** |  | [optional] 
**bytes_skipped** | **int** |  | [optional] 
**bytes_skipped_glacier** | **int** |  | [optional] 
**bytes_uploaded** | **int** |  | [optional] 
**cleanup** | [**CleanupStat**](CleanupStat.md) | Cleanup that may be performed before migration | [optional] 
**created** | **datetime** | Creation time | [optional] 
**dst_region** | **str** |  | [optional] 
**estimated** | **datetime** | Estimated finish time | [optional] 
**finished** | **datetime** | Finished time | [optional] 
**initial_bytes** | **int** | Initial size of all objects in source storage (if known) | [optional] 
**initial_objects** | **int** | Initial number of objects in source storage (if known) | [optional] 
**objects_failed** | **int** |  | [optional] 
**objects_glacier_restore_started** | **int** |  | [optional] 
**objects_not_matching_pattern** | **int** |  | [optional] 
**objects_processed** | **int** |  | [optional] 
**objects_skipped** | **int** |  | [optional] 
**objects_skipped_glacier** | **int** |  | [optional] 
**objects_uploaded** | **int** |  | [optional] 
**processing_objects_per_second** | **float** | Objects/second processed | [optional] 
**progress** | **float** | Progress from 0.0 to 1.0 | [optional] 
**retried** | **int** | Number of retries | [optional] 
**src_region** | **str** |  | [optional] 
**started** | **datetime** | Started time | [optional] 
**state** | **str** | State of migration on its part | [optional] 
**step** | **str** | Step that this mapping is currently doing | [optional] 
**total_upload** | **int** |  | [optional] 
**uploading_bytes_per_second** | **float** |  | [optional] 
**uploading_objects_per_second** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


