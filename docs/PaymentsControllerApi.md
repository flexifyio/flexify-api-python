# flexify_api.PaymentsControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_options**](PaymentsControllerApi.md#get_payment_options) | **GET** /backend/rest/pay/paddle/options | getPaymentOptions
[**payment_fulfilled**](PaymentsControllerApi.md#payment_fulfilled) | **GET** /backend/rest/pay/paddle/webhook | paymentFulfilled


# **get_payment_options**
> PaymentOptions get_payment_options(amount, currency)

getPaymentOptions

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
api_instance = flexify_api.PaymentsControllerApi(flexify_api.ApiClient(configuration))
amount = 1.2 # float | amount
currency = 'currency_example' # str | currency

try:
    # getPaymentOptions
    api_response = api_instance.get_payment_options(amount, currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsControllerApi->get_payment_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**| amount | 
 **currency** | **str**| currency | 

### Return type

[**PaymentOptions**](PaymentOptions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_fulfilled**
> payment_fulfilled()

paymentFulfilled

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
api_instance = flexify_api.PaymentsControllerApi(flexify_api.ApiClient(configuration))

try:
    # paymentFulfilled
    api_instance.payment_fulfilled()
except ApiException as e:
    print("Exception when calling PaymentsControllerApi->payment_fulfilled: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

