# StorageProvider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_region** | **str** | Default region for this provider | [optional] 
**disabled_as_destination** | **bool** | Storage is not allowed to be used as a default storage in endpoint or as a migration destination) | [optional] 
**dot_encode** | **str** | Indicates that the privder does not support dots in bucket names and how dots should be encoded | [optional] 
**endpoint** | **str** | Endpoint to access this provider or null for custom providers | [optional] 
**id** | **int** | Id of the provider in the system | [optional] 
**name** | **str** | Name of the provider | [optional] 
**port_http** | **int** | Port for HTTP request (null for default 80) | [optional] 
**port_https** | **int** | Port for HTTPS request (null for default 443) | [optional] 
**product_name** | **str** | Name of product/region for this provider | [optional] 
**protocol** | **str** | Storage protocol this provider uses | [optional] 
**regions** | **list[str]** | List of regions supported for this provider (or null if regions are not supported | [optional] 
**supports_http** | **bool** | Indicates that HTTP is supported | [optional] 
**supports_https** | **bool** | Indicates that HTTPS (SSL) is supported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


