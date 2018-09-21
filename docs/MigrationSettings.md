# MigrationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflict_resolution** | **str** | Conflict resolution | 
**count_source_objects** | **bool** | Count objects in source before migration | [optional] 
**engines_location** | [**CloudLocation**](CloudLocation.md) | Location of the engines to migrate | [optional] 
**existing_data_in_destination** | **str** | Keep or clean data in destination before migration (identical with source objects keep in any cases) | [optional] 
**max_active_slots** | **int** | Maximum number of slots that can be migrated simultaneously | [optional] 
**max_streams_per_slot** | **int** | Maximum Connections per engine | [optional] 
**migration_mode** | **str** | Migration mode | 
**name** | **str** | Name of the migration | 
**object_key_filter** | **str** | Migrate objects matching pattern | [optional] 
**slots_per_mapping** | **int** | Number of slots of storage mapping (bucket) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


