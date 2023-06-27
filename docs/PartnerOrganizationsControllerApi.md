# flexify_api.PartnerOrganizationsControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all**](PartnerOrganizationsControllerApi.md#get_all) | **GET** /backend/rest/partner/organizations | getAll
[**get_org_limits**](PartnerOrganizationsControllerApi.md#get_org_limits) | **GET** /backend/rest/partner/organizations/{orgId}/limits | getOrgLimits


# **get_all**
> list[Organization] get_all()

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
api_instance = flexify_api.PartnerOrganizationsControllerApi(flexify_api.ApiClient(configuration))

try:
    # getAll
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerOrganizationsControllerApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_limits**
> UserConfig get_org_limits(org_id)

getOrgLimits

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
api_instance = flexify_api.PartnerOrganizationsControllerApi(flexify_api.ApiClient(configuration))
org_id = 789 # int | orgId

try:
    # getOrgLimits
    api_response = api_instance.get_org_limits(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerOrganizationsControllerApi->get_org_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| orgId | 

### Return type

[**UserConfig**](UserConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

