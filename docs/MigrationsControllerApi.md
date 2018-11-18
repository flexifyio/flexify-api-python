# flexify_api.MigrationsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_migration**](MigrationsControllerApi.md#add_migration) | **POST** /rest/migrations | Add new migration
[**get_migration**](MigrationsControllerApi.md#get_migration) | **GET** /rest/migrations/{migration-id} | Get migration by id. Only migration owner or administrator have access to the migration
[**get_migrations**](MigrationsControllerApi.md#get_migrations) | **GET** /rest/migrations | Get all migrations for logged in user in pagged mode
[**hide_migration**](MigrationsControllerApi.md#hide_migration) | **POST** /rest/migrations/{migration-id}/hide | Hide migration from UI
[**stop_migration**](MigrationsControllerApi.md#stop_migration) | **POST** /rest/migrations/{migration-id}/stop | Stop (cancel) the migration


# **add_migration**
> IdResponse add_migration(migration_request)

Add new migration

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
api_instance = flexify_api.MigrationsControllerApi(flexify_api.ApiClient(configuration))
migration_request = flexify_api.AddMigrationRequest() # AddMigrationRequest | migrationRequest

try:
    # Add new migration
    api_response = api_instance.add_migration(migration_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->add_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_request** | [**AddMigrationRequest**](AddMigrationRequest.md)| migrationRequest | 

### Return type

[**IdResponse**](IdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration**
> Migration get_migration(migration_id)

Get migration by id. Only migration owner or administrator have access to the migration

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
api_instance = flexify_api.MigrationsControllerApi(flexify_api.ApiClient(configuration))
migration_id = 789 # int | migration-id

try:
    # Get migration by id. Only migration owner or administrator have access to the migration
    api_response = api_instance.get_migration(migration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->get_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| migration-id | 

### Return type

[**Migration**](Migration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migrations**
> PageMigration get_migrations(page, size, include_hidden=include_hidden, sort=sort, sort_direction=sort_direction, spring_page_request_offset=spring_page_request_offset, spring_page_request_page_number=spring_page_request_page_number, spring_page_request_page_size=spring_page_request_page_size, spring_page_request_paged=spring_page_request_paged, spring_page_request_sort_sorted=spring_page_request_sort_sorted, spring_page_request_sort_unsorted=spring_page_request_sort_unsorted, spring_page_request_unpaged=spring_page_request_unpaged)

Get all migrations for logged in user in pagged mode

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
api_instance = flexify_api.MigrationsControllerApi(flexify_api.ApiClient(configuration))
page = 0 # int | Page number
size = 100 # int | Page size
include_hidden = true # bool | Include hidden migrations to response (optional) (default to true)
sort = ['sort_example'] # list[str] | Attributes to sort (optional)
sort_direction = '\"ASC\"' # str | Sort Direction (optional)
spring_page_request_offset = 789 # int |  (optional)
spring_page_request_page_number = 56 # int |  (optional)
spring_page_request_page_size = 56 # int |  (optional)
spring_page_request_paged = true # bool |  (optional)
spring_page_request_sort_sorted = true # bool |  (optional)
spring_page_request_sort_unsorted = true # bool |  (optional)
spring_page_request_unpaged = true # bool |  (optional)

try:
    # Get all migrations for logged in user in pagged mode
    api_response = api_instance.get_migrations(page, size, include_hidden=include_hidden, sort=sort, sort_direction=sort_direction, spring_page_request_offset=spring_page_request_offset, spring_page_request_page_number=spring_page_request_page_number, spring_page_request_page_size=spring_page_request_page_size, spring_page_request_paged=spring_page_request_paged, spring_page_request_sort_sorted=spring_page_request_sort_sorted, spring_page_request_sort_unsorted=spring_page_request_sort_unsorted, spring_page_request_unpaged=spring_page_request_unpaged)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->get_migrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 
 **size** | **int**| Page size | 
 **include_hidden** | **bool**| Include hidden migrations to response | [optional] [default to true]
 **sort** | [**list[str]**](str.md)| Attributes to sort | [optional] 
 **sort_direction** | **str**| Sort Direction | [optional] 
 **spring_page_request_offset** | **int**|  | [optional] 
 **spring_page_request_page_number** | **int**|  | [optional] 
 **spring_page_request_page_size** | **int**|  | [optional] 
 **spring_page_request_paged** | **bool**|  | [optional] 
 **spring_page_request_sort_sorted** | **bool**|  | [optional] 
 **spring_page_request_sort_unsorted** | **bool**|  | [optional] 
 **spring_page_request_unpaged** | **bool**|  | [optional] 

### Return type

[**PageMigration**](PageMigration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_migration**
> Migration hide_migration(migration_id)

Hide migration from UI

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
api_instance = flexify_api.MigrationsControllerApi(flexify_api.ApiClient(configuration))
migration_id = 789 # int | migration-id

try:
    # Hide migration from UI
    api_response = api_instance.hide_migration(migration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->hide_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| migration-id | 

### Return type

[**Migration**](Migration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_migration**
> Migration stop_migration(migration_id)

Stop (cancel) the migration

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
api_instance = flexify_api.MigrationsControllerApi(flexify_api.ApiClient(configuration))
migration_id = 789 # int | migration-id

try:
    # Stop (cancel) the migration
    api_response = api_instance.stop_migration(migration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->stop_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| migration-id | 

### Return type

[**Migration**](Migration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

