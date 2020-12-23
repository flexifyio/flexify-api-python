# AddStorageAccountRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_buckets** | **list[str]** | Lists of buckets to start monitoring, or null to request buckets from the cloud | [optional] 
**refresh_now** | **bool** | If set to true, buckets will be refreshed after storage is added | [optional] 
**storage_account** | [**NewStorageAccount**](NewStorageAccount.md) | Storage account to create | [optional] 
**verify** | **bool** | Specified if credentials or public access to included buckets should be checked | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


