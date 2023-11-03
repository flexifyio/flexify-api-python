# StorageProvider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_overwrite_endpoint** | **bool** | If customEndpoint can be used to overwrite the default endpoint | [optional] 
**bucket_dot_encode** | **bool** | Indicates that the provider does not support dots in bucket names and how dots should be encoded | [optional] 
**can_create_buckets_with_uppercase** | **bool** | Indicates that this provider allow creating bucket with uppercase in names | [optional] 
**code** | **str** | Code of this cloud provider | [optional] 
**default_region** | **str** | Default region for this provider | [optional] 
**disabled_as_destination** | **bool** | Storage is not allowed to be used as a default storage in endpoint or as a migration destination) | [optional] 
**endpoint** | **str** | Endpoint to access this provider or null for custom providers | [optional] 
**endpoint_pattern** | **str** | Endpoint pattern to access specific region of this provider | [optional] 
**id** | **int** | Id of the provider in the system | [optional] 
**max_upload_size** | **int** | Maximum size of a single upload w/o multipart | [optional] 
**multi_regional** | **bool** | This cloud provider supports multiple regions | [optional] 
**name** | **str** | Name of the provider | [optional] 
**port_http** | **int** | Port for HTTP request (null for default 80) | [optional] 
**port_https** | **int** | Port for HTTPS request (null for default 443) | [optional] 
**private_endpoint** | **str** | Endpoint used by engines (or null if only public endpoint is used) | [optional] 
**private_endpoint_pattern** | **str** | Endpoint pattern used by engines for specific region | [optional] 
**product_name** | **str** | Name of product/region for this provider | [optional] 
**protocol** | **str** | Storage protocol this provider uses | [optional] 
**supported_o_auth_providers** | **list[str]** | The list of OAuth providers that can be used with this storage provider (instead of storage keys) | [optional] 
**supports_credential** | **bool** | If the provider supports auth with credential (storage keys) | [optional] 
**supports_http** | **bool** | Indicates that HTTP is supported | [optional] 
**supports_https** | **bool** | Indicates that HTTPS (SSL) is supported | [optional] 
**supports_multipart_upload** | **bool** | Indicates that the provider supports multipart upload | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


