# swagger_client.AuthenticationControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_request**](AuthenticationControllerApi.md#authentication_request) | **POST** /rest/auth | Generate access token for user
[**logout**](AuthenticationControllerApi.md#logout) | **POST** /rest/auth/logout | Logout


# **authentication_request**
> AuthenticationResponse authentication_request(authentication_request)

Generate access token for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationControllerApi()
authentication_request = swagger_client.AuthenticationRequest() # AuthenticationRequest | authenticationRequest

try:
    # Generate access token for user
    api_response = api_instance.authentication_request(authentication_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->authentication_request: %s\n" % e)
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

# **logout**
> object logout()

Logout

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
api_instance = swagger_client.AuthenticationControllerApi(swagger_client.ApiClient(configuration))

try:
    # Logout
    api_response = api_instance.logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

