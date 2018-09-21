# flexify_api.LogControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_for_current_user**](LogControllerApi.md#get_log_for_current_user) | **GET** /rest/log | getLogForCurrentUser


# **get_log_for_current_user**
> PageLogEntry get_log_for_current_user(storage_id=storage_id, migration_id=migration_id, endpoint_id=endpoint_id, sort=sort, page=page, size=size, sort_direction=sort_direction)

getLogForCurrentUser

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
api_instance = flexify_api.LogControllerApi(flexify_api.ApiClient(configuration))
storage_id = 789 # int | storage-id (optional)
migration_id = 789 # int | migration-id (optional)
endpoint_id = 789 # int | endpoint-id (optional)
sort = ['sort_example'] # list[str] | Attributes to sort (optional)
page = 0 # int | Page number (optional) (default to 0)
size = 100 # int | Page size (optional) (default to 100)
sort_direction = 'ASC' # str | Sort Direction (optional) (default to ASC)

try:
    # getLogForCurrentUser
    api_response = api_instance.get_log_for_current_user(storage_id=storage_id, migration_id=migration_id, endpoint_id=endpoint_id, sort=sort, page=page, size=size, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogControllerApi->get_log_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**| storage-id | [optional] 
 **migration_id** | **int**| migration-id | [optional] 
 **endpoint_id** | **int**| endpoint-id | [optional] 
 **sort** | [**list[str]**](str.md)| Attributes to sort | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **size** | **int**| Page size | [optional] [default to 100]
 **sort_direction** | **str**| Sort Direction | [optional] [default to ASC]

### Return type

[**PageLogEntry**](PageLogEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

