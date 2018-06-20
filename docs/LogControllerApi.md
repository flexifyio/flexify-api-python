# swagger_client.LogControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_for_current_user**](LogControllerApi.md#get_log_for_current_user) | **GET** /rest/log | getLogForCurrentUser


# **get_log_for_current_user**
> list[LogEntry] get_log_for_current_user(storage_id=storage_id, migration_id=migration_id, endpoint_id=endpoint_id)

getLogForCurrentUser

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogControllerApi(swagger_client.ApiClient(configuration))
storage_id = 789 # int | storage-id (optional)
migration_id = 789 # int | migration-id (optional)
endpoint_id = 789 # int | endpoint-id (optional)

try:
    # getLogForCurrentUser
    api_response = api_instance.get_log_for_current_user(storage_id=storage_id, migration_id=migration_id, endpoint_id=endpoint_id)
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

### Return type

[**list[LogEntry]**](LogEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

