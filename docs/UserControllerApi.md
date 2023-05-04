# flexify_api.UserControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_microsoft_sso**](UserControllerApi.md#change_microsoft_sso) | **POST** /backend/rest/user/current/sso-microsoft | changeMicrosoftSso
[**get_current_user**](UserControllerApi.md#get_current_user) | **GET** /backend/rest/user/current | Get details of user corresponding to provided auth token
[**request_delete**](UserControllerApi.md#request_delete) | **POST** /backend/rest/user/request-delete | requestDelete
[**request_reset_password**](UserControllerApi.md#request_reset_password) | **POST** /backend/rest/user/request-reset-password | requestResetPassword


# **change_microsoft_sso**
> change_microsoft_sso(request)

changeMicrosoftSso

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
api_instance = flexify_api.UserControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.ChangeSsoMicrosoftRequest() # ChangeSsoMicrosoftRequest | request

try:
    # changeMicrosoftSso
    api_instance.change_microsoft_sso(request)
except ApiException as e:
    print("Exception when calling UserControllerApi->change_microsoft_sso: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ChangeSsoMicrosoftRequest**](ChangeSsoMicrosoftRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user(context_path=context_path, locale_country=locale_country, locale_display_country=locale_display_country, locale_display_language=locale_display_language, locale_display_name=locale_display_name, locale_display_script=locale_display_script, locale_display_variant=locale_display_variant, locale_extension_keys=locale_extension_keys, locale_iso3_country=locale_iso3_country, locale_iso3_language=locale_iso3_language, locale_language=locale_language, locale_script=locale_script, locale_unicode_locale_attributes=locale_unicode_locale_attributes, locale_unicode_locale_keys=locale_unicode_locale_keys, locale_variant=locale_variant, remote_user=remote_user, secure=secure, user_principal_name=user_principal_name)

Get details of user corresponding to provided auth token

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
api_instance = flexify_api.UserControllerApi(flexify_api.ApiClient(configuration))
context_path = 'context_path_example' # str |  (optional)
locale_country = 'locale_country_example' # str |  (optional)
locale_display_country = 'locale_display_country_example' # str |  (optional)
locale_display_language = 'locale_display_language_example' # str |  (optional)
locale_display_name = 'locale_display_name_example' # str |  (optional)
locale_display_script = 'locale_display_script_example' # str |  (optional)
locale_display_variant = 'locale_display_variant_example' # str |  (optional)
locale_extension_keys = ['locale_extension_keys_example'] # list[str] |  (optional)
locale_iso3_country = 'locale_iso3_country_example' # str |  (optional)
locale_iso3_language = 'locale_iso3_language_example' # str |  (optional)
locale_language = 'locale_language_example' # str |  (optional)
locale_script = 'locale_script_example' # str |  (optional)
locale_unicode_locale_attributes = ['locale_unicode_locale_attributes_example'] # list[str] |  (optional)
locale_unicode_locale_keys = ['locale_unicode_locale_keys_example'] # list[str] |  (optional)
locale_variant = 'locale_variant_example' # str |  (optional)
remote_user = 'remote_user_example' # str |  (optional)
secure = true # bool |  (optional)
user_principal_name = 'user_principal_name_example' # str |  (optional)

try:
    # Get details of user corresponding to provided auth token
    api_response = api_instance.get_current_user(context_path=context_path, locale_country=locale_country, locale_display_country=locale_display_country, locale_display_language=locale_display_language, locale_display_name=locale_display_name, locale_display_script=locale_display_script, locale_display_variant=locale_display_variant, locale_extension_keys=locale_extension_keys, locale_iso3_country=locale_iso3_country, locale_iso3_language=locale_iso3_language, locale_language=locale_language, locale_script=locale_script, locale_unicode_locale_attributes=locale_unicode_locale_attributes, locale_unicode_locale_keys=locale_unicode_locale_keys, locale_variant=locale_variant, remote_user=remote_user, secure=secure, user_principal_name=user_principal_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_path** | **str**|  | [optional] 
 **locale_country** | **str**|  | [optional] 
 **locale_display_country** | **str**|  | [optional] 
 **locale_display_language** | **str**|  | [optional] 
 **locale_display_name** | **str**|  | [optional] 
 **locale_display_script** | **str**|  | [optional] 
 **locale_display_variant** | **str**|  | [optional] 
 **locale_extension_keys** | [**list[str]**](str.md)|  | [optional] 
 **locale_iso3_country** | **str**|  | [optional] 
 **locale_iso3_language** | **str**|  | [optional] 
 **locale_language** | **str**|  | [optional] 
 **locale_script** | **str**|  | [optional] 
 **locale_unicode_locale_attributes** | [**list[str]**](str.md)|  | [optional] 
 **locale_unicode_locale_keys** | [**list[str]**](str.md)|  | [optional] 
 **locale_variant** | **str**|  | [optional] 
 **remote_user** | **str**|  | [optional] 
 **secure** | **bool**|  | [optional] 
 **user_principal_name** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_delete**
> request_delete()

requestDelete

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
api_instance = flexify_api.UserControllerApi(flexify_api.ApiClient(configuration))

try:
    # requestDelete
    api_instance.request_delete()
except ApiException as e:
    print("Exception when calling UserControllerApi->request_delete: %s\n" % e)
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

# **request_reset_password**
> request_reset_password(request)

requestResetPassword

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
api_instance = flexify_api.UserControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.RequestResetPasswordRequest() # RequestResetPasswordRequest | request

try:
    # requestResetPassword
    api_instance.request_reset_password(request)
except ApiException as e:
    print("Exception when calling UserControllerApi->request_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**RequestResetPasswordRequest**](RequestResetPasswordRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

