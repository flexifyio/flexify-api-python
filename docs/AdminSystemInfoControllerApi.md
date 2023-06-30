# flexify_api.AdminSystemInfoControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_info**](AdminSystemInfoControllerApi.md#system_info) | **GET** /backend/rest/admin/system-info | Request General System Information


# **system_info**
> ManagementServerDetailedVersionInfo system_info()

Request General System Information

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
api_instance = flexify_api.AdminSystemInfoControllerApi(flexify_api.ApiClient(configuration))

try:
    # Request General System Information
    api_response = api_instance.system_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminSystemInfoControllerApi->system_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManagementServerDetailedVersionInfo**](ManagementServerDetailedVersionInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

