# flexify_api.MigrationsControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_migration**](MigrationsControllerApi.md#add_migration) | **POST** /backend/rest/migrations | Add new migration
[**get_migration**](MigrationsControllerApi.md#get_migration) | **GET** /backend/rest/migrations/{migration-id} | Get migration by id. Only migration owner or administrator have access to the migration
[**get_migrations**](MigrationsControllerApi.md#get_migrations) | **GET** /backend/rest/migrations | Get all migrations for logged in user in paged mode
[**hide_all_migrations**](MigrationsControllerApi.md#hide_all_migrations) | **POST** /backend/rest/migrations/actions/hide-all | Mark all unfinished migrations as hidden UI
[**hide_migration**](MigrationsControllerApi.md#hide_migration) | **POST** /backend/rest/migrations/{migration-id}/actions/hide | Mark migration as hidden
[**restart_slot**](MigrationsControllerApi.md#restart_slot) | **POST** /backend/rest/migrations/{migration-id}/mappings/{mapping-id}/slots/{slot}/actions/restart | Mark migration as hidden
[**stop_migration**](MigrationsControllerApi.md#stop_migration) | **POST** /backend/rest/migrations/{migration-id}/actions/stop | Stop (cancel) the migration


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
> PageMigration get_migrations(offset, page, include_hidden=include_hidden, paged=paged, page_number=page_number, page_size=page_size, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_direction=sort_direction)

Get all migrations for logged in user in paged mode

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
offset = 0 # int | Position of the first migration in the list (or null to start from the beginning)
page = 0 # int | [Deprecated] Page number
include_hidden = true # bool | Include hidden migrations to response (optional) (default to true)
paged = true # bool |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
size = 100 # int | Max number of entries to return (AKA page size), null means no paging (optional)
sort_sorted = true # bool |  (optional)
sort_unsorted = true # bool |  (optional)
sort_direction = 'ASC' # str | Sort Direction (optional)

try:
    # Get all migrations for logged in user in paged mode
    api_response = api_instance.get_migrations(offset, page, include_hidden=include_hidden, paged=paged, page_number=page_number, page_size=page_size, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->get_migrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Position of the first migration in the list (or null to start from the beginning) | 
 **page** | **int**| [Deprecated] Page number | 
 **include_hidden** | **bool**| Include hidden migrations to response | [optional] [default to true]
 **paged** | **bool**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **size** | **int**| Max number of entries to return (AKA page size), null means no paging | [optional] 
 **sort_sorted** | **bool**|  | [optional] 
 **sort_unsorted** | **bool**|  | [optional] 
 **sort_direction** | **str**| Sort Direction | [optional] 

### Return type

[**PageMigration**](PageMigration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_all_migrations**
> hide_all_migrations()

Mark all unfinished migrations as hidden UI

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

try:
    # Mark all unfinished migrations as hidden UI
    api_instance.hide_all_migrations()
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->hide_all_migrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_migration**
> hide_migration(migration_id)

Mark migration as hidden

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
    # Mark migration as hidden
    api_instance.hide_migration(migration_id)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->hide_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| migration-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_slot**
> restart_slot(mapping_id, migration_id, slot)

Mark migration as hidden

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
mapping_id = 789 # int | mapping-id
migration_id = 789 # int | migration-id
slot = 56 # int | slot

try:
    # Mark migration as hidden
    api_instance.restart_slot(mapping_id, migration_id, slot)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->restart_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mapping-id | 
 **migration_id** | **int**| migration-id | 
 **slot** | **int**| slot | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_migration**
> stop_migration(migration_id)

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
    api_instance.stop_migration(migration_id)
except ApiException as e:
    print("Exception when calling MigrationsControllerApi->stop_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| migration-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

