# flexify_api.LogControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_for_current_user**](LogControllerApi.md#get_log_for_current_user) | **GET** /backend/rest/log | getLogForCurrentUser


# **get_log_for_current_user**
> MarkerPageLogEntry get_log_for_current_user(endpoint_id=endpoint_id, marker=marker, migration_id=migration_id, storage_account_id=storage_account_id, storage_id=storage_id)

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
endpoint_id = 789 # int | endpoint-id (optional)
marker = 789 # int | marker (optional)
migration_id = 789 # int | migration-id (optional)
storage_account_id = 789 # int | storage-account-id (optional)
storage_id = 789 # int | storage-id (optional)

try:
    # getLogForCurrentUser
    api_response = api_instance.get_log_for_current_user(endpoint_id=endpoint_id, marker=marker, migration_id=migration_id, storage_account_id=storage_account_id, storage_id=storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogControllerApi->get_log_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | [optional] 
 **marker** | **int**| marker | [optional] 
 **migration_id** | **int**| migration-id | [optional] 
 **storage_account_id** | **int**| storage-account-id | [optional] 
 **storage_id** | **int**| storage-id | [optional] 

### Return type

[**MarkerPageLogEntry**](MarkerPageLogEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

