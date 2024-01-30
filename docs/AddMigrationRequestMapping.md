# AddMigrationRequestMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdn_url** | **str** | CDN base URL for GET operations during migration | [optional] 
**dest_bucket_name** | **str** | Name of source destination or container | 
**dest_bucket_new_region** | **str** | Region where the destination bucket will be created if it does not exist. null to use cloud&#39;s default region | [optional] 
**dest_storage_account_id** | **int** | ID of source destination account | 
**key_add_prefix** | **str** | Prefix to to be added to each key when migrating | [optional] 
**key_remove_prefix** | **str** | Prefix to to be removed from each key when migrating | [optional] 
**objects_list_uri** | **str** | A URI of a text file to take objects list from | [optional] 
**source_bucket_name** | **str** | Name of source bucket or container | 
**source_storage_account_id** | **int** | ID of source storage account | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


