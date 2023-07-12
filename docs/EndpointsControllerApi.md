# flexify_api.EndpointsControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_accounts**](EndpointsControllerApi.md#attach_accounts) | **POST** /backend/rest/endpoints/{endpoint-id}/storage-accounts | Attach storage accounts to the endpoint
[**attach_buckets**](EndpointsControllerApi.md#attach_buckets) | **POST** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets | Attach storages to the virtual bucket
[**change_accounts**](EndpointsControllerApi.md#change_accounts) | **PUT** /backend/rest/endpoints/{endpoint-id}/storage-accounts | Modified all storage accounts to the endpoint
[**change_buckets**](EndpointsControllerApi.md#change_buckets) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets | Replaces the list of storages attached to the virtual bucket
[**create_endpoint**](EndpointsControllerApi.md#create_endpoint) | **POST** /backend/rest/endpoints | Creates new endpoint
[**create_virtual_bucket**](EndpointsControllerApi.md#create_virtual_bucket) | **POST** /backend/rest/endpoints/{endpoint-id}/virtual-buckets | Creates new virtual bucket
[**delete**](EndpointsControllerApi.md#delete) | **DELETE** /backend/rest/endpoints/{endpoint-id} | Delete the endpoint
[**delete_virtual_bucket**](EndpointsControllerApi.md#delete_virtual_bucket) | **DELETE** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket} | Deletes virtual bucket
[**detach_account**](EndpointsControllerApi.md#detach_account) | **DELETE** /backend/rest/endpoints/{endpoint-id}/storage-accounts/{storage-account-id} | Detach storage account from the endpoint
[**detach_bucket**](EndpointsControllerApi.md#detach_bucket) | **DELETE** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets/{bucket-id} | Detach storage account from the endpoint
[**disable**](EndpointsControllerApi.md#disable) | **PUT** /backend/rest/endpoints/{endpoint-id}/actions/disable | Disable the endpoint
[**enable**](EndpointsControllerApi.md#enable) | **PUT** /backend/rest/endpoints/{endpoint-id}/actions/enable | Enable the endpoint
[**generate_access_keys**](EndpointsControllerApi.md#generate_access_keys) | **GET** /backend/rest/endpoints/generated-access-keys | Generate new access keys pair
[**get_endpoint_details**](EndpointsControllerApi.md#get_endpoint_details) | **GET** /backend/rest/endpoints/{endpoint-id} | Get endpoint details
[**get_endpoint_secret_key**](EndpointsControllerApi.md#get_endpoint_secret_key) | **GET** /backend/rest/endpoints/{endpoint-id}/settings/secret-key | Get endpoint secret key
[**get_endpoints_for_current_user**](EndpointsControllerApi.md#get_endpoints_for_current_user) | **GET** /backend/rest/endpoints | Get the list of endpoints for current user optionally filtering by name or identity using SQL LIKE syntax
[**set_attached_account_settings**](EndpointsControllerApi.md#set_attached_account_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/storage-accounts/{storage-account-id}/settings | Modifies settings of the attached storage account
[**set_attached_bucket_settings**](EndpointsControllerApi.md#set_attached_bucket_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets/{bucket-id}/settings | Modifies settings of the attached storage
[**set_virtual_bucket_settings**](EndpointsControllerApi.md#set_virtual_bucket_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/settings | Modifies virtual bucket configuration
[**update_endpoint_settings**](EndpointsControllerApi.md#update_endpoint_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/settings | Update attributes of the endpoint


# **attach_accounts**
> attach_accounts(endpoint_id, request)

Attach storage accounts to the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
request = flexify_api.StorageAccountsRequest() # StorageAccountsRequest | request

try:
    # Attach storage accounts to the endpoint
    api_instance.attach_accounts(endpoint_id, request)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->attach_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **request** | [**StorageAccountsRequest**](StorageAccountsRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_buckets**
> attach_buckets(endpoint_id, request, virtual_bucket)

Attach storages to the virtual bucket

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
request = flexify_api.VirtualBucketStoragesRequest() # VirtualBucketStoragesRequest | request
virtual_bucket = 'virtual_bucket_example' # str | virtual-bucket

try:
    # Attach storages to the virtual bucket
    api_instance.attach_buckets(endpoint_id, request, virtual_bucket)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->attach_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **request** | [**VirtualBucketStoragesRequest**](VirtualBucketStoragesRequest.md)| request | 
 **virtual_bucket** | **str**| virtual-bucket | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_accounts**
> change_accounts(endpoint_id, request)

Modified all storage accounts to the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
request = flexify_api.StorageAccountsRequest() # StorageAccountsRequest | request

try:
    # Modified all storage accounts to the endpoint
    api_instance.change_accounts(endpoint_id, request)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->change_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **request** | [**StorageAccountsRequest**](StorageAccountsRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_buckets**
> change_buckets(endpoint_id, request, virtual_bucket)

Replaces the list of storages attached to the virtual bucket

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
request = flexify_api.VirtualBucketStoragesRequest() # VirtualBucketStoragesRequest | request
virtual_bucket = 'virtual_bucket_example' # str | virtual-bucket

try:
    # Replaces the list of storages attached to the virtual bucket
    api_instance.change_buckets(endpoint_id, request, virtual_bucket)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->change_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **request** | [**VirtualBucketStoragesRequest**](VirtualBucketStoragesRequest.md)| request | 
 **virtual_bucket** | **str**| virtual-bucket | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint**
> IdResponse create_endpoint(settings)

Creates new endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
settings = flexify_api.EndpointSettingsReq() # EndpointSettingsReq | settings

try:
    # Creates new endpoint
    api_response = api_instance.create_endpoint(settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->create_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**EndpointSettingsReq**](EndpointSettingsReq.md)| settings | 

### Return type

[**IdResponse**](IdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_bucket**
> create_virtual_bucket(endpoint_id, request)

Creates new virtual bucket

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
request = flexify_api.CreateVirtualBucketRequest() # CreateVirtualBucketRequest | request

try:
    # Creates new virtual bucket
    api_instance.create_virtual_bucket(endpoint_id, request)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->create_virtual_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **request** | [**CreateVirtualBucketRequest**](CreateVirtualBucketRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(endpoint_id)

Delete the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Delete the endpoint
    api_instance.delete(endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_bucket**
> delete_virtual_bucket(endpoint_id, virtual_bucket)

Deletes virtual bucket

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
virtual_bucket = 'virtual_bucket_example' # str | virtual-bucket

try:
    # Deletes virtual bucket
    api_instance.delete_virtual_bucket(endpoint_id, virtual_bucket)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->delete_virtual_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **virtual_bucket** | **str**| virtual-bucket | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_account**
> detach_account(endpoint_id, storage_account_id)

Detach storage account from the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
storage_account_id = 789 # int | storage-account-id

try:
    # Detach storage account from the endpoint
    api_instance.detach_account(endpoint_id, storage_account_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->detach_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **storage_account_id** | **int**| storage-account-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_bucket**
> detach_bucket(bucket_id, endpoint_id, virtual_bucket)

Detach storage account from the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
bucket_id = 789 # int | bucket-id
endpoint_id = 789 # int | endpoint-id
virtual_bucket = 'virtual_bucket_example' # str | virtual-bucket

try:
    # Detach storage account from the endpoint
    api_instance.detach_bucket(bucket_id, endpoint_id, virtual_bucket)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->detach_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket-id | 
 **endpoint_id** | **int**| endpoint-id | 
 **virtual_bucket** | **str**| virtual-bucket | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable**
> disable(endpoint_id)

Disable the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Disable the endpoint
    api_instance.disable(endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable**
> enable(endpoint_id)

Enable the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Enable the endpoint
    api_instance.enable(endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_access_keys**
> AccessKeysPair generate_access_keys()

Generate new access keys pair

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))

try:
    # Generate new access keys pair
    api_response = api_instance.generate_access_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->generate_access_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessKeysPair**](AccessKeysPair.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_details**
> EndpointDetails get_endpoint_details(endpoint_id)

Get endpoint details

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Get endpoint details
    api_response = api_instance.get_endpoint_details(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->get_endpoint_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

[**EndpointDetails**](EndpointDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_secret_key**
> EndpointSecretResponse get_endpoint_secret_key(endpoint_id)

Get endpoint secret key

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Get endpoint secret key
    api_response = api_instance.get_endpoint_secret_key(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->get_endpoint_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

[**EndpointSecretResponse**](EndpointSecretResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_for_current_user**
> list[EndpointDetails] get_endpoints_for_current_user(identity=identity, name=name)

Get the list of endpoints for current user optionally filtering by name or identity using SQL LIKE syntax

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
identity = 'identity_example' # str | identity (optional)
name = 'name_example' # str | name (optional)

try:
    # Get the list of endpoints for current user optionally filtering by name or identity using SQL LIKE syntax
    api_response = api_instance.get_endpoints_for_current_user(identity=identity, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->get_endpoints_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity** | **str**| identity | [optional] 
 **name** | **str**| name | [optional] 

### Return type

[**list[EndpointDetails]**](EndpointDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attached_account_settings**
> set_attached_account_settings(endpoint_id, settings, storage_account_id)

Modifies settings of the attached storage account

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
settings = flexify_api.EndpointStorageAccountSettings() # EndpointStorageAccountSettings | settings
storage_account_id = 789 # int | storage-account-id

try:
    # Modifies settings of the attached storage account
    api_instance.set_attached_account_settings(endpoint_id, settings, storage_account_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->set_attached_account_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **settings** | [**EndpointStorageAccountSettings**](EndpointStorageAccountSettings.md)| settings | 
 **storage_account_id** | **int**| storage-account-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attached_bucket_settings**
> set_attached_bucket_settings(bucket_id, endpoint_id, settings, virtual_bucket)

Modifies settings of the attached storage

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
bucket_id = 789 # int | bucket-id
endpoint_id = 789 # int | endpoint-id
settings = flexify_api.VirtualBucketStorageSettings() # VirtualBucketStorageSettings | settings
virtual_bucket = 'virtual_bucket_example' # str | virtual-bucket

try:
    # Modifies settings of the attached storage
    api_instance.set_attached_bucket_settings(bucket_id, endpoint_id, settings, virtual_bucket)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->set_attached_bucket_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket-id | 
 **endpoint_id** | **int**| endpoint-id | 
 **settings** | [**VirtualBucketStorageSettings**](VirtualBucketStorageSettings.md)| settings | 
 **virtual_bucket** | **str**| virtual-bucket | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_virtual_bucket_settings**
> set_virtual_bucket_settings(endpoint_id, settings, virtual_bucket)

Modifies virtual bucket configuration

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
settings = flexify_api.VirtualBucketSettings() # VirtualBucketSettings | settings
virtual_bucket = 'virtual_bucket_example' # str | virtual-bucket

try:
    # Modifies virtual bucket configuration
    api_instance.set_virtual_bucket_settings(endpoint_id, settings, virtual_bucket)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->set_virtual_bucket_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **settings** | [**VirtualBucketSettings**](VirtualBucketSettings.md)| settings | 
 **virtual_bucket** | **str**| virtual-bucket | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint_settings**
> update_endpoint_settings(endpoint_id, settings)

Update attributes of the endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api.EndpointsControllerApi(flexify_api.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
settings = flexify_api.EndpointSettingsReq() # EndpointSettingsReq | settings

try:
    # Update attributes of the endpoint
    api_instance.update_endpoint_settings(endpoint_id, settings)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->update_endpoint_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **settings** | [**EndpointSettingsReq**](EndpointSettingsReq.md)| settings | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

