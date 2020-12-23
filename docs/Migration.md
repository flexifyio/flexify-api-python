# Migration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_deployed_engines_cloud_name** | **str** | The name of cloud used to auto deploy engines. All engines are auto deployed to the same cloud. | [optional] 
**auto_deployed_engines_cloud_region** | **str** | The name of cloud region used to auto deploy engines. All engines are auto deployed to the same cloud region. | [optional] 
**hidden** | **bool** | Indicates that his migration should not be show in UI | [optional] 
**id** | **int** | Unique ID | [optional] 
**mappings** | [**list[Mapping]**](Mapping.md) | Source to destination storages mappings | [optional] 
**settings** | [**MigrationSettingsRes**](MigrationSettingsRes.md) | Migration settings | [optional] 
**stat** | [**MigrationStat**](MigrationStat.md) | Cumulative migration statistics | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


