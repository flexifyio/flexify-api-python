# MigrationSettingsReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflict_resolution** | **str** | Conflict resolution | [optional] 
**deployment_type** | **str** | The type of engine deployment | [optional] 
**dry_run** | **bool** | Dry run mode | [optional] 
**engines_location** | [**CloudLocationReq**](CloudLocationReq.md) | Location of the engines to migrate | [optional] 
**existing_data_in_destination** | **str** | Keep or clean data in destination before migration (identical with source objects keep in any cases) | [optional] 
**last_modified_from** | **datetime** | Migrate objects modified on or after specified date | [optional] 
**max_engines** | **int** | Maximum number of engines this migration uses (experimental) | [optional] 
**max_retries** | **int** | Maximum number of retries | [optional] 
**max_retries_for_copy** | **int** | Maximum number of retries after copy started | [optional] 
**max_retry_timeout** | **int** | Maximum timeout between retries in seconds | [optional] 
**max_streams** | **int** | Maximum streams that migration will use across all engines | [optional] 
**migration_mode** | **str** | Migration mode | [optional] 
**multipart_concurrency** | **int** | Maximum parts for parallel upload for a single object | [optional] 
**multipart_limit** | **int** | Minimum size in bytes for multipart upload | [optional] 
**multipart_part_size** | **int** | Part size for multipart upload | [optional] 
**name** | **str** | Name of the migration | [optional] 
**object_key_filter** | **str** | Migrate objects matching pattern | [optional] 
**retry_timeout** | **int** | Initial timeout between retries in seconds | [optional] 
**skip_if_hash_matches** | **bool** | Skip migration if source and destination object hash match | [optional] 
**slots_per_mapping** | **int** | Number of slots of storage mapping (bucket) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


