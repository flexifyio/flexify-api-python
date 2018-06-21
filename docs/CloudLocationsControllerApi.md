# flexify_api.CloudLocationsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_locations_for_current_user**](CloudLocationsControllerApi.md#get_available_locations_for_current_user) | **GET** /rest/cloud-locations | getAvailableLocationsForCurrentUser


# **get_available_locations_for_current_user**
> list[CloudLocation] get_available_locations_for_current_user()

getAvailableLocationsForCurrentUser

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
api_instance = flexify_api.CloudLocationsControllerApi(flexify_api.ApiClient(configuration))

try:
    # getAvailableLocationsForCurrentUser
    api_response = api_instance.get_available_locations_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudLocationsControllerApi->get_available_locations_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CloudLocation]**](CloudLocation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

