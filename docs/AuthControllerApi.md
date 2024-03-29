# flexify_api.AuthControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthControllerApi.md#authenticate) | **POST** /backend/rest/auth | Generate new access token for the user
[**check_token_and_get_user**](AuthControllerApi.md#check_token_and_get_user) | **GET** /backend/rest/auth/user | Check of given token
[**logout**](AuthControllerApi.md#logout) | **POST** /backend/rest/auth/logout | Logout


# **authenticate**
> AuthenticationResponse authenticate(authentication_request)

Generate new access token for the user

### Example
```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flexify_api.AuthControllerApi()
authentication_request = flexify_api.AuthenticationRequest() # AuthenticationRequest | authenticationRequest

try:
    # Generate new access token for the user
    api_response = api_instance.authenticate(authentication_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**AuthenticationRequest**](AuthenticationRequest.md)| authenticationRequest | 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_token_and_get_user**
> AuthCheckTokenAndGetUserResponse check_token_and_get_user()

Check of given token

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
api_instance = flexify_api.AuthControllerApi(flexify_api.ApiClient(configuration))

try:
    # Check of given token
    api_response = api_instance.check_token_and_get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->check_token_and_get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthCheckTokenAndGetUserResponse**](AuthCheckTokenAndGetUserResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(request)

Logout

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
api_instance = flexify_api.AuthControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.LogoutRequest() # LogoutRequest | request

try:
    # Logout
    api_instance.logout(request)
except ApiException as e:
    print("Exception when calling AuthControllerApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LogoutRequest**](LogoutRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

