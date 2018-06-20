# swagger_client.UserControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](UserControllerApi.md#get_current_user) | **GET** /rest/user/current | Get details information for logged in user
[**request_reset_password**](UserControllerApi.md#request_reset_password) | **POST** /rest/user/request-reset-password | requestResetPassword


# **get_current_user**
> User get_current_user(silence=silence)

Get details information for logged in user

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
api_instance = swagger_client.UserControllerApi(swagger_client.ApiClient(configuration))
silence = false # bool | Return 204 No Content or 401 Unauthorized in case of username not found (optional) (default to false)

try:
    # Get details information for logged in user
    api_response = api_instance.get_current_user(silence=silence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **silence** | **bool**| Return 204 No Content or 401 Unauthorized in case of username not found | [optional] [default to false]

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_reset_password**
> request_reset_password(reqeust)

requestResetPassword

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
api_instance = swagger_client.UserControllerApi(swagger_client.ApiClient(configuration))
reqeust = swagger_client.RequestResetPasswordReqeust() # RequestResetPasswordReqeust | reqeust

try:
    # requestResetPassword
    api_instance.request_reset_password(reqeust)
except ApiException as e:
    print("Exception when calling UserControllerApi->request_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reqeust** | [**RequestResetPasswordReqeust**](RequestResetPasswordReqeust.md)| reqeust | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

