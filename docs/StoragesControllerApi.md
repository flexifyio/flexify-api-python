# flexify_api.StoragesControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_buckets**](StoragesControllerApi.md#add_buckets) | **POST** /rest/storage-accounts/{storage-account-id}/buckets | Add buckets to the storage account
[**add_storage_account**](StoragesControllerApi.md#add_storage_account) | **POST** /rest/storage-accounts | Add Storage Account with an optional list of buckets
[**delete_bucket**](StoragesControllerApi.md#delete_bucket) | **DELETE** /rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Deletes (hides) a bucket/container
[**delete_buckets**](StoragesControllerApi.md#delete_buckets) | **POST** /rest/storage-accounts/actions/delete-buckets | Deletes (hides) multiple buckets/containers
[**generate_access_keys**](StoragesControllerApi.md#generate_access_keys) | **GET** /rest/generate-access-keys | Generate new access keys pair
[**get_buckets**](StoragesControllerApi.md#get_buckets) | **GET** /rest/storage-accounts/{storage-account-id}/buckets | Get registered non-hidden bukects/containers of the storage account
[**get_providers**](StoragesControllerApi.md#get_providers) | **GET** /rest/providers | Get all storage providers
[**get_storage_accounts**](StoragesControllerApi.md#get_storage_accounts) | **GET** /rest/storage-accounts | Get all storage accounts for current user
[**refresh_bucket**](StoragesControllerApi.md#refresh_bucket) | **POST** /rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}/actions/refresh | Refresh statistics of a single bucket
[**refresh_buckets**](StoragesControllerApi.md#refresh_buckets) | **POST** /rest/storage-accounts/actions/refresh-buckets | Refresh statistics of multiple buckets
[**request_buckets**](StoragesControllerApi.md#request_buckets) | **GET** /rest/buckets | Lists buckets of the external storage account
[**request_cloud_buckets**](StoragesControllerApi.md#request_cloud_buckets) | **GET** /rest/storage-accounts/{storage-account-id}/cloud/buckets | Retrieve buckets/containers list from underlying cloud
[**set_buckets**](StoragesControllerApi.md#set_buckets) | **PUT** /rest/storage-accounts/{storage-account-id}/buckets | Sets a list of bucket for a storage account (hides existing buckets not in a list and adds buckets not in a list)


# **add_buckets**
> IdsList add_buckets(storage_account_id, request)

Add buckets to the storage account

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
request = flexify_api.BucketsRequest() # BucketsRequest | request

try:
    # Add buckets to the storage account
    api_response = api_instance.add_buckets(storage_account_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->add_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **request** | [**BucketsRequest**](BucketsRequest.md)| request | 

### Return type

[**IdsList**](IdsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_storage_account**
> IdResponse add_storage_account(request)

Add Storage Account with an optional list of buckets

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.AddStorageAccountRequest() # AddStorageAccountRequest | request

try:
    # Add Storage Account with an optional list of buckets
    api_response = api_instance.add_storage_account(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->add_storage_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AddStorageAccountRequest**](AddStorageAccountRequest.md)| request | 

### Return type

[**IdResponse**](IdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> delete_bucket(storage_account_id, bucket_id)

Deletes (hides) a bucket/container

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
bucket_id = 789 # int | bucket-id

try:
    # Deletes (hides) a bucket/container
    api_instance.delete_bucket(storage_account_id, bucket_id)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->delete_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **bucket_id** | **int**| bucket-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_buckets**
> delete_buckets(request)

Deletes (hides) multiple buckets/containers

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.IdsList() # IdsList | request

try:
    # Deletes (hides) multiple buckets/containers
    api_instance.delete_buckets(request)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->delete_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IdsList**](IdsList.md)| request | 

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))

try:
    # Generate new access keys pair
    api_response = api_instance.generate_access_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->generate_access_keys: %s\n" % e)
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

# **get_buckets**
> list[Bucket] get_buckets(storage_account_id)

Get registered non-hidden bukects/containers of the storage account

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id

try:
    # Get registered non-hidden bukects/containers of the storage account
    api_response = api_instance.get_buckets(storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->get_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 

### Return type

[**list[Bucket]**](Bucket.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> list[StorageProvider] get_providers()

Get all storage providers

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get all storage providers
    api_response = api_instance.get_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->get_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StorageProvider]**](StorageProvider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_accounts**
> list[StorageAccount] get_storage_accounts(include_storages=include_storages)

Get all storage accounts for current user

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
include_storages = true # bool | Include storages of given storage account to the response (optional) (default to true)

try:
    # Get all storage accounts for current user
    api_response = api_instance.get_storage_accounts(include_storages=include_storages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->get_storage_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_storages** | **bool**| Include storages of given storage account to the response | [optional] [default to true]

### Return type

[**list[StorageAccount]**](StorageAccount.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_bucket**
> refresh_bucket(storage_account_id, bucket_id)

Refresh statistics of a single bucket

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
bucket_id = 789 # int | bucket-id

try:
    # Refresh statistics of a single bucket
    api_instance.refresh_bucket(storage_account_id, bucket_id)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->refresh_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **bucket_id** | **int**| bucket-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_buckets**
> refresh_buckets(request)

Refresh statistics of multiple buckets

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.IdsList() # IdsList | request

try:
    # Refresh statistics of multiple buckets
    api_instance.refresh_buckets(request)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->refresh_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IdsList**](IdsList.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_buckets**
> list[Bucket] request_buckets(provider_id=provider_id, identity=identity, credential=credential, custom_url=custom_url, use_ssl=use_ssl)

Lists buckets of the external storage account

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
provider_id = 789 # int | Provider ID (Amazon S3, Microsoft Azure, etc) (optional)
identity = 'identity_example' # str | Account Identity (optional)
credential = 'credential_example' # str | Account Credential (optional)
custom_url = 'custom_url_example' # str | Optional endpoint to access the storage (optional)
use_ssl = true # bool | Use SSL to connect to the endpoint (optional) (default to true)

try:
    # Lists buckets of the external storage account
    api_response = api_instance.request_buckets(provider_id=provider_id, identity=identity, credential=credential, custom_url=custom_url, use_ssl=use_ssl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->request_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| Provider ID (Amazon S3, Microsoft Azure, etc) | [optional] 
 **identity** | **str**| Account Identity | [optional] 
 **credential** | **str**| Account Credential | [optional] 
 **custom_url** | **str**| Optional endpoint to access the storage | [optional] 
 **use_ssl** | **bool**| Use SSL to connect to the endpoint | [optional] [default to true]

### Return type

[**list[Bucket]**](Bucket.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_cloud_buckets**
> list[Bucket] request_cloud_buckets(storage_account_id)

Retrieve buckets/containers list from underlying cloud

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id

try:
    # Retrieve buckets/containers list from underlying cloud
    api_response = api_instance.request_cloud_buckets(storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->request_cloud_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 

### Return type

[**list[Bucket]**](Bucket.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_buckets**
> IdsList set_buckets(storage_account_id, request)

Sets a list of bucket for a storage account (hides existing buckets not in a list and adds buckets not in a list)

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
api_instance = flexify_api.StoragesControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
request = flexify_api.BucketsRequest() # BucketsRequest | request

try:
    # Sets a list of bucket for a storage account (hides existing buckets not in a list and adds buckets not in a list)
    api_response = api_instance.set_buckets(storage_account_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->set_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **request** | [**BucketsRequest**](BucketsRequest.md)| request | 

### Return type

[**IdsList**](IdsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

