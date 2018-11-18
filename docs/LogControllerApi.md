# flexify_api.LogControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_for_current_user**](LogControllerApi.md#get_log_for_current_user) | **GET** /rest/log | getLogForCurrentUser


# **get_log_for_current_user**
> PageLogEntry get_log_for_current_user(page, size, endpoint_id=endpoint_id, migration_id=migration_id, sort=sort, sort_direction=sort_direction, spring_page_request_offset=spring_page_request_offset, spring_page_request_page_number=spring_page_request_page_number, spring_page_request_page_size=spring_page_request_page_size, spring_page_request_paged=spring_page_request_paged, spring_page_request_sort_sorted=spring_page_request_sort_sorted, spring_page_request_sort_unsorted=spring_page_request_sort_unsorted, spring_page_request_unpaged=spring_page_request_unpaged, storage_id=storage_id)

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
page = 0 # int | Page number
size = 100 # int | Page size
endpoint_id = 789 # int | endpoint-id (optional)
migration_id = 789 # int | migration-id (optional)
sort = ['sort_example'] # list[str] | Attributes to sort (optional)
sort_direction = '\"ASC\"' # str | Sort Direction (optional)
spring_page_request_offset = 789 # int |  (optional)
spring_page_request_page_number = 56 # int |  (optional)
spring_page_request_page_size = 56 # int |  (optional)
spring_page_request_paged = true # bool |  (optional)
spring_page_request_sort_sorted = true # bool |  (optional)
spring_page_request_sort_unsorted = true # bool |  (optional)
spring_page_request_unpaged = true # bool |  (optional)
storage_id = 789 # int | storage-id (optional)

try:
    # getLogForCurrentUser
    api_response = api_instance.get_log_for_current_user(page, size, endpoint_id=endpoint_id, migration_id=migration_id, sort=sort, sort_direction=sort_direction, spring_page_request_offset=spring_page_request_offset, spring_page_request_page_number=spring_page_request_page_number, spring_page_request_page_size=spring_page_request_page_size, spring_page_request_paged=spring_page_request_paged, spring_page_request_sort_sorted=spring_page_request_sort_sorted, spring_page_request_sort_unsorted=spring_page_request_sort_unsorted, spring_page_request_unpaged=spring_page_request_unpaged, storage_id=storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogControllerApi->get_log_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 
 **size** | **int**| Page size | 
 **endpoint_id** | **int**| endpoint-id | [optional] 
 **migration_id** | **int**| migration-id | [optional] 
 **sort** | [**list[str]**](str.md)| Attributes to sort | [optional] 
 **sort_direction** | **str**| Sort Direction | [optional] 
 **spring_page_request_offset** | **int**|  | [optional] 
 **spring_page_request_page_number** | **int**|  | [optional] 
 **spring_page_request_page_size** | **int**|  | [optional] 
 **spring_page_request_paged** | **bool**|  | [optional] 
 **spring_page_request_sort_sorted** | **bool**|  | [optional] 
 **spring_page_request_sort_unsorted** | **bool**|  | [optional] 
 **spring_page_request_unpaged** | **bool**|  | [optional] 
 **storage_id** | **int**| storage-id | [optional] 

### Return type

[**PageLogEntry**](PageLogEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

