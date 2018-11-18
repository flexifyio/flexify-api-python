# flexify_api.StorageAccountsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_storage_account**](StorageAccountsControllerApi.md#add_storage_account) | **POST** /rest/storage-accounts | Add Storage Account with an optional list of buckets
[**delete_storage_account**](StorageAccountsControllerApi.md#delete_storage_account) | **DELETE** /rest/storage-accounts/{storage-account-id} | Deletes (hides) a bucket/container
[**get_storage_account**](StorageAccountsControllerApi.md#get_storage_account) | **GET** /rest/storage-accounts/storage-accounts/{storage-account-id} | Get storage account by id
[**get_storage_accounts**](StorageAccountsControllerApi.md#get_storage_accounts) | **GET** /rest/storage-accounts | Get all storage accounts for current user
[**refresh_storage_account**](StorageAccountsControllerApi.md#refresh_storage_account) | **POST** /rest/storage-accounts/{storage-account-id}/actions/refresh | Requests and updates list of buckets/containers for the storage account


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
api_instance = flexify_api.StorageAccountsControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.AddStorageAccountRequest() # AddStorageAccountRequest | request

try:
    # Add Storage Account with an optional list of buckets
    api_response = api_instance.add_storage_account(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAccountsControllerApi->add_storage_account: %s\n" % e)
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

# **delete_storage_account**
> delete_storage_account(storage_account_id, force_detach=force_detach)

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
api_instance = flexify_api.StorageAccountsControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
force_detach = false # bool | force-detach (optional) (default to false)

try:
    # Deletes (hides) a bucket/container
    api_instance.delete_storage_account(storage_account_id, force_detach=force_detach)
except ApiException as e:
    print("Exception when calling StorageAccountsControllerApi->delete_storage_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_storage_account**
> list[Bucket] get_storage_account(storage_account_id)

Get storage account by id

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
api_instance = flexify_api.StorageAccountsControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id

try:
    # Get storage account by id
    api_response = api_instance.get_storage_account(storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAccountsControllerApi->get_storage_account: %s\n" % e)
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
api_instance = flexify_api.StorageAccountsControllerApi(flexify_api.ApiClient(configuration))
include_storages = true # bool | Include storages of given storage account to the response (optional) (default to true)

try:
    # Get all storage accounts for current user
    api_response = api_instance.get_storage_accounts(include_storages=include_storages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAccountsControllerApi->get_storage_accounts: %s\n" % e)
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

# **refresh_storage_account**
> refresh_storage_account(storage_account_id)

Requests and updates list of buckets/containers for the storage account

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
api_instance = flexify_api.StorageAccountsControllerApi(flexify_api.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id

try:
    # Requests and updates list of buckets/containers for the storage account
    api_instance.refresh_storage_account(storage_account_id)
except ApiException as e:
    print("Exception when calling StorageAccountsControllerApi->refresh_storage_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

