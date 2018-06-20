# Migration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflict_resolution** | **str** | Conflict resolution | 
**count_source_objects** | **bool** | Count objects in source before migration | [optional] 
**destination_storage** | [**Storage**](Storage.md) | Destination storage | 
**destination_storage_account** | [**StorageAccount**](StorageAccount.md) | Destination storage account | 
**engines_location** | [**CloudLocation**](CloudLocation.md) | Location of the engines to migrate | [optional] 
**existing_data_in_destination** | **str** | Keep or clean data in destination before migration (identical with source objects keep in any cases) | [optional] 
**hidden** | **bool** | Hide migration on UI | [optional] 
**id** | **int** | Unique identifier | [optional] 
**max_connections_per_engine** | **int** | Maximum Connections per engine | [optional] 
**migration_mode** | **str** | Migration mode | 
**name** | **str** | Name of the migration | 
**object_key_filter** | **str** | Migrate objects matching pattern | [optional] 
**slots** | **int** | Number of slots of migration | [optional] 
**source_storage** | [**Storage**](Storage.md) | Source storage | 
**source_storage_account** | [**StorageAccount**](StorageAccount.md) | Source storage account | 
**stat** | [**MigrationStat**](MigrationStat.md) | Migration statistics | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


