# flexify_api.ImpersonationControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_impersonate_from_user**](ImpersonationControllerApi.md#add_impersonate_from_user) | **POST** /backend/rest/impersonate/from | addImpersonateFromUser
[**get_impersonate_from_list**](ImpersonationControllerApi.md#get_impersonate_from_list) | **GET** /backend/rest/impersonate/from | getImpersonateFromList
[**get_impersonate_to_list**](ImpersonationControllerApi.md#get_impersonate_to_list) | **GET** /backend/rest/impersonate/to | getImpersonateToList
[**impersonate**](ImpersonationControllerApi.md#impersonate) | **POST** /backend/rest/impersonate/as/{userId} | impersonate
[**remove_impersonate_from_user**](ImpersonationControllerApi.md#remove_impersonate_from_user) | **DELETE** /backend/rest/impersonate/from/{user-id} | removeImpersonateFromUser


# **add_impersonate_from_user**
> add_impersonate_from_user(request)

addImpersonateFromUser

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
api_instance = flexify_api.ImpersonationControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.AddImpersonateFromUserRequest() # AddImpersonateFromUserRequest | request

try:
    # addImpersonateFromUser
    api_instance.add_impersonate_from_user(request)
except ApiException as e:
    print("Exception when calling ImpersonationControllerApi->add_impersonate_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AddImpersonateFromUserRequest**](AddImpersonateFromUserRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_impersonate_from_list**
> list[ImpersonateUser] get_impersonate_from_list()

getImpersonateFromList

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
api_instance = flexify_api.ImpersonationControllerApi(flexify_api.ApiClient(configuration))

try:
    # getImpersonateFromList
    api_response = api_instance.get_impersonate_from_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpersonationControllerApi->get_impersonate_from_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImpersonateUser]**](ImpersonateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_impersonate_to_list**
> list[ImpersonateUser] get_impersonate_to_list()

getImpersonateToList

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
api_instance = flexify_api.ImpersonationControllerApi(flexify_api.ApiClient(configuration))

try:
    # getImpersonateToList
    api_response = api_instance.get_impersonate_to_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpersonationControllerApi->get_impersonate_to_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImpersonateUser]**](ImpersonateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonate**
> InformationAboutAuthenticationToken impersonate(user_id)

impersonate

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
api_instance = flexify_api.ImpersonationControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # impersonate
    api_response = api_instance.impersonate(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImpersonationControllerApi->impersonate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_impersonate_from_user**
> remove_impersonate_from_user(user_id)

removeImpersonateFromUser

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
api_instance = flexify_api.ImpersonationControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | user-id

try:
    # removeImpersonateFromUser
    api_instance.remove_impersonate_from_user(user_id)
except ApiException as e:
    print("Exception when calling ImpersonationControllerApi->remove_impersonate_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

