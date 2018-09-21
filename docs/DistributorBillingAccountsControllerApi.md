# flexify_api.DistributorBillingAccountsControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_account**](DistributorBillingAccountsControllerApi.md#activate_account) | **PUT** /rest/distributor/accounts/{account-id}/actions/activate | activateAccount
[**add_payment**](DistributorBillingAccountsControllerApi.md#add_payment) | **POST** /rest/distributor/accounts/{account-id}/payments | addPayment
[**get_costs**](DistributorBillingAccountsControllerApi.md#get_costs) | **GET** /rest/distributor/accounts/{account-id}/costs | getCosts
[**get_details**](DistributorBillingAccountsControllerApi.md#get_details) | **GET** /rest/distributor/accounts/{account-id} | getDetails
[**get_payments**](DistributorBillingAccountsControllerApi.md#get_payments) | **GET** /rest/distributor/accounts/{account-id}/payments | getPayments
[**suspend_account**](DistributorBillingAccountsControllerApi.md#suspend_account) | **PUT** /rest/distributor/accounts/{account-id}/actions/suspend | suspendAccount


# **activate_account**
> activate_account(account_id)

activateAccount

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
api_instance = flexify_api.DistributorBillingAccountsControllerApi(flexify_api.ApiClient(configuration))
account_id = 789 # int | account-id

try:
    # activateAccount
    api_instance.activate_account(account_id)
except ApiException as e:
    print("Exception when calling DistributorBillingAccountsControllerApi->activate_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment**
> add_payment(account_id, payment_request)

addPayment

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
api_instance = flexify_api.DistributorBillingAccountsControllerApi(flexify_api.ApiClient(configuration))
account_id = 789 # int | account-id
payment_request = flexify_api.PaymentAddRequest() # PaymentAddRequest | paymentRequest

try:
    # addPayment
    api_instance.add_payment(account_id, payment_request)
except ApiException as e:
    print("Exception when calling DistributorBillingAccountsControllerApi->add_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account-id | 
 **payment_request** | [**PaymentAddRequest**](PaymentAddRequest.md)| paymentRequest | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_costs**
> list[CostDetails] get_costs(account_id)

getCosts

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
api_instance = flexify_api.DistributorBillingAccountsControllerApi(flexify_api.ApiClient(configuration))
account_id = 789 # int | account-id

try:
    # getCosts
    api_response = api_instance.get_costs(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributorBillingAccountsControllerApi->get_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account-id | 

### Return type

[**list[CostDetails]**](CostDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details**
> BillingAccountWithMoney get_details(account_id)

getDetails

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
api_instance = flexify_api.DistributorBillingAccountsControllerApi(flexify_api.ApiClient(configuration))
account_id = 789 # int | account-id

try:
    # getDetails
    api_response = api_instance.get_details(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributorBillingAccountsControllerApi->get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account-id | 

### Return type

[**BillingAccountWithMoney**](BillingAccountWithMoney.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments**
> list[Payment] get_payments(account_id)

getPayments

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
api_instance = flexify_api.DistributorBillingAccountsControllerApi(flexify_api.ApiClient(configuration))
account_id = 789 # int | account-id

try:
    # getPayments
    api_response = api_instance.get_payments(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributorBillingAccountsControllerApi->get_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account-id | 

### Return type

[**list[Payment]**](Payment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_account**
> suspend_account(account_id)

suspendAccount

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
api_instance = flexify_api.DistributorBillingAccountsControllerApi(flexify_api.ApiClient(configuration))
account_id = 789 # int | account-id

try:
    # suspendAccount
    api_instance.suspend_account(account_id)
except ApiException as e:
    print("Exception when calling DistributorBillingAccountsControllerApi->suspend_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account-id | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

