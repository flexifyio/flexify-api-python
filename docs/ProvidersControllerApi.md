# flexify_api.ProvidersControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_providers**](ProvidersControllerApi.md#get_providers) | **GET** /backend/rest/providers | Get all storage providers


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
api_instance = flexify_api.ProvidersControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get all storage providers
    api_response = api_instance.get_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersControllerApi->get_providers: %s\n" % e)
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

