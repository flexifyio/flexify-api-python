# flexify_api.AzureIntegrationOAuthControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_azure_integration**](AzureIntegrationOAuthControllerApi.md#add_azure_integration) | **POST** /backend/rest/azure-integration | Add new Azure integration
[**auth_storage**](AzureIntegrationOAuthControllerApi.md#auth_storage) | **POST** /backend/rest/azure-integration/{azure-integration-id}/actions/auth-storage | Authenticate Azure integration storage access
[**delete_azure_integration**](AzureIntegrationOAuthControllerApi.md#delete_azure_integration) | **DELETE** /backend/rest/azure-integration/{azure-integration-id} | Deletes (hides) Azure integration by Id
[**get_azure_integrations**](AzureIntegrationOAuthControllerApi.md#get_azure_integrations) | **GET** /backend/rest/azure-integration | Get Azure integration by id
[**get_config_for_azure_integration**](AzureIntegrationOAuthControllerApi.md#get_config_for_azure_integration) | **GET** /backend/rest/azure-integration/oauth/config | Get OAuth configuration to authorize Azure integration
[**get_device_code_for_azure_integration_management**](AzureIntegrationOAuthControllerApi.md#get_device_code_for_azure_integration_management) | **GET** /backend/rest/azure-integration/oauth/device-code/management | Request device code to authorize Azure integration with device code flow (management access)
[**get_device_code_for_azure_integration_storage**](AzureIntegrationOAuthControllerApi.md#get_device_code_for_azure_integration_storage) | **GET** /backend/rest/azure-integration/oauth/device-code/storage | Request device code to authorize Azure integration with device code flow (storage access)
[**get_storage_accounts_from_azure**](AzureIntegrationOAuthControllerApi.md#get_storage_accounts_from_azure) | **GET** /backend/rest/azure-integration/{azure-integration-id}/storage-accounts-list | Use Azure integration to get list of storage accounts from Azure
[**reauth_azure_integration**](AzureIntegrationOAuthControllerApi.md#reauth_azure_integration) | **POST** /backend/rest/azure-integration/{azure-integration-id}/actions/reauth | Reauthenticate Azure integration


# **add_azure_integration**
> IdResponse add_azure_integration(request)

Add new Azure integration

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.FinishOAuthParams() # FinishOAuthParams | request

try:
    # Add new Azure integration
    api_response = api_instance.add_azure_integration(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->add_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FinishOAuthParams**](FinishOAuthParams.md)| request | 

### Return type

[**IdResponse**](IdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_storage**
> auth_storage(auth_params, azure_integration_id)

Authenticate Azure integration storage access

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))
auth_params = flexify_api.FinishOAuthParams() # FinishOAuthParams | authParams
azure_integration_id = 789 # int | azure-integration-id

try:
    # Authenticate Azure integration storage access
    api_instance.auth_storage(auth_params, azure_integration_id)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->auth_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_params** | [**FinishOAuthParams**](FinishOAuthParams.md)| authParams | 
 **azure_integration_id** | **int**| azure-integration-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_integration**
> delete_azure_integration(azure_integration_id)

Deletes (hides) Azure integration by Id

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))
azure_integration_id = 789 # int | azure-integration-id

try:
    # Deletes (hides) Azure integration by Id
    api_instance.delete_azure_integration(azure_integration_id)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->delete_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_integration_id** | **int**| azure-integration-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_integrations**
> list[AzureIntegration] get_azure_integrations()

Get Azure integration by id

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get Azure integration by id
    api_response = api_instance.get_azure_integrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->get_azure_integrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AzureIntegration]**](AzureIntegration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_for_azure_integration**
> MicrosoftOAuthConfig get_config_for_azure_integration()

Get OAuth configuration to authorize Azure integration

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get OAuth configuration to authorize Azure integration
    api_response = api_instance.get_config_for_azure_integration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->get_config_for_azure_integration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MicrosoftOAuthConfig**](MicrosoftOAuthConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_code_for_azure_integration_management**
> OAuth2DeviceCodeResponse get_device_code_for_azure_integration_management()

Request device code to authorize Azure integration with device code flow (management access)

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))

try:
    # Request device code to authorize Azure integration with device code flow (management access)
    api_response = api_instance.get_device_code_for_azure_integration_management()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->get_device_code_for_azure_integration_management: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuth2DeviceCodeResponse**](OAuth2DeviceCodeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_code_for_azure_integration_storage**
> OAuth2DeviceCodeResponse get_device_code_for_azure_integration_storage()

Request device code to authorize Azure integration with device code flow (storage access)

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))

try:
    # Request device code to authorize Azure integration with device code flow (storage access)
    api_response = api_instance.get_device_code_for_azure_integration_storage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->get_device_code_for_azure_integration_storage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuth2DeviceCodeResponse**](OAuth2DeviceCodeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_accounts_from_azure**
> list[AzureSubscriptionInfoWithStorages] get_storage_accounts_from_azure(azure_integration_id)

Use Azure integration to get list of storage accounts from Azure

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))
azure_integration_id = 789 # int | azure-integration-id

try:
    # Use Azure integration to get list of storage accounts from Azure
    api_response = api_instance.get_storage_accounts_from_azure(azure_integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->get_storage_accounts_from_azure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_integration_id** | **int**| azure-integration-id | 

### Return type

[**list[AzureSubscriptionInfoWithStorages]**](AzureSubscriptionInfoWithStorages.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reauth_azure_integration**
> reauth_azure_integration(auth_params, azure_integration_id)

Reauthenticate Azure integration

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
api_instance = flexify_api.AzureIntegrationOAuthControllerApi(flexify_api.ApiClient(configuration))
auth_params = flexify_api.FinishOAuthParams() # FinishOAuthParams | authParams
azure_integration_id = 789 # int | azure-integration-id

try:
    # Reauthenticate Azure integration
    api_instance.reauth_azure_integration(auth_params, azure_integration_id)
except ApiException as e:
    print("Exception when calling AzureIntegrationOAuthControllerApi->reauth_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_params** | [**FinishOAuthParams**](FinishOAuthParams.md)| authParams | 
 **azure_integration_id** | **int**| azure-integration-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

