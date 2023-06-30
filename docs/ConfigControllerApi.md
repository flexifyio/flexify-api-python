# flexify_api.ConfigControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](ConfigControllerApi.md#get_config) | **GET** /backend/rest/auth/config | Get public Management Server config
[**get_config1**](ConfigControllerApi.md#get_config1) | **GET** /backend/rest/config | Get public Management Server config


# **get_config**
> PublicManagementServerConfiguration get_config()

Get public Management Server config

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
api_instance = flexify_api.ConfigControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get public Management Server config
    api_response = api_instance.get_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigControllerApi->get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicManagementServerConfiguration**](PublicManagementServerConfiguration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config1**
> PublicManagementServerConfiguration get_config1()

Get public Management Server config

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
api_instance = flexify_api.ConfigControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get public Management Server config
    api_response = api_instance.get_config1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigControllerApi->get_config1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicManagementServerConfiguration**](PublicManagementServerConfiguration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

