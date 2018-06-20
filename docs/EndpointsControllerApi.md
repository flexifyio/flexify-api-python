# swagger_client.EndpointsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_storage_to_endpoint**](EndpointsControllerApi.md#attach_storage_to_endpoint) | **POST** /rest/endpoints/{endpoint-id}/storages | Attach the storage to the endpoint
[**detach_storage_from_endpoint**](EndpointsControllerApi.md#detach_storage_from_endpoint) | **DELETE** /rest/endpoints/{endpoint-id}/storages/{storage-id} | Detach the storage from the endpoint
[**disable**](EndpointsControllerApi.md#disable) | **PUT** /rest/endpoints/{endpoint-id}/actions/disable | Disable the endpoint
[**enable**](EndpointsControllerApi.md#enable) | **PUT** /rest/endpoints/{endpoint-id}/actions/enable | Enable the endpoint
[**get_endpoint_details**](EndpointsControllerApi.md#get_endpoint_details) | **GET** /rest/endpoints/{endpoint-id} | Get endpoint details
[**get_endpoints_for_current_user**](EndpointsControllerApi.md#get_endpoints_for_current_user) | **GET** /rest/endpoints | Get endpoint for current user. This method will create new endpoint if no endpoints exist for user
[**set_default_storage**](EndpointsControllerApi.md#set_default_storage) | **PUT** /rest/endpoints/{endpoint-id}/storages/{storage-id}/actions/set-as-default | Set given storage as default for the endpoint
[**update_endpoint**](EndpointsControllerApi.md#update_endpoint) | **PUT** /rest/endpoints/{endpoint-id} | Update attributes of the endpoint


# **attach_storage_to_endpoint**
> attach_storage_to_endpoint(endpoint_id, endpoint_storage)

Attach the storage to the endpoint

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
endpoint_storage = swagger_client.EndpointStorage() # EndpointStorage | endpointStorage

try:
    # Attach the storage to the endpoint
    api_instance.attach_storage_to_endpoint(endpoint_id, endpoint_storage)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->attach_storage_to_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **endpoint_storage** | [**EndpointStorage**](EndpointStorage.md)| endpointStorage | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_storage_from_endpoint**
> detach_storage_from_endpoint(endpoint_id, storage_id)

Detach the storage from the endpoint

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
storage_id = 789 # int | storage-id

try:
    # Detach the storage from the endpoint
    api_instance.detach_storage_from_endpoint(endpoint_id, storage_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->detach_storage_from_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **storage_id** | **int**| storage-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable**
> disable(endpoint_id)

Disable the endpoint

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Disable the endpoint
    api_instance.disable(endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable**
> enable(endpoint_id)

Enable the endpoint

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Enable the endpoint
    api_instance.enable(endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_details**
> EndpointDetails get_endpoint_details(endpoint_id)

Get endpoint details

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id

try:
    # Get endpoint details
    api_response = api_instance.get_endpoint_details(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->get_endpoint_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 

### Return type

[**EndpointDetails**](EndpointDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_for_current_user**
> list[EndpointDetails] get_endpoints_for_current_user()

Get endpoint for current user. This method will create new endpoint if no endpoints exist for user

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get endpoint for current user. This method will create new endpoint if no endpoints exist for user
    api_response = api_instance.get_endpoints_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->get_endpoints_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EndpointDetails]**](EndpointDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_storage**
> set_default_storage(endpoint_id, storage_id)

Set given storage as default for the endpoint

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
storage_id = 789 # int | storage-id

try:
    # Set given storage as default for the endpoint
    api_instance.set_default_storage(endpoint_id, storage_id)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->set_default_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **storage_id** | **int**| storage-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint**
> update_endpoint(endpoint_id, endpoint)

Update attributes of the endpoint

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
api_instance = swagger_client.EndpointsControllerApi(swagger_client.ApiClient(configuration))
endpoint_id = 789 # int | endpoint-id
endpoint = swagger_client.Endpoint() # Endpoint | endpoint

try:
    # Update attributes of the endpoint
    api_instance.update_endpoint(endpoint_id, endpoint)
except ApiException as e:
    print("Exception when calling EndpointsControllerApi->update_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| endpoint-id | 
 **endpoint** | [**Endpoint**](Endpoint.md)| endpoint | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

