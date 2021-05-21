# flexify_api.PartnerSignUpCodesControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code**](PartnerSignUpCodesControllerApi.md#create_code) | **POST** /backend/rest/distributor/codes | createCode
[**create_code1**](PartnerSignUpCodesControllerApi.md#create_code1) | **POST** /backend/rest/partner/codes | createCode
[**delete_code**](PartnerSignUpCodesControllerApi.md#delete_code) | **DELETE** /backend/rest/distributor/codes/{code} | deleteCode
[**delete_code1**](PartnerSignUpCodesControllerApi.md#delete_code1) | **DELETE** /backend/rest/partner/codes/{code} | deleteCode
[**get_all1**](PartnerSignUpCodesControllerApi.md#get_all1) | **GET** /backend/rest/distributor/codes | getAll
[**get_all2**](PartnerSignUpCodesControllerApi.md#get_all2) | **GET** /backend/rest/partner/codes | getAll


# **create_code**
> create_code(request)

createCode

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
api_instance = flexify_api.PartnerSignUpCodesControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SignupCodeReq() # SignupCodeReq | request

try:
    # createCode
    api_instance.create_code(request)
except ApiException as e:
    print("Exception when calling PartnerSignUpCodesControllerApi->create_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SignupCodeReq**](SignupCodeReq.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_code1**
> create_code1(request)

createCode

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
api_instance = flexify_api.PartnerSignUpCodesControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SignupCodeReq() # SignupCodeReq | request

try:
    # createCode
    api_instance.create_code1(request)
except ApiException as e:
    print("Exception when calling PartnerSignUpCodesControllerApi->create_code1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SignupCodeReq**](SignupCodeReq.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_code**
> delete_code(code)

deleteCode

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
api_instance = flexify_api.PartnerSignUpCodesControllerApi(flexify_api.ApiClient(configuration))
code = 'code_example' # str | code

try:
    # deleteCode
    api_instance.delete_code(code)
except ApiException as e:
    print("Exception when calling PartnerSignUpCodesControllerApi->delete_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_code1**
> delete_code1(code)

deleteCode

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
api_instance = flexify_api.PartnerSignUpCodesControllerApi(flexify_api.ApiClient(configuration))
code = 'code_example' # str | code

try:
    # deleteCode
    api_instance.delete_code1(code)
except ApiException as e:
    print("Exception when calling PartnerSignUpCodesControllerApi->delete_code1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all1**
> list[SignupCodeRes] get_all1()

getAll

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
api_instance = flexify_api.PartnerSignUpCodesControllerApi(flexify_api.ApiClient(configuration))

try:
    # getAll
    api_response = api_instance.get_all1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerSignUpCodesControllerApi->get_all1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SignupCodeRes]**](SignupCodeRes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all2**
> list[SignupCodeRes] get_all2()

getAll

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
api_instance = flexify_api.PartnerSignUpCodesControllerApi(flexify_api.ApiClient(configuration))

try:
    # getAll
    api_response = api_instance.get_all2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerSignUpCodesControllerApi->get_all2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SignupCodeRes]**](SignupCodeRes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

