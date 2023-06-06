# StorageAccountWithBuckets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_key_vault_secret_id** | **str** |  | [optional] 
**buckets** | [**list[Bucket]**](Bucket.md) | Buckets that we have cached for this storage account | [optional] 
**id** | **int** | Id of the storage account | [optional] 
**is_sas** | **bool** |  | [optional] 
**private_url** | **str** | URL used by engines to access the cloud | [optional] 
**provider** | [**StorageProvider**](StorageProvider.md) | Link to the storage provider (Amazon, Azure, etc) | [optional] 
**settings** | [**StorageAccountSettingsRes**](StorageAccountSettingsRes.md) | Configuration of this storage account | [optional] 
**stat** | [**StorageAccountStat**](StorageAccountStat.md) | Storage account state and statistics | [optional] 
**url** | **str** | URL to the cloud | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


