# flexify_api.BillingAccountControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_costs_for_current_user_billing_account**](BillingAccountControllerApi.md#get_costs_for_current_user_billing_account) | **GET** /backend/rest/account/costs | Get costs for current user
[**get_current_user_billing_account**](BillingAccountControllerApi.md#get_current_user_billing_account) | **GET** /backend/rest/account | Get billing account for current user
[**get_payments_for_current_user**](BillingAccountControllerApi.md#get_payments_for_current_user) | **GET** /backend/rest/account/payments | Get payments for current user


# **get_costs_for_current_user_billing_account**
> list[CostDetails] get_costs_for_current_user_billing_account()

Get costs for current user

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
api_instance = flexify_api.BillingAccountControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get costs for current user
    api_response = api_instance.get_costs_for_current_user_billing_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAccountControllerApi->get_costs_for_current_user_billing_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CostDetails]**](CostDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_billing_account**
> BillingAccount get_current_user_billing_account()

Get billing account for current user

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
api_instance = flexify_api.BillingAccountControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get billing account for current user
    api_response = api_instance.get_current_user_billing_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAccountControllerApi->get_current_user_billing_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_for_current_user**
> list[Payment] get_payments_for_current_user()

Get payments for current user

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
api_instance = flexify_api.BillingAccountControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get payments for current user
    api_response = api_instance.get_payments_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingAccountControllerApi->get_payments_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Payment]**](Payment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

