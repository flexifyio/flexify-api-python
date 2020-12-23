# flexify_api.OAuthControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_info**](OAuthControllerApi.md#get_app_info) | **GET** /backend/rest/oauth/app-info | getAppInfo


# **get_app_info**
> AuthAppInfo get_app_info(provider_id)

getAppInfo

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
api_instance = flexify_api.OAuthControllerApi(flexify_api.ApiClient(configuration))
provider_id = 789 # int | provider-id

try:
    # getAppInfo
    api_response = api_instance.get_app_info(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthControllerApi->get_app_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| provider-id | 

### Return type

[**AuthAppInfo**](AuthAppInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

