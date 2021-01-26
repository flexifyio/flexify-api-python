# Python API Client for Flexify.IO Management Console

With [Flexify.IO](https://flexify.io/), storing your data in a cloud does not imply dependency on a single provider anymore!

By unlocking your application from the specific cloud vendor or protocol, you finally gain the freedom to decide when and where to store your data. And we can migrate data too!

+ Get API token
+ Enjoy Flexify.IO REST API

- API version: 2.12.1

## Requirements

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
import flexify_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flexify_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = flexify_api.AuthenticationControllerApi()
authentication_request = flexify_api.AuthenticationRequest() # AuthenticationRequest | authenticationRequest

try:
    # Generate access token for user
    api_response = api_instance.authentication_request(authentication_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->authentication_request: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.flexify.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthControllerApi* | [**authenticate**](docs/AuthControllerApi.md#authenticate) | **POST** /backend/rest/auth | Generate new access token for the user
*AuthControllerApi* | [**authorize**](docs/AuthControllerApi.md#authorize) | **POST** /backend/rest/auth/authorize | Authorization check of given token
*AuthControllerApi* | [**get_config**](docs/AuthControllerApi.md#get_config) | **GET** /backend/rest/auth/config | Logout
*AuthControllerApi* | [**logout**](docs/AuthControllerApi.md#logout) | **POST** /backend/rest/auth/logout | Logout
*BillingAccountControllerApi* | [**get_costs_for_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_costs_for_current_user_billing_account) | **GET** /backend/rest/account/costs | Get costs for current user
*BillingAccountControllerApi* | [**get_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_current_user_billing_account) | **GET** /backend/rest/account | Get billing account for current user
*BillingAccountControllerApi* | [**get_payments_for_current_user**](docs/BillingAccountControllerApi.md#get_payments_for_current_user) | **GET** /backend/rest/account/payments | Get payments for current user
*CloudLocationsControllerApi* | [**get_auto_deploy_available_locations_for_current_user**](docs/CloudLocationsControllerApi.md#get_auto_deploy_available_locations_for_current_user) | **GET** /backend/rest/cloud-locations/auto-deploy | getAutoDeployAvailableLocationsForCurrentUser
*CloudLocationsControllerApi* | [**get_existing_available_locations_for_current_user**](docs/CloudLocationsControllerApi.md#get_existing_available_locations_for_current_user) | **GET** /backend/rest/cloud-locations | getExistingAvailableLocationsForCurrentUser
*CostEstimateControllerApi* | [**estimate_migration_cost**](docs/CostEstimateControllerApi.md#estimate_migration_cost) | **POST** /backend/rest/cost/migration | estimateMigrationCost
*EndpointsControllerApi* | [**attach_accounts**](docs/EndpointsControllerApi.md#attach_accounts) | **POST** /backend/rest/endpoints/{endpoint-id}/storage-accounts | Attach storage accounts to the endpoint
*EndpointsControllerApi* | [**attach_buckets**](docs/EndpointsControllerApi.md#attach_buckets) | **POST** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets | Attach storages to the virtual bucket
*EndpointsControllerApi* | [**create_endpoint**](docs/EndpointsControllerApi.md#create_endpoint) | **POST** /backend/rest/endpoints | Creates new endpoint
*EndpointsControllerApi* | [**create_virtual_bucket**](docs/EndpointsControllerApi.md#create_virtual_bucket) | **POST** /backend/rest/endpoints/{endpoint-id}/virtual-buckets | Creates new virtual bucket
*EndpointsControllerApi* | [**delete**](docs/EndpointsControllerApi.md#delete) | **DELETE** /backend/rest/endpoints/{endpoint-id} | Delete the endpoint
*EndpointsControllerApi* | [**delete_virtual_bucket**](docs/EndpointsControllerApi.md#delete_virtual_bucket) | **DELETE** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket} | Deletes virtual bucket
*EndpointsControllerApi* | [**detach_account**](docs/EndpointsControllerApi.md#detach_account) | **DELETE** /backend/rest/endpoints/{endpoint-id}/storage-accounts/{storage-account-id} | Detach storage account from the endpoint
*EndpointsControllerApi* | [**detach_bucket**](docs/EndpointsControllerApi.md#detach_bucket) | **DELETE** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets/{bucket-id} | Detach storage account from the endpoint
*EndpointsControllerApi* | [**disable**](docs/EndpointsControllerApi.md#disable) | **PUT** /backend/rest/endpoints/{endpoint-id}/actions/disable | Disable the endpoint
*EndpointsControllerApi* | [**enable**](docs/EndpointsControllerApi.md#enable) | **PUT** /backend/rest/endpoints/{endpoint-id}/actions/enable | Enable the endpoint
*EndpointsControllerApi* | [**generate_access_keys**](docs/EndpointsControllerApi.md#generate_access_keys) | **GET** /backend/rest/endpoints/generated-access-keys | Generate new access keys pair
*EndpointsControllerApi* | [**get_endpoint_details**](docs/EndpointsControllerApi.md#get_endpoint_details) | **GET** /backend/rest/endpoints/{endpoint-id} | Get endpoint details
*EndpointsControllerApi* | [**get_endpoints_for_current_user**](docs/EndpointsControllerApi.md#get_endpoints_for_current_user) | **GET** /backend/rest/endpoints | Get endpoint for current user. This method will create new endpoint if no endpoints exist for user
*EndpointsControllerApi* | [**set_attached_account_settings**](docs/EndpointsControllerApi.md#set_attached_account_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/storage-accounts/{storage-account-id}/settings | Modifies settings of the attached storage account
*EndpointsControllerApi* | [**set_attached_bucket_settings**](docs/EndpointsControllerApi.md#set_attached_bucket_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets/{bucket-id}/settings | Modifies settings of the attached storage
*EndpointsControllerApi* | [**set_virtual_bucket_settings**](docs/EndpointsControllerApi.md#set_virtual_bucket_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/settings | Modifies virtual bucket configuration
*EndpointsControllerApi* | [**update_endpoint_settings**](docs/EndpointsControllerApi.md#update_endpoint_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/settings | Update attributes of the endpoint
*LogControllerApi* | [**get_log_for_current_user**](docs/LogControllerApi.md#get_log_for_current_user) | **GET** /backend/rest/log | getLogForCurrentUser
*MigrationsControllerApi* | [**add_migration**](docs/MigrationsControllerApi.md#add_migration) | **POST** /backend/rest/migrations | Add new migration
*MigrationsControllerApi* | [**get_migration**](docs/MigrationsControllerApi.md#get_migration) | **GET** /backend/rest/migrations/{migration-id} | Get migration by id. Only migration owner or administrator have access to the migration
*MigrationsControllerApi* | [**get_migrations**](docs/MigrationsControllerApi.md#get_migrations) | **GET** /backend/rest/migrations | Get all migrations for logged in user in paged mode
*MigrationsControllerApi* | [**hide_all_migrations**](docs/MigrationsControllerApi.md#hide_all_migrations) | **POST** /backend/rest/migrations/actions/hide-all | Mark all unfinished migrations as hidden UI
*MigrationsControllerApi* | [**hide_migration**](docs/MigrationsControllerApi.md#hide_migration) | **POST** /backend/rest/migrations/{migration-id}/actions/hide | Mark migration as hidden
*MigrationsControllerApi* | [**restart_slot**](docs/MigrationsControllerApi.md#restart_slot) | **POST** /backend/rest/migrations/{migration-id}/mappings/{mapping-id}/slots/{slot}/actions/restart | Mark migration as hidden
*MigrationsControllerApi* | [**stop_migration**](docs/MigrationsControllerApi.md#stop_migration) | **POST** /backend/rest/migrations/{migration-id}/actions/stop | Stop (cancel) the migration
*OAuthControllerApi* | [**get_app_info**](docs/OAuthControllerApi.md#get_app_info) | **GET** /backend/rest/oauth/app-info | getAppInfo
*PaymentsControllerApi* | [**get_payment_options**](docs/PaymentsControllerApi.md#get_payment_options) | **GET** /backend/rest/pay/paddle/options | getPaymentOptions
*PaymentsControllerApi* | [**payment_fulfilled**](docs/PaymentsControllerApi.md#payment_fulfilled) | **GET** /backend/rest/pay/paddle/webhook | paymentFulfilled
*StorageAccountsControllerApi* | [**add_storage_account**](docs/StorageAccountsControllerApi.md#add_storage_account) | **POST** /backend/rest/storage-accounts | Add Storage Account with an optional list of buckets
*StorageAccountsControllerApi* | [**delete_storage_account**](docs/StorageAccountsControllerApi.md#delete_storage_account) | **DELETE** /backend/rest/storage-accounts/{storage-account-id} | Deletes (hides) storage account and all its buckets/containers
*StorageAccountsControllerApi* | [**delete_storage_accounts**](docs/StorageAccountsControllerApi.md#delete_storage_accounts) | **POST** /backend/rest/storage-accounts/actions/delete | Deletes (hides) a multiple storage accounts and all their buckets/containers
*StorageAccountsControllerApi* | [**get_storage_account**](docs/StorageAccountsControllerApi.md#get_storage_account) | **GET** /backend/rest/storage-accounts/storage-accounts/{storage-account-id} | Get storage account by id
*StorageAccountsControllerApi* | [**get_storage_accounts**](docs/StorageAccountsControllerApi.md#get_storage_accounts) | **GET** /backend/rest/storage-accounts | Get all storage accounts for current user
*StorageAccountsControllerApi* | [**refresh_storage_account**](docs/StorageAccountsControllerApi.md#refresh_storage_account) | **POST** /backend/rest/storage-accounts/{storage-account-id}/actions/refresh | Requests and updates list of buckets/containers for the storage account
*StorageAccountsControllerApi* | [**refresh_storage_accounts**](docs/StorageAccountsControllerApi.md#refresh_storage_accounts) | **POST** /backend/rest/storage-accounts/actions/refresh | Requests and updates list of buckets/containers for a list of storage accounts
*StorageAccountsControllerApi* | [**set_storage_account_settings**](docs/StorageAccountsControllerApi.md#set_storage_account_settings) | **PUT** /backend/rest/storage-accounts/{storage-account-id}/settings | Updates storage account settings
*StoragesControllerApi* | [**add_buckets**](docs/StoragesControllerApi.md#add_buckets) | **POST** /backend/rest/storage-accounts/{storage-account-id}/buckets | Add buckets to the storage account
*StoragesControllerApi* | [**delete_bucket**](docs/StoragesControllerApi.md#delete_bucket) | **DELETE** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Deletes (hides) a bucket/container
*StoragesControllerApi* | [**delete_buckets**](docs/StoragesControllerApi.md#delete_buckets) | **POST** /backend/rest/storage-accounts/actions/delete-buckets | Deletes (hides) multiple buckets/containers
*StoragesControllerApi* | [**get_providers**](docs/StoragesControllerApi.md#get_providers) | **GET** /backend/rest/providers | Get all storage providers
*StoragesControllerApi* | [**refresh_bucket**](docs/StoragesControllerApi.md#refresh_bucket) | **POST** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}/actions/refresh | Refresh statistics of a single bucket
*StoragesControllerApi* | [**refresh_buckets**](docs/StoragesControllerApi.md#refresh_buckets) | **POST** /backend/rest/storage-accounts/actions/refresh-buckets | Refresh statistics of multiple buckets
*UserControllerApi* | [**get_current_user**](docs/UserControllerApi.md#get_current_user) | **GET** /backend/rest/user/current | Get details of user corresponding to provided auth token
*UserControllerApi* | [**request_delete**](docs/UserControllerApi.md#request_delete) | **POST** /backend/rest/user/request-delete | requestDelete
*UserControllerApi* | [**request_reset_password**](docs/UserControllerApi.md#request_reset_password) | **POST** /backend/rest/user/request-reset-password | requestResetPassword


## Documentation For Models

 - [AccessKeysPair](docs/AccessKeysPair.md)
 - [AddMigrationRequest](docs/AddMigrationRequest.md)
 - [AddMigrationRequestMapping](docs/AddMigrationRequestMapping.md)
 - [AddStorageAccountRequest](docs/AddStorageAccountRequest.md)
 - [AttachStorageAccountsRequest](docs/AttachStorageAccountsRequest.md)
 - [AttachVirtualBucketStoragesRequest](docs/AttachVirtualBucketStoragesRequest.md)
 - [AuthAppInfo](docs/AuthAppInfo.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [AuthorizationResponse](docs/AuthorizationResponse.md)
 - [BillingAccount](docs/BillingAccount.md)
 - [BillingAccountWithMoney](docs/BillingAccountWithMoney.md)
 - [Bucket](docs/Bucket.md)
 - [BucketStat](docs/BucketStat.md)
 - [BucketsRequest](docs/BucketsRequest.md)
 - [ChangePasswordRequest](docs/ChangePasswordRequest.md)
 - [CleanupStat](docs/CleanupStat.md)
 - [CloudLocation](docs/CloudLocation.md)
 - [CloudLocationReq](docs/CloudLocationReq.md)
 - [CloudLocationRes](docs/CloudLocationRes.md)
 - [CostDetails](docs/CostDetails.md)
 - [CreateVirtualBucketRequest](docs/CreateVirtualBucketRequest.md)
 - [Distributor](docs/Distributor.md)
 - [DtoMappingCostEstimate](docs/DtoMappingCostEstimate.md)
 - [DtoMappingCostEstimateEntry](docs/DtoMappingCostEstimateEntry.md)
 - [DtoMigrationCostEstimate](docs/DtoMigrationCostEstimate.md)
 - [EndpointDetails](docs/EndpointDetails.md)
 - [EndpointSettings](docs/EndpointSettings.md)
 - [EndpointStat](docs/EndpointStat.md)
 - [EndpointStorageAccountReq](docs/EndpointStorageAccountReq.md)
 - [EndpointStorageAccountRes](docs/EndpointStorageAccountRes.md)
 - [EndpointStorageAccountSettings](docs/EndpointStorageAccountSettings.md)
 - [GrantedAuthority](docs/GrantedAuthority.md)
 - [IdResponse](docs/IdResponse.md)
 - [IdsList](docs/IdsList.md)
 - [LogEntry](docs/LogEntry.md)
 - [LogEvent](docs/LogEvent.md)
 - [LogoutRequest](docs/LogoutRequest.md)
 - [Mapping](docs/Mapping.md)
 - [MappingStat](docs/MappingStat.md)
 - [MarkerPageLogEntry](docs/MarkerPageLogEntry.md)
 - [Migration](docs/Migration.md)
 - [MigrationSettings](docs/MigrationSettings.md)
 - [MigrationSettingsReq](docs/MigrationSettingsReq.md)
 - [MigrationSettingsRes](docs/MigrationSettingsRes.md)
 - [MigrationStat](docs/MigrationStat.md)
 - [Money](docs/Money.md)
 - [NewStorageAccount](docs/NewStorageAccount.md)
 - [Organization](docs/Organization.md)
 - [PageMigration](docs/PageMigration.md)
 - [Pageable](docs/Pageable.md)
 - [Payment](docs/Payment.md)
 - [PaymentOptions](docs/PaymentOptions.md)
 - [Price](docs/Price.md)
 - [PriceConstraints](docs/PriceConstraints.md)
 - [PriceList](docs/PriceList.md)
 - [PublicAuthenticationConfiguration](docs/PublicAuthenticationConfiguration.md)
 - [RequestResetPasswordRequest](docs/RequestResetPasswordRequest.md)
 - [ResetPasswordRequest](docs/ResetPasswordRequest.md)
 - [SignUpRequest](docs/SignUpRequest.md)
 - [SignupResult](docs/SignupResult.md)
 - [Slot](docs/Slot.md)
 - [SlotStat](docs/SlotStat.md)
 - [Sort](docs/Sort.md)
 - [StorageAccount](docs/StorageAccount.md)
 - [StorageAccountSettings](docs/StorageAccountSettings.md)
 - [StorageAccountSettingsReq](docs/StorageAccountSettingsReq.md)
 - [StorageAccountSettingsRes](docs/StorageAccountSettingsRes.md)
 - [StorageAccountStat](docs/StorageAccountStat.md)
 - [StorageProvider](docs/StorageProvider.md)
 - [User](docs/User.md)
 - [UserConfig](docs/UserConfig.md)
 - [UserProfile](docs/UserProfile.md)
 - [UserSettings](docs/UserSettings.md)
 - [VirtualBucket](docs/VirtualBucket.md)
 - [VirtualBucketSettings](docs/VirtualBucketSettings.md)
 - [VirtualBucketStorageReq](docs/VirtualBucketStorageReq.md)
 - [VirtualBucketStorageRes](docs/VirtualBucketStorageRes.md)
 - [VirtualBucketStorageSettings](docs/VirtualBucketStorageSettings.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Contact us:

+ Information: [info@flexify.io](mailto:info@flexify.io)
+ Sales: [sales@flexify.io](mailto:sales@flexify.io)
+ Support: [support@flexify.io](mailto:support@flexify.io)

