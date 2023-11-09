# flexify_api.StorageAccountsOAuthControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config2**](StorageAccountsOAuthControllerApi.md#get_config2) | **GET** /backend/rest/storage-accounts/oauth/config | getConfig
[**get_device_code1**](StorageAccountsOAuthControllerApi.md#get_device_code1) | **GET** /backend/rest/storage-accounts/oauth/device-code | getDeviceCode


# **get_config2**
> object get_config2(oauth_provider_id)

getConfig

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
api_instance = flexify_api.StorageAccountsOAuthControllerApi(flexify_api.ApiClient(configuration))
oauth_provider_id = 'oauth_provider_id_example' # str | oauth-provider-id

try:
    # getConfig
    api_response = api_instance.get_config2(oauth_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAccountsOAuthControllerApi->get_config2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_provider_id** | **str**| oauth-provider-id | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_code1**
> OAuth2DeviceCodeResponse get_device_code1(oauth_provider_id, storage_account_name, storage_provider_id, use_ssl, custom_endpoint=custom_endpoint)

getDeviceCode

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
api_instance = flexify_api.StorageAccountsOAuthControllerApi(flexify_api.ApiClient(configuration))
oauth_provider_id = 'oauth_provider_id_example' # str | oauth-provider-id
storage_account_name = 'storage_account_name_example' # str | storage-account-name
storage_provider_id = 789 # int | storage-provider-id
use_ssl = true # bool | use-ssl
custom_endpoint = 'custom_endpoint_example' # str | custom-endpoint (optional)

try:
    # getDeviceCode
    api_response = api_instance.get_device_code1(oauth_provider_id, storage_account_name, storage_provider_id, use_ssl, custom_endpoint=custom_endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageAccountsOAuthControllerApi->get_device_code1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_provider_id** | **str**| oauth-provider-id | 
 **storage_account_name** | **str**| storage-account-name | 
 **storage_provider_id** | **int**| storage-provider-id | 
 **use_ssl** | **bool**| use-ssl | 
 **custom_endpoint** | **str**| custom-endpoint | [optional] 

### Return type

[**OAuth2DeviceCodeResponse**](OAuth2DeviceCodeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

