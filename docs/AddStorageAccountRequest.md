# AddStorageAccountRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_account** | [**NewStorageAccount**](NewStorageAccount.md) | Storage account to create | [optional] 
**include_buckets** | **list[str]** | Lists of buckets to start monitoring, or null to request buckets from the cloud | [optional] 
**verify** | **bool** | Specified if credentials or public access to included buckets should be checked | [optional] 
**refresh_now** | **bool** | If set to true, buckets will be refreshed after storage is added | [optional] 
**endpoint_id** | **int** | ID of the user endpoint to add storages to. Do not set the value if you want to attach storages to the endpoint later | [optional] 
**put_objects** | **bool** | Specifies if new data should be stored to added storages | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


