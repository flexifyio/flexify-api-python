# flexify_api_client.StoragesControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_storage_account**](StoragesControllerApi.md#add_storage_account) | **POST** /rest/storage-accounts | Add Storage Account with an optional list of buckets
[**add_storages**](StoragesControllerApi.md#add_storages) | **POST** /rest/storage-accounts/{storage-account-id}/storages | Add buckets to the storage account and optionally attach them to endpoint
[**delete_storage**](StoragesControllerApi.md#delete_storage) | **DELETE** /rest/storage-accounts/{storage-account-id}/storages/{storage-id} | Delete Storage
[**delete_storages**](StoragesControllerApi.md#delete_storages) | **POST** /rest/storage-accounts/actions/delete-storages | Deletes storages
[**generate_access_keys**](StoragesControllerApi.md#generate_access_keys) | **GET** /rest/generate-access-keys | Generate new access keys pair
[**get_providers**](StoragesControllerApi.md#get_providers) | **GET** /rest/providers | Get all storage providers
[**get_storage_accounts**](StoragesControllerApi.md#get_storage_accounts) | **GET** /rest/storage-accounts | Get all storage accounts for current user
[**get_storages**](StoragesControllerApi.md#get_storages) | **GET** /rest/storage-accounts/{storage-account-id}/storages | Get storages of the storage account
[**refresh_storage**](StoragesControllerApi.md#refresh_storage) | **POST** /rest/storage-accounts/{storage-account-id}/storages/{storage-id}/actions/refresh | Refresh storage
[**refresh_storages**](StoragesControllerApi.md#refresh_storages) | **POST** /rest/storage-accounts/actions/refresh-storages | Refresh storages
[**request_buckets**](StoragesControllerApi.md#request_buckets) | **GET** /rest/buckets | Lists buckets of the external storage account
[**request_buckets_for_storage_account**](StoragesControllerApi.md#request_buckets_for_storage_account) | **GET** /rest/storage-accounts/{storage-account-id}/buckets | Retrieve buckets from external cloud storage account


# **add_storage_account**
> IdResponse add_storage_account(request)

Add Storage Account with an optional list of buckets

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
request = flexify_api_client.AddStorageAccountRequest() # AddStorageAccountRequest | request

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

# **add_storages**
> AddStoragesResponse add_storages(storage_account_id, request)

Add buckets to the storage account and optionally attach them to endpoint

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
request = flexify_api_client.AddStoragesRequest() # AddStoragesRequest | request

try:
    # Add buckets to the storage account and optionally attach them to endpoint
    api_response = api_instance.add_storages(storage_account_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->add_storages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **request** | [**AddStoragesRequest**](AddStoragesRequest.md)| request | 

### Return type

[**AddStoragesResponse**](AddStoragesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage**
> delete_storage(storage_account_id, storage_id)

Delete Storage

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
storage_id = 789 # int | storage-id

try:
    # Delete Storage
    api_instance.delete_storage(storage_account_id, storage_id)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->delete_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **storage_id** | **int**| storage-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storages**
> delete_storages(request)

Deletes storages

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
request = flexify_api_client.IdsList() # IdsList | request

try:
    # Deletes storages
    api_instance.delete_storages(request)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->delete_storages: %s\n" % e)
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
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))

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

# **get_providers**
> list[StorageProvider] get_providers()

Get all storage providers

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))

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
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
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

# **get_storages**
> list[Storage] get_storages(storage_account_id)

Get storages of the storage account

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id

try:
    # Get storages of the storage account
    api_response = api_instance.get_storages(storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->get_storages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 

### Return type

[**list[Storage]**](Storage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_storage**
> refresh_storage(storage_account_id, storage_id)

Refresh storage

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id
storage_id = 789 # int | storage-id

try:
    # Refresh storage
    api_instance.refresh_storage(storage_account_id, storage_id)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->refresh_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_account_id** | **int**| storage-account-id | 
 **storage_id** | **int**| storage-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_storages**
> refresh_storages(request)

Refresh storages

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
request = flexify_api_client.IdsList() # IdsList | request

try:
    # Refresh storages
    api_instance.refresh_storages(request)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->refresh_storages: %s\n" % e)
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
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
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

# **request_buckets_for_storage_account**
> list[Bucket] request_buckets_for_storage_account(storage_account_id)

Retrieve buckets from external cloud storage account

### Example
```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = flexify_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = flexify_api_client.StoragesControllerApi(flexify_api_client.ApiClient(configuration))
storage_account_id = 789 # int | storage-account-id

try:
    # Retrieve buckets from external cloud storage account
    api_response = api_instance.request_buckets_for_storage_account(storage_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragesControllerApi->request_buckets_for_storage_account: %s\n" % e)
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

