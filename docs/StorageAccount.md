# StorageAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the storage account | [optional] 
**is_sas** | **bool** | For Azure - if credential is SAS signature (not included if storing in key vault) | [optional] 
**key_vault_secret_id** | **str** | Key Vault secret ID where this credential secret is stored (only for admins) | [optional] 
**private_url** | **str** | URL used by engines to access the cloud | [optional] 
**provider** | [**StorageProvider**](StorageProvider.md) | Link to the storage provider (Amazon, Azure, etc) | [optional] 
**secret_in_key_vault** | **bool** | If secret credential is stored in Key Vault | [optional] 
**settings** | [**StorageAccountSettingsRes**](StorageAccountSettingsRes.md) | Configuration of this storage account | [optional] 
**stat** | [**StorageAccountStat**](StorageAccountStat.md) | Storage account state and statistics | [optional] 
**url** | **str** | URL to the cloud | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


