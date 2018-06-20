# Python API Client for Flexify.IO Management Console

With [Flexify.IO](https://flexify.io/), storing your data in a cloud does not imply dependency on a single provider anymore!

By unlocking your application from the specific cloud vendor or protocol, you finally gain the freedom to decide when and where to store your data.

And we took care about data migration too!


+ Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.4.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://flexify.io/](https://flexify.io/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Install directly from Github

```sh
pip install git+https://github.com/flexifyio/flexify-manage-api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/flexifyio/flexify-manage-api-client-python.git`)

Then import the package:
```python
import flexify_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flexify_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import flexify_api_client
from flexify_api_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = flexify_api_client.AuthenticationControllerApi()
authentication_request = flexify_api_client.AuthenticationRequest() # AuthenticationRequest | authenticationRequest

try:
    # Generate access token for user
    api_response = api_instance.authentication_request(authentication_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->authentication_request: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationControllerApi* | [**authentication_request**](docs/AuthenticationControllerApi.md#authentication_request) | **POST** /rest/auth | Generate access token for user
*AuthenticationControllerApi* | [**logout**](docs/AuthenticationControllerApi.md#logout) | **POST** /rest/auth/logout | Logout
*BillingAccountControllerApi* | [**get_costs_for_current_user**](docs/BillingAccountControllerApi.md#get_costs_for_current_user) | **GET** /rest/account/costs | Get costs for current user
*BillingAccountControllerApi* | [**get_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_current_user_billing_account) | **GET** /rest/account | Get billing account for current user
*BillingAccountControllerApi* | [**get_payments_for_current_user**](docs/BillingAccountControllerApi.md#get_payments_for_current_user) | **GET** /rest/account/payments | Get payments for current user
*CloudLocationsControllerApi* | [**get_available_locations_for_current_user**](docs/CloudLocationsControllerApi.md#get_available_locations_for_current_user) | **GET** /rest/cloud-locations | getAvailableLocationsForCurrentUser
*EndpointsControllerApi* | [**attach_storage_to_endpoint**](docs/EndpointsControllerApi.md#attach_storage_to_endpoint) | **POST** /rest/endpoints/{endpoint-id}/storages | Attach the storage to the endpoint
*EndpointsControllerApi* | [**detach_storage_from_endpoint**](docs/EndpointsControllerApi.md#detach_storage_from_endpoint) | **DELETE** /rest/endpoints/{endpoint-id}/storages/{storage-id} | Detach the storage from the endpoint
*EndpointsControllerApi* | [**disable**](docs/EndpointsControllerApi.md#disable) | **PUT** /rest/endpoints/{endpoint-id}/actions/disable | Disable the endpoint
*EndpointsControllerApi* | [**enable**](docs/EndpointsControllerApi.md#enable) | **PUT** /rest/endpoints/{endpoint-id}/actions/enable | Enable the endpoint
*EndpointsControllerApi* | [**get_endpoint_details**](docs/EndpointsControllerApi.md#get_endpoint_details) | **GET** /rest/endpoints/{endpoint-id} | Get endpoint details
*EndpointsControllerApi* | [**get_endpoints_for_current_user**](docs/EndpointsControllerApi.md#get_endpoints_for_current_user) | **GET** /rest/endpoints | Get endpoint for current user. This method will create new endpoint if no endpoints exist for user
*EndpointsControllerApi* | [**set_default_storage**](docs/EndpointsControllerApi.md#set_default_storage) | **PUT** /rest/endpoints/{endpoint-id}/storages/{storage-id}/actions/set-as-default | Set given storage as default for the endpoint
*EndpointsControllerApi* | [**update_endpoint**](docs/EndpointsControllerApi.md#update_endpoint) | **PUT** /rest/endpoints/{endpoint-id} | Update attributes of the endpoint
*LogControllerApi* | [**get_log_for_current_user**](docs/LogControllerApi.md#get_log_for_current_user) | **GET** /rest/log | getLogForCurrentUser
*MigrationsControllerApi* | [**add_migration**](docs/MigrationsControllerApi.md#add_migration) | **POST** /rest/migrations | Add new migration
*MigrationsControllerApi* | [**get_migration**](docs/MigrationsControllerApi.md#get_migration) | **GET** /rest/migrations/{migration-id} | Get migration by id. Only migration owner or administrator have access to the migration
*MigrationsControllerApi* | [**get_migrations**](docs/MigrationsControllerApi.md#get_migrations) | **GET** /rest/migrations | Get all migrations for logged in user in pagged mode
*MigrationsControllerApi* | [**hide_migration**](docs/MigrationsControllerApi.md#hide_migration) | **POST** /rest/migrations/{migration-id}/hide | Hide migration from UI
*MigrationsControllerApi* | [**stop_migration**](docs/MigrationsControllerApi.md#stop_migration) | **POST** /rest/migrations/{migration-id}/stop | Stop (cancel) the migration
*PaymentControllerApi* | [**get_payment_options**](docs/PaymentControllerApi.md#get_payment_options) | **GET** /rest/pay/paddle/options | getPaymentOptions
*PaymentControllerApi* | [**payment_fulfilled**](docs/PaymentControllerApi.md#payment_fulfilled) | **GET** /rest/pay/paddle/webhook | paymentFulfilled
*StoragesControllerApi* | [**add_storage_account**](docs/StoragesControllerApi.md#add_storage_account) | **POST** /rest/storage-accounts | Add Storage Account with an optional list of buckets
*StoragesControllerApi* | [**add_storages**](docs/StoragesControllerApi.md#add_storages) | **POST** /rest/storage-accounts/{storage-account-id}/storages | Add buckets to the storage account and optionally attach them to endpoint
*StoragesControllerApi* | [**delete_storage**](docs/StoragesControllerApi.md#delete_storage) | **DELETE** /rest/storage-accounts/{storage-account-id}/storages/{storage-id} | Delete Storage
*StoragesControllerApi* | [**delete_storages**](docs/StoragesControllerApi.md#delete_storages) | **POST** /rest/storage-accounts/actions/delete-storages | Deletes storages
*StoragesControllerApi* | [**generate_access_keys**](docs/StoragesControllerApi.md#generate_access_keys) | **GET** /rest/generate-access-keys | Generate new access keys pair
*StoragesControllerApi* | [**get_providers**](docs/StoragesControllerApi.md#get_providers) | **GET** /rest/providers | Get all storage providers
*StoragesControllerApi* | [**get_storage_accounts**](docs/StoragesControllerApi.md#get_storage_accounts) | **GET** /rest/storage-accounts | Get all storage accounts for current user
*StoragesControllerApi* | [**get_storages**](docs/StoragesControllerApi.md#get_storages) | **GET** /rest/storage-accounts/{storage-account-id}/storages | Get storages of the storage account
*StoragesControllerApi* | [**refresh_storage**](docs/StoragesControllerApi.md#refresh_storage) | **POST** /rest/storage-accounts/{storage-account-id}/storages/{storage-id}/actions/refresh | Refresh storage
*StoragesControllerApi* | [**refresh_storages**](docs/StoragesControllerApi.md#refresh_storages) | **POST** /rest/storage-accounts/actions/refresh-storages | Refresh storages
*StoragesControllerApi* | [**request_buckets**](docs/StoragesControllerApi.md#request_buckets) | **GET** /rest/buckets | Lists buckets of the external storage account
*StoragesControllerApi* | [**request_buckets_for_storage_account**](docs/StoragesControllerApi.md#request_buckets_for_storage_account) | **GET** /rest/storage-accounts/{storage-account-id}/buckets | Retrieve buckets from external cloud storage account
*UserControllerApi* | [**get_current_user**](docs/UserControllerApi.md#get_current_user) | **GET** /rest/user/current | Get details information for logged in user
*UserControllerApi* | [**request_reset_password**](docs/UserControllerApi.md#request_reset_password) | **POST** /rest/user/request-reset-password | requestResetPassword


## Documentation For Models

 - [AccessKeysPair](docs/AccessKeysPair.md)
 - [AddMigrationRequest](docs/AddMigrationRequest.md)
 - [AddStorageAccountRequest](docs/AddStorageAccountRequest.md)
 - [AddStoragesRequest](docs/AddStoragesRequest.md)
 - [AddStoragesResponse](docs/AddStoragesResponse.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [BillingAccount](docs/BillingAccount.md)
 - [BillingAccountWithMoney](docs/BillingAccountWithMoney.md)
 - [Bucket](docs/Bucket.md)
 - [ChangePasswordRequest](docs/ChangePasswordRequest.md)
 - [CloudLocation](docs/CloudLocation.md)
 - [CostDetails](docs/CostDetails.md)
 - [DataStorageStat](docs/DataStorageStat.md)
 - [DescribeOrganization](docs/DescribeOrganization.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointDetails](docs/EndpointDetails.md)
 - [EndpointStat](docs/EndpointStat.md)
 - [EndpointStorage](docs/EndpointStorage.md)
 - [IdResponse](docs/IdResponse.md)
 - [IdsList](docs/IdsList.md)
 - [LogEntry](docs/LogEntry.md)
 - [LogEvent](docs/LogEvent.md)
 - [Migration](docs/Migration.md)
 - [MigrationSlotStat](docs/MigrationSlotStat.md)
 - [MigrationStat](docs/MigrationStat.md)
 - [Money](docs/Money.md)
 - [PageMigration](docs/PageMigration.md)
 - [Pageable](docs/Pageable.md)
 - [Payment](docs/Payment.md)
 - [PaymentOptions](docs/PaymentOptions.md)
 - [PriceListEntry](docs/PriceListEntry.md)
 - [RequestResetPasswordReqeust](docs/RequestResetPasswordReqeust.md)
 - [ResetPasswordRequest](docs/ResetPasswordRequest.md)
 - [SignUpRequest](docs/SignUpRequest.md)
 - [SignupResult](docs/SignupResult.md)
 - [Sort](docs/Sort.md)
 - [Storage](docs/Storage.md)
 - [StorageAccount](docs/StorageAccount.md)
 - [StorageAccountCreateRequest](docs/StorageAccountCreateRequest.md)
 - [StorageProvider](docs/StorageProvider.md)
 - [User](docs/User.md)
 - [UserProfile](docs/UserProfile.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Contact us:

+ Information: [info@flexify.io](mailto:info@flexify.io)
+ Sales: [sales@flexify.io](mailto:sales@flexify.io)
+ Support: [support@flexify.io](mailto:support@flexify.io)

