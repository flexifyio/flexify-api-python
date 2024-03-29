# Mapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_bucket** | [**Bucket**](Bucket.md) | Destination bucket/container | 
**dest_bucket_new_region** | **str** | Region where bucket should be created if missing | [optional] 
**dest_storage_account** | [**StorageAccount**](StorageAccount.md) | Destination storage account | 
**id** | **int** | ID of this mapping | 
**key_add_prefix** | **str** | Prefix added to each object key | [optional] 
**key_remove_prefix** | **str** | Prefix removed from each object key | [optional] 
**objects_list_uri** | **str** | URI of a text file with a list of objects to migrate | [optional] 
**selected_comparison_method** | **str** | Method selected for comparison | [optional] 
**slots** | [**list[Slot]**](Slot.md) | Slots that this mapping is split into | 
**source_bucket** | [**Bucket**](Bucket.md) | Source bucket/container | 
**source_storage_account** | [**StorageAccount**](StorageAccount.md) | Source storage account | 
**stat** | [**MappingStat**](MappingStat.md) | Cumulative statistics of this mapping | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


