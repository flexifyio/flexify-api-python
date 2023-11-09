# flexify_api.AuthSsoControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](AuthSsoControllerApi.md#get_config) | **GET** /backend/rest/auth/sso/config | getConfig
[**get_device_code**](AuthSsoControllerApi.md#get_device_code) | **GET** /backend/rest/auth/sso/device-code | getDeviceCode
[**get_token_by_device_code**](AuthSsoControllerApi.md#get_token_by_device_code) | **POST** /backend/rest/auth/sso/token-by-device-code | getTokenByDeviceCode
[**refresh_token_for_device_code_flow**](AuthSsoControllerApi.md#refresh_token_for_device_code_flow) | **POST** /backend/rest/auth/sso/token-refresh | refreshTokenForDeviceCodeFlow


# **get_config**
> MicrosoftOAuthConfig get_config(oauth_provider_id)

getConfig

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
api_instance = flexify_api.AuthSsoControllerApi(flexify_api.ApiClient(configuration))
oauth_provider_id = 'oauth_provider_id_example' # str | oauth-provider-id

try:
    # getConfig
    api_response = api_instance.get_config(oauth_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSsoControllerApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_provider_id** | **str**| oauth-provider-id | 

### Return type

[**MicrosoftOAuthConfig**](MicrosoftOAuthConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_code**
> OAuth2DeviceCodeResponse get_device_code(oauth_provider_id)

getDeviceCode

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
api_instance = flexify_api.AuthSsoControllerApi(flexify_api.ApiClient(configuration))
oauth_provider_id = 'oauth_provider_id_example' # str | oauth-provider-id

try:
    # getDeviceCode
    api_response = api_instance.get_device_code(oauth_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSsoControllerApi->get_device_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_provider_id** | **str**| oauth-provider-id | 

### Return type

[**OAuth2DeviceCodeResponse**](OAuth2DeviceCodeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_by_device_code**
> OAuthToken get_token_by_device_code(request)

getTokenByDeviceCode

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
api_instance = flexify_api.AuthSsoControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.TokenByDeviceCodeRequest() # TokenByDeviceCodeRequest | request

try:
    # getTokenByDeviceCode
    api_response = api_instance.get_token_by_device_code(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSsoControllerApi->get_token_by_device_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TokenByDeviceCodeRequest**](TokenByDeviceCodeRequest.md)| request | 

### Return type

[**OAuthToken**](OAuthToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token_for_device_code_flow**
> OAuthToken refresh_token_for_device_code_flow(request)

refreshTokenForDeviceCodeFlow

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
api_instance = flexify_api.AuthSsoControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.RefreshTokenRequest() # RefreshTokenRequest | request

try:
    # refreshTokenForDeviceCodeFlow
    api_response = api_instance.refresh_token_for_device_code_flow(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthSsoControllerApi->refresh_token_for_device_code_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)| request | 

### Return type

[**OAuthToken**](OAuthToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

