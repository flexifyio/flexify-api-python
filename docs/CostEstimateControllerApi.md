# flexify_api.CostEstimateControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimate_migration_cost**](CostEstimateControllerApi.md#estimate_migration_cost) | **POST** /backend/rest/cost/migration | estimateMigrationCost


# **estimate_migration_cost**
> DtoMigrationCostEstimate estimate_migration_cost(migration_request)

estimateMigrationCost

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
api_instance = flexify_api.CostEstimateControllerApi(flexify_api.ApiClient(configuration))
migration_request = flexify_api.AddMigrationRequest() # AddMigrationRequest | migrationRequest

try:
    # estimateMigrationCost
    api_response = api_instance.estimate_migration_cost(migration_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostEstimateControllerApi->estimate_migration_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_request** | [**AddMigrationRequest**](AddMigrationRequest.md)| migrationRequest | 

### Return type

[**DtoMigrationCostEstimate**](DtoMigrationCostEstimate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

