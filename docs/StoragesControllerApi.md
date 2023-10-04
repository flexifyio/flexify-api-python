# flexify_api.StoragesControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_buckets**](StoragesControllerApi.md#add_buckets) | **POST** /backend/rest/storage-accounts/{storage-account-id}/buckets | Add buckets to the storage account
[**delete_bucket**](StoragesControllerApi.md#delete_bucket) | **DELETE** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Deletes (hides) a bucket/container
[**get_bucket**](StoragesControllerApi.md#get_bucket) | **GET** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Get detailed stats for the bucket
[**refresh_bucket**](StoragesControllerApi.md#refresh_bucket) | **POST** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}/actions/refresh | Refresh statistics of a single bucket


# **add_buckets**
> IdsList add_buckets(request, storage_account_id)

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
request = flexify_api.AddBucketsRequest() # AddBucketsRequest | request
storage_account_id = 789 # int | storage-account-id

try:
    # Add buckets to the storage account
    api_response = api_instance.add_buckets(request, storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->add_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AddBucketsRequest**](AddBucketsRequest.md)| request | 
 **storage_account_id** | **int**| storage-account-id | 

### Return type

[**IdsList**](IdsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> delete_bucket(bucket_id, storage_account_id, force_detach=force_detach)

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
bucket_id = 789 # int | bucket-id
storage_account_id = 789 # int | storage-account-id
force_detach = false # bool | force-detach (optional) (default to false)

try:
    # Deletes (hides) a bucket/container
    api_instance.delete_bucket(bucket_id, storage_account_id, force_detach=force_detach)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->delete_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket-id | 
 **storage_account_id** | **int**| storage-account-id | 
 **force_detach** | **bool**| force-detach | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucket**
> Bucket get_bucket(bucket_id, storage_account_id)

Get detailed stats for the bucket

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
bucket_id = 789 # int | bucket-id
storage_account_id = 789 # int | storage-account-id

try:
    # Get detailed stats for the bucket
    api_response = api_instance.get_bucket(bucket_id, storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->get_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket-id | 
 **storage_account_id** | **int**| storage-account-id | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_bucket**
> refresh_bucket(bucket_id, storage_account_id)

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
bucket_id = 789 # int | bucket-id
storage_account_id = 789 # int | storage-account-id

try:
    # Refresh statistics of a single bucket
    api_instance.refresh_bucket(bucket_id, storage_account_id)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->refresh_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket-id | 
 **storage_account_id** | **int**| storage-account-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

