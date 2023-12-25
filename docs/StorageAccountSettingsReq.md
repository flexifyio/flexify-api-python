# StorageAccountSettingsReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_integration_id** | **int** | Id of Azure integration | [optional] 
**bucket_dot_encode_sequence** | **str** | Dot escape sequence for buckets | [optional] 
**credential** | **str** | Credential (such as Secret Key) of the cloud account | [optional] 
**custom_endpoint** | **str** | Custom endpoint to be used for requests | [optional] 
**identity** | **str** | Identity (such as Key ID) of the cloud account | [optional] 
**name** | **str** | User-defined storage account name | [optional] 
**refresh_interval_sec** | **int** | Automatic refresh interval in seconds or null to disable automatic refresh | [optional] 
**refresh_storages_stat** | **bool** | Indicates if statistics for each bucket/container should be calculated on automatic refresh | [optional] 
**use_ssl** | **bool** | Encrypt transfer with SSL | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


