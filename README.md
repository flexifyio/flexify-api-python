# Python API Client for Flexify IO Management Console

With [Flexify IO](https://flexify.io/), storing your data in a cloud does not imply dependency on a single provider anymore!

By unlocking your application from the specific cloud vendor or protocol, you finally gain the freedom to decide when and where to store your data. And we can migrate data too!

+ Get API token
+ Enjoy Flexify IO REST API

- API version: 2.14.2

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
*AuthControllerApi* | [**check_token_and_get_user**](docs/AuthControllerApi.md#check_token_and_get_user) | **GET** /backend/rest/auth/user | Check of given token
*AuthControllerApi* | [**logout**](docs/AuthControllerApi.md#logout) | **POST** /backend/rest/auth/logout | Logout
*AuthSsoControllerApi* | [**get_config**](docs/AuthSsoControllerApi.md#get_config) | **GET** /backend/rest/auth/sso/config | getConfig
*AuthSsoControllerApi* | [**get_device_code**](docs/AuthSsoControllerApi.md#get_device_code) | **GET** /backend/rest/auth/sso/device-code | getDeviceCode
*AuthSsoControllerApi* | [**get_token_by_device_code**](docs/AuthSsoControllerApi.md#get_token_by_device_code) | **POST** /backend/rest/auth/sso/token-by-device-code | getTokenByDeviceCode
*AuthSsoControllerApi* | [**refresh_token_for_device_code_flow**](docs/AuthSsoControllerApi.md#refresh_token_for_device_code_flow) | **POST** /backend/rest/auth/sso/token-refresh | refreshTokenForDeviceCodeFlow
*AzureIntegrationOAuthControllerApi* | [**add_azure_integration**](docs/AzureIntegrationOAuthControllerApi.md#add_azure_integration) | **POST** /backend/rest/azure-integration | Add new Azure integration
*AzureIntegrationOAuthControllerApi* | [**auth_storage**](docs/AzureIntegrationOAuthControllerApi.md#auth_storage) | **POST** /backend/rest/azure-integration/{azure-integration-id}/actions/auth-storage | Authenticate Azure integration storage access
*AzureIntegrationOAuthControllerApi* | [**delete_azure_integration**](docs/AzureIntegrationOAuthControllerApi.md#delete_azure_integration) | **DELETE** /backend/rest/azure-integration/{azure-integration-id} | Deletes (hides) Azure integration by Id
*AzureIntegrationOAuthControllerApi* | [**get_azure_integrations**](docs/AzureIntegrationOAuthControllerApi.md#get_azure_integrations) | **GET** /backend/rest/azure-integration | Get Azure integration by id
*AzureIntegrationOAuthControllerApi* | [**get_config_for_azure_integration**](docs/AzureIntegrationOAuthControllerApi.md#get_config_for_azure_integration) | **GET** /backend/rest/azure-integration/oauth/config | Get OAuth configuration to authorize Azure integration
*AzureIntegrationOAuthControllerApi* | [**get_device_code_for_azure_integration_management**](docs/AzureIntegrationOAuthControllerApi.md#get_device_code_for_azure_integration_management) | **GET** /backend/rest/azure-integration/oauth/device-code/management | Request device code to authorize Azure integration with device code flow (management access)
*AzureIntegrationOAuthControllerApi* | [**get_device_code_for_azure_integration_storage**](docs/AzureIntegrationOAuthControllerApi.md#get_device_code_for_azure_integration_storage) | **GET** /backend/rest/azure-integration/oauth/device-code/storage | Request device code to authorize Azure integration with device code flow (storage access)
*AzureIntegrationOAuthControllerApi* | [**get_storage_accounts_from_azure**](docs/AzureIntegrationOAuthControllerApi.md#get_storage_accounts_from_azure) | **GET** /backend/rest/azure-integration/{azure-integration-id}/storage-accounts-list | Use Azure integration to get list of storage accounts from Azure
*AzureIntegrationOAuthControllerApi* | [**reauth_azure_integration**](docs/AzureIntegrationOAuthControllerApi.md#reauth_azure_integration) | **POST** /backend/rest/azure-integration/{azure-integration-id}/actions/reauth | Reauthenticate Azure integration
*BillingAccountControllerApi* | [**get_costs_for_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_costs_for_current_user_billing_account) | **GET** /backend/rest/account/costs | Get costs for current user
*BillingAccountControllerApi* | [**get_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_current_user_billing_account) | **GET** /backend/rest/account | Get billing account for current user
*BillingAccountControllerApi* | [**get_payments_for_current_user**](docs/BillingAccountControllerApi.md#get_payments_for_current_user) | **GET** /backend/rest/account/payments | Get payments for current user
*CloudLocationsControllerApi* | [**get_auto_deploy_available_locations_for_current_user**](docs/CloudLocationsControllerApi.md#get_auto_deploy_available_locations_for_current_user) | **GET** /backend/rest/cloud-locations/auto-deploy | getAutoDeployAvailableLocationsForCurrentUser
*CloudLocationsControllerApi* | [**get_existing_available_locations_for_current_user**](docs/CloudLocationsControllerApi.md#get_existing_available_locations_for_current_user) | **GET** /backend/rest/cloud-locations | getExistingAvailableLocationsForCurrentUser
*ConfigControllerApi* | [**get_config1**](docs/ConfigControllerApi.md#get_config1) | **GET** /backend/rest/config | Get public Management Server config
*CostEstimateControllerApi* | [**estimate_migration_cost**](docs/CostEstimateControllerApi.md#estimate_migration_cost) | **POST** /backend/rest/cost/migration | estimateMigrationCost
*EndpointsControllerApi* | [**attach_accounts**](docs/EndpointsControllerApi.md#attach_accounts) | **POST** /backend/rest/endpoints/{endpoint-id}/storage-accounts | Attach storage accounts to the endpoint
*EndpointsControllerApi* | [**attach_buckets**](docs/EndpointsControllerApi.md#attach_buckets) | **POST** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets | Attach storages to the virtual bucket
*EndpointsControllerApi* | [**change_accounts**](docs/EndpointsControllerApi.md#change_accounts) | **PUT** /backend/rest/endpoints/{endpoint-id}/storage-accounts | Modified all storage accounts to the endpoint
*EndpointsControllerApi* | [**change_buckets**](docs/EndpointsControllerApi.md#change_buckets) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets | Replaces the list of storages attached to the virtual bucket
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
*EndpointsControllerApi* | [**get_endpoint_secret_key**](docs/EndpointsControllerApi.md#get_endpoint_secret_key) | **GET** /backend/rest/endpoints/{endpoint-id}/settings/secret-key | Get endpoint secret key
*EndpointsControllerApi* | [**get_endpoints_for_current_user**](docs/EndpointsControllerApi.md#get_endpoints_for_current_user) | **GET** /backend/rest/endpoints | Get the list of endpoints for current user optionally filtering by name or identity using SQL LIKE syntax
*EndpointsControllerApi* | [**set_attached_account_settings**](docs/EndpointsControllerApi.md#set_attached_account_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/storage-accounts/{storage-account-id}/settings | Modifies settings of the attached storage account
*EndpointsControllerApi* | [**set_attached_bucket_settings**](docs/EndpointsControllerApi.md#set_attached_bucket_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/buckets/{bucket-id}/settings | Modifies settings of the attached storage
*EndpointsControllerApi* | [**set_virtual_bucket_settings**](docs/EndpointsControllerApi.md#set_virtual_bucket_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/virtual-buckets/{virtual-bucket}/settings | Modifies virtual bucket configuration
*EndpointsControllerApi* | [**update_endpoint_settings**](docs/EndpointsControllerApi.md#update_endpoint_settings) | **PUT** /backend/rest/endpoints/{endpoint-id}/settings | Update attributes of the endpoint
*ImpersonationControllerApi* | [**add_impersonate_code**](docs/ImpersonationControllerApi.md#add_impersonate_code) | **POST** /backend/rest/impersonate/codes | addImpersonateCode
*ImpersonationControllerApi* | [**add_impersonate_from_user**](docs/ImpersonationControllerApi.md#add_impersonate_from_user) | **POST** /backend/rest/impersonate/from | addImpersonateFromUser
*ImpersonationControllerApi* | [**get_impersonate_codes_list**](docs/ImpersonationControllerApi.md#get_impersonate_codes_list) | **GET** /backend/rest/impersonate/codes | getImpersonateCodesList
*ImpersonationControllerApi* | [**get_impersonate_from_list**](docs/ImpersonationControllerApi.md#get_impersonate_from_list) | **GET** /backend/rest/impersonate/from | getImpersonateFromList
*ImpersonationControllerApi* | [**get_impersonate_to_list**](docs/ImpersonationControllerApi.md#get_impersonate_to_list) | **GET** /backend/rest/impersonate/to | getImpersonateToList
*ImpersonationControllerApi* | [**impersonate**](docs/ImpersonationControllerApi.md#impersonate) | **POST** /backend/rest/impersonate/as/{userId} | impersonate
*ImpersonationControllerApi* | [**remove_impersonate_from_user**](docs/ImpersonationControllerApi.md#remove_impersonate_from_user) | **DELETE** /backend/rest/impersonate/from/{user-id} | removeImpersonateFromUser
*ImpersonationControllerApi* | [**remove_impersonate_from_user1**](docs/ImpersonationControllerApi.md#remove_impersonate_from_user1) | **DELETE** /backend/rest/impersonate/codes/{code} | removeImpersonateFromUser
*LogControllerApi* | [**get_log_for_current_user**](docs/LogControllerApi.md#get_log_for_current_user) | **GET** /backend/rest/log | getLogForCurrentUser
*MigrationsControllerApi* | [**add_migration**](docs/MigrationsControllerApi.md#add_migration) | **POST** /backend/rest/migrations | Add new migration
*MigrationsControllerApi* | [**get_migration**](docs/MigrationsControllerApi.md#get_migration) | **GET** /backend/rest/migrations/{migration-id} | Get migration by id. Only migration owner or administrator have access to the migration
*MigrationsControllerApi* | [**get_migrations**](docs/MigrationsControllerApi.md#get_migrations) | **GET** /backend/rest/migrations | Get all migrations for logged in user in paged mode
*MigrationsControllerApi* | [**hide_all_migrations**](docs/MigrationsControllerApi.md#hide_all_migrations) | **POST** /backend/rest/migrations/actions/hide-all | Mark all unfinished migrations as hidden UI
*MigrationsControllerApi* | [**hide_migration**](docs/MigrationsControllerApi.md#hide_migration) | **POST** /backend/rest/migrations/{migration-id}/actions/hide | Mark migration as hidden
*MigrationsControllerApi* | [**restart_slot**](docs/MigrationsControllerApi.md#restart_slot) | **POST** /backend/rest/migrations/{migration-id}/mappings/{mapping-id}/slots/{slot}/actions/restart | Mark migration as hidden
*MigrationsControllerApi* | [**stop_migration**](docs/MigrationsControllerApi.md#stop_migration) | **POST** /backend/rest/migrations/{migration-id}/actions/stop | Stop (cancel) the migration
*PartnerOrganizationsControllerApi* | [**get_all**](docs/PartnerOrganizationsControllerApi.md#get_all) | **GET** /backend/rest/partner/organizations | getAll
*PartnerOrganizationsControllerApi* | [**get_org_limits**](docs/PartnerOrganizationsControllerApi.md#get_org_limits) | **GET** /backend/rest/partner/organizations/{orgId}/limits | getOrgLimits
*PartnerSignUpCodesControllerApi* | [**create_code**](docs/PartnerSignUpCodesControllerApi.md#create_code) | **POST** /backend/rest/distributor/codes | createCode
*PartnerSignUpCodesControllerApi* | [**create_code1**](docs/PartnerSignUpCodesControllerApi.md#create_code1) | **POST** /backend/rest/partner/codes | createCode
*PartnerSignUpCodesControllerApi* | [**delete_code**](docs/PartnerSignUpCodesControllerApi.md#delete_code) | **DELETE** /backend/rest/distributor/codes/{code} | deleteCode
*PartnerSignUpCodesControllerApi* | [**delete_code1**](docs/PartnerSignUpCodesControllerApi.md#delete_code1) | **DELETE** /backend/rest/partner/codes/{code} | deleteCode
*PartnerSignUpCodesControllerApi* | [**get_all1**](docs/PartnerSignUpCodesControllerApi.md#get_all1) | **GET** /backend/rest/distributor/codes | getAll
*PartnerSignUpCodesControllerApi* | [**get_all2**](docs/PartnerSignUpCodesControllerApi.md#get_all2) | **GET** /backend/rest/partner/codes | getAll
*PartnerUsersControllerApi* | [**change_user_state**](docs/PartnerUsersControllerApi.md#change_user_state) | **PUT** /backend/rest/distributor/users/{userId}/state | Change user state
*PartnerUsersControllerApi* | [**change_user_state1**](docs/PartnerUsersControllerApi.md#change_user_state1) | **PUT** /backend/rest/partner/users/{userId}/state | Change user state
*PartnerUsersControllerApi* | [**change_user_state_by_external_id**](docs/PartnerUsersControllerApi.md#change_user_state_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId}/state | Change user state by external ID
*PartnerUsersControllerApi* | [**change_user_state_by_external_id1**](docs/PartnerUsersControllerApi.md#change_user_state_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId}/state | Change user state by external ID
*PartnerUsersControllerApi* | [**change_user_state_by_username**](docs/PartnerUsersControllerApi.md#change_user_state_by_username) | **PUT** /backend/rest/distributor/users/username/{username}/state | Change user state by username
*PartnerUsersControllerApi* | [**change_user_state_by_username1**](docs/PartnerUsersControllerApi.md#change_user_state_by_username1) | **PUT** /backend/rest/partner/users/username/{username}/state | Change user state by username
*PartnerUsersControllerApi* | [**create**](docs/PartnerUsersControllerApi.md#create) | **POST** /backend/rest/distributor/users | Create a user
*PartnerUsersControllerApi* | [**create1**](docs/PartnerUsersControllerApi.md#create1) | **POST** /backend/rest/partner/users | Create a user
*PartnerUsersControllerApi* | [**create_password_reset_token**](docs/PartnerUsersControllerApi.md#create_password_reset_token) | **POST** /backend/rest/distributor/users/{userId}/actions/create-password-reset-token | Create password reset token
*PartnerUsersControllerApi* | [**create_password_reset_token1**](docs/PartnerUsersControllerApi.md#create_password_reset_token1) | **POST** /backend/rest/partner/users/{userId}/actions/create-password-reset-token | Create password reset token
*PartnerUsersControllerApi* | [**create_password_reset_token_by_external_id**](docs/PartnerUsersControllerApi.md#create_password_reset_token_by_external_id) | **POST** /backend/rest/distributor/users/external/{externalId}/actions/create-password-reset-token | Create password reset token by external ID
*PartnerUsersControllerApi* | [**create_password_reset_token_by_external_id1**](docs/PartnerUsersControllerApi.md#create_password_reset_token_by_external_id1) | **POST** /backend/rest/partner/users/external/{externalId}/actions/create-password-reset-token | Create password reset token by external ID
*PartnerUsersControllerApi* | [**create_password_reset_token_by_username**](docs/PartnerUsersControllerApi.md#create_password_reset_token_by_username) | **POST** /backend/rest/distributor/users/username/{username}/actions/create-password-reset-token | Create password reset token by username
*PartnerUsersControllerApi* | [**create_password_reset_token_by_username1**](docs/PartnerUsersControllerApi.md#create_password_reset_token_by_username1) | **POST** /backend/rest/partner/users/username/{username}/actions/create-password-reset-token | Create password reset token by username
*PartnerUsersControllerApi* | [**delete_user**](docs/PartnerUsersControllerApi.md#delete_user) | **DELETE** /backend/rest/distributor/users/{userId} | Delete user
*PartnerUsersControllerApi* | [**delete_user1**](docs/PartnerUsersControllerApi.md#delete_user1) | **DELETE** /backend/rest/partner/users/{userId} | Delete user
*PartnerUsersControllerApi* | [**delete_user_by_external_id**](docs/PartnerUsersControllerApi.md#delete_user_by_external_id) | **DELETE** /backend/rest/distributor/users/external/{externalId} | Delete user by external ID
*PartnerUsersControllerApi* | [**delete_user_by_external_id1**](docs/PartnerUsersControllerApi.md#delete_user_by_external_id1) | **DELETE** /backend/rest/partner/users/external/{externalId} | Delete user by external ID
*PartnerUsersControllerApi* | [**delete_user_by_username**](docs/PartnerUsersControllerApi.md#delete_user_by_username) | **DELETE** /backend/rest/distributor/users/username/{username} | Delete user by username
*PartnerUsersControllerApi* | [**delete_user_by_username1**](docs/PartnerUsersControllerApi.md#delete_user_by_username1) | **DELETE** /backend/rest/partner/users/username/{username} | Delete user by username
*PartnerUsersControllerApi* | [**generate_token**](docs/PartnerUsersControllerApi.md#generate_token) | **POST** /backend/rest/distributor/users/{userId}/tokens | Create token
*PartnerUsersControllerApi* | [**generate_token1**](docs/PartnerUsersControllerApi.md#generate_token1) | **POST** /backend/rest/partner/users/{userId}/tokens | Create token
*PartnerUsersControllerApi* | [**generate_token_by_external_id**](docs/PartnerUsersControllerApi.md#generate_token_by_external_id) | **POST** /backend/rest/distributor/users/external/{externalId}/tokens | Create token by external ID
*PartnerUsersControllerApi* | [**generate_token_by_external_id1**](docs/PartnerUsersControllerApi.md#generate_token_by_external_id1) | **POST** /backend/rest/partner/users/external/{externalId}/tokens | Create token by external ID
*PartnerUsersControllerApi* | [**generate_token_by_username**](docs/PartnerUsersControllerApi.md#generate_token_by_username) | **POST** /backend/rest/distributor/users/username/{username}/tokens | Create token by username
*PartnerUsersControllerApi* | [**generate_token_by_username1**](docs/PartnerUsersControllerApi.md#generate_token_by_username1) | **POST** /backend/rest/partner/users/username/{username}/tokens | Create token by username
*PartnerUsersControllerApi* | [**get_all_users_pageable**](docs/PartnerUsersControllerApi.md#get_all_users_pageable) | **GET** /backend/rest/distributor/users/search | Get users with search, sorting and pagination
*PartnerUsersControllerApi* | [**get_all_users_pageable1**](docs/PartnerUsersControllerApi.md#get_all_users_pageable1) | **GET** /backend/rest/partner/users/search | Get users with search, sorting and pagination
*PartnerUsersControllerApi* | [**get_user**](docs/PartnerUsersControllerApi.md#get_user) | **GET** /backend/rest/distributor/users/{userId} | Get user details
*PartnerUsersControllerApi* | [**get_user1**](docs/PartnerUsersControllerApi.md#get_user1) | **GET** /backend/rest/partner/users/{userId} | Get user details
*PartnerUsersControllerApi* | [**get_user_by_external_id**](docs/PartnerUsersControllerApi.md#get_user_by_external_id) | **GET** /backend/rest/distributor/users/external/{externalId} | Get user details by external ID
*PartnerUsersControllerApi* | [**get_user_by_external_id1**](docs/PartnerUsersControllerApi.md#get_user_by_external_id1) | **GET** /backend/rest/partner/users/external/{externalId} | Get user details by external ID
*PartnerUsersControllerApi* | [**get_user_by_username**](docs/PartnerUsersControllerApi.md#get_user_by_username) | **GET** /backend/rest/distributor/users/username/{username} | Get user details by username
*PartnerUsersControllerApi* | [**get_user_by_username1**](docs/PartnerUsersControllerApi.md#get_user_by_username1) | **GET** /backend/rest/partner/users/username/{username} | Get user details by username
*PartnerUsersControllerApi* | [**get_users**](docs/PartnerUsersControllerApi.md#get_users) | **GET** /backend/rest/distributor/users | Get all users
*PartnerUsersControllerApi* | [**get_users1**](docs/PartnerUsersControllerApi.md#get_users1) | **GET** /backend/rest/partner/users | Get all users
*PartnerUsersControllerApi* | [**send_password_reset_email**](docs/PartnerUsersControllerApi.md#send_password_reset_email) | **POST** /backend/rest/distributor/users/{userId}/actions/send-password-reset-email | Set/reset password
*PartnerUsersControllerApi* | [**send_password_reset_email1**](docs/PartnerUsersControllerApi.md#send_password_reset_email1) | **POST** /backend/rest/partner/users/{userId}/actions/send-password-reset-email | Set/reset password
*PartnerUsersControllerApi* | [**send_password_reset_email_by_external_id**](docs/PartnerUsersControllerApi.md#send_password_reset_email_by_external_id) | **POST** /backend/rest/distributor/users/external/{externalId}/actions/send-password-reset-email | Set/reset password by external ID
*PartnerUsersControllerApi* | [**send_password_reset_email_by_external_id1**](docs/PartnerUsersControllerApi.md#send_password_reset_email_by_external_id1) | **POST** /backend/rest/partner/users/external/{externalId}/actions/send-password-reset-email | Set/reset password by external ID
*PartnerUsersControllerApi* | [**send_password_reset_email_by_username**](docs/PartnerUsersControllerApi.md#send_password_reset_email_by_username) | **POST** /backend/rest/distributor/users/username/{username}/actions/send-password-reset-email | Set/reset password by username
*PartnerUsersControllerApi* | [**send_password_reset_email_by_username1**](docs/PartnerUsersControllerApi.md#send_password_reset_email_by_username1) | **POST** /backend/rest/partner/users/username/{username}/actions/send-password-reset-email | Set/reset password by username
*PartnerUsersControllerApi* | [**set_limits**](docs/PartnerUsersControllerApi.md#set_limits) | **PUT** /backend/rest/distributor/users/{userId}/limits | Set custom user limits by partner
*PartnerUsersControllerApi* | [**set_limits1**](docs/PartnerUsersControllerApi.md#set_limits1) | **PUT** /backend/rest/partner/users/{userId}/limits | Set custom user limits by partner
*PartnerUsersControllerApi* | [**set_limits_by_external_id**](docs/PartnerUsersControllerApi.md#set_limits_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId}/limits | setLimitsByExternalId
*PartnerUsersControllerApi* | [**set_limits_by_external_id1**](docs/PartnerUsersControllerApi.md#set_limits_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId}/limits | setLimitsByExternalId
*PartnerUsersControllerApi* | [**set_limits_by_username**](docs/PartnerUsersControllerApi.md#set_limits_by_username) | **PUT** /backend/rest/distributor/users/username/{username}/limits | setLimitsByUsername
*PartnerUsersControllerApi* | [**set_limits_by_username1**](docs/PartnerUsersControllerApi.md#set_limits_by_username1) | **PUT** /backend/rest/partner/users/username/{username}/limits | setLimitsByUsername
*PartnerUsersControllerApi* | [**set_roles**](docs/PartnerUsersControllerApi.md#set_roles) | **PUT** /backend/rest/distributor/users/{userId}/roles | setRoles
*PartnerUsersControllerApi* | [**set_roles1**](docs/PartnerUsersControllerApi.md#set_roles1) | **PUT** /backend/rest/partner/users/{userId}/roles | setRoles
*PartnerUsersControllerApi* | [**set_roles_by_external_id**](docs/PartnerUsersControllerApi.md#set_roles_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId}/roles | setRolesByExternalId
*PartnerUsersControllerApi* | [**set_roles_by_external_id1**](docs/PartnerUsersControllerApi.md#set_roles_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId}/roles | setRolesByExternalId
*PartnerUsersControllerApi* | [**set_roles_by_username**](docs/PartnerUsersControllerApi.md#set_roles_by_username) | **PUT** /backend/rest/distributor/users/username/{username}/roles | setRolesByUsername
*PartnerUsersControllerApi* | [**set_roles_by_username1**](docs/PartnerUsersControllerApi.md#set_roles_by_username1) | **PUT** /backend/rest/partner/users/username/{username}/roles | setRolesByUsername
*PartnerUsersControllerApi* | [**update_user**](docs/PartnerUsersControllerApi.md#update_user) | **PUT** /backend/rest/distributor/users/{userId} | Update profile
*PartnerUsersControllerApi* | [**update_user1**](docs/PartnerUsersControllerApi.md#update_user1) | **PUT** /backend/rest/partner/users/{userId} | Update profile
*PartnerUsersControllerApi* | [**update_user_by_external_id**](docs/PartnerUsersControllerApi.md#update_user_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId} | Update profile by external ID
*PartnerUsersControllerApi* | [**update_user_by_external_id1**](docs/PartnerUsersControllerApi.md#update_user_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId} | Update profile by external ID
*PartnerUsersControllerApi* | [**update_user_by_username**](docs/PartnerUsersControllerApi.md#update_user_by_username) | **PUT** /backend/rest/distributor/users/username/{username} | Update profile by username
*PartnerUsersControllerApi* | [**update_user_by_username1**](docs/PartnerUsersControllerApi.md#update_user_by_username1) | **PUT** /backend/rest/partner/users/username/{username} | Update profile by username
*PaymentsControllerApi* | [**get_payment_options**](docs/PaymentsControllerApi.md#get_payment_options) | **GET** /backend/rest/pay/paddle/options | getPaymentOptions
*PaymentsControllerApi* | [**payment_fulfilled**](docs/PaymentsControllerApi.md#payment_fulfilled) | **GET** /backend/rest/pay/paddle/webhook | paymentFulfilled
*ProvidersControllerApi* | [**get_providers**](docs/ProvidersControllerApi.md#get_providers) | **GET** /backend/rest/providers | Get all storage providers
*StorageAccountsControllerApi* | [**add_storage_account**](docs/StorageAccountsControllerApi.md#add_storage_account) | **POST** /backend/rest/storage-accounts | Add Storage Account with an optional list of buckets
*StorageAccountsControllerApi* | [**add_storage_accounts_with_azure_integration**](docs/StorageAccountsControllerApi.md#add_storage_accounts_with_azure_integration) | **POST** /backend/rest/storage-accounts/azure-integration | Add multiple storage accounts with Azure integration
*StorageAccountsControllerApi* | [**delete_storage_account**](docs/StorageAccountsControllerApi.md#delete_storage_account) | **DELETE** /backend/rest/storage-accounts/{storage-account-id} | Deletes (hides) storage account and all its buckets/containers
*StorageAccountsControllerApi* | [**get_storage_account**](docs/StorageAccountsControllerApi.md#get_storage_account) | **GET** /backend/rest/storage-accounts/{storage-account-id} | Get storage account by id
*StorageAccountsControllerApi* | [**get_storage_accounts**](docs/StorageAccountsControllerApi.md#get_storage_accounts) | **GET** /backend/rest/storage-accounts | Get all storage accounts for current user
*StorageAccountsControllerApi* | [**reauth_storage_account**](docs/StorageAccountsControllerApi.md#reauth_storage_account) | **POST** /backend/rest/storage-accounts/{storage-account-id}/reauth | Reauthenticate storage account
*StorageAccountsControllerApi* | [**refresh_storage_account**](docs/StorageAccountsControllerApi.md#refresh_storage_account) | **POST** /backend/rest/storage-accounts/{storage-account-id}/actions/refresh | Requests and updates list of buckets/containers for the storage account
*StorageAccountsControllerApi* | [**set_storage_account_settings**](docs/StorageAccountsControllerApi.md#set_storage_account_settings) | **PUT** /backend/rest/storage-accounts/{storage-account-id}/settings | Updates storage account settings
*StorageAccountsOAuthControllerApi* | [**get_config2**](docs/StorageAccountsOAuthControllerApi.md#get_config2) | **GET** /backend/rest/storage-accounts/oauth/config | getConfig
*StorageAccountsOAuthControllerApi* | [**get_device_code1**](docs/StorageAccountsOAuthControllerApi.md#get_device_code1) | **GET** /backend/rest/storage-accounts/oauth/device-code | getDeviceCode
*StoragesControllerApi* | [**add_buckets**](docs/StoragesControllerApi.md#add_buckets) | **POST** /backend/rest/storage-accounts/{storage-account-id}/buckets | Add buckets to the storage account
*StoragesControllerApi* | [**delete_bucket**](docs/StoragesControllerApi.md#delete_bucket) | **DELETE** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Deletes (hides) a bucket/container
*StoragesControllerApi* | [**get_bucket**](docs/StoragesControllerApi.md#get_bucket) | **GET** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Get detailed stats for the bucket
*StoragesControllerApi* | [**refresh_bucket**](docs/StoragesControllerApi.md#refresh_bucket) | **POST** /backend/rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}/actions/refresh | Refresh statistics of a single bucket
*UserControllerApi* | [**change_microsoft_sso**](docs/UserControllerApi.md#change_microsoft_sso) | **POST** /backend/rest/user/current/sso-microsoft | changeMicrosoftSso
*UserControllerApi* | [**get_current_user**](docs/UserControllerApi.md#get_current_user) | **GET** /backend/rest/user/current | Get details of user corresponding to provided auth token
*UserControllerApi* | [**request_delete**](docs/UserControllerApi.md#request_delete) | **POST** /backend/rest/user/request-delete | requestDelete
*UserControllerApi* | [**request_reset_password**](docs/UserControllerApi.md#request_reset_password) | **POST** /backend/rest/user/request-reset-password | requestResetPassword


## Documentation For Models

 - [AccessKeysPair](docs/AccessKeysPair.md)
 - [AddBucketsRequest](docs/AddBucketsRequest.md)
 - [AddImpersonateCodeRequest](docs/AddImpersonateCodeRequest.md)
 - [AddImpersonateFromUserRequest](docs/AddImpersonateFromUserRequest.md)
 - [AddMigrationRequest](docs/AddMigrationRequest.md)
 - [AddMigrationRequestMapping](docs/AddMigrationRequestMapping.md)
 - [AddStorageAccountRequest](docs/AddStorageAccountRequest.md)
 - [AddStorageAccountsWithAzureLinkRequest](docs/AddStorageAccountsWithAzureLinkRequest.md)
 - [AuthCheckTokenAndGetUserResponse](docs/AuthCheckTokenAndGetUserResponse.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [AzureIntegration](docs/AzureIntegration.md)
 - [AzureStorageAccountInfo](docs/AzureStorageAccountInfo.md)
 - [AzureSubscriptionInfoWithStorages](docs/AzureSubscriptionInfoWithStorages.md)
 - [BillingAccount](docs/BillingAccount.md)
 - [Bucket](docs/Bucket.md)
 - [BucketStat](docs/BucketStat.md)
 - [ChangePasswordRequest](docs/ChangePasswordRequest.md)
 - [ChangeSsoMicrosoftRequest](docs/ChangeSsoMicrosoftRequest.md)
 - [CleanupStat](docs/CleanupStat.md)
 - [CloudLocation](docs/CloudLocation.md)
 - [CloudLocationReq](docs/CloudLocationReq.md)
 - [CloudLocationRes](docs/CloudLocationRes.md)
 - [CostDetails](docs/CostDetails.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateVirtualBucketRequest](docs/CreateVirtualBucketRequest.md)
 - [Distributor](docs/Distributor.md)
 - [DtoMappingCostEstimate](docs/DtoMappingCostEstimate.md)
 - [DtoMappingCostEstimateEntry](docs/DtoMappingCostEstimateEntry.md)
 - [DtoMigrationCostEstimate](docs/DtoMigrationCostEstimate.md)
 - [EndpointDetails](docs/EndpointDetails.md)
 - [EndpointSecretResponse](docs/EndpointSecretResponse.md)
 - [EndpointSettingsReq](docs/EndpointSettingsReq.md)
 - [EndpointSettingsRes](docs/EndpointSettingsRes.md)
 - [EndpointStat](docs/EndpointStat.md)
 - [EndpointStorageAccount](docs/EndpointStorageAccount.md)
 - [EndpointStorageAccountSettings](docs/EndpointStorageAccountSettings.md)
 - [FinishOAuthParams](docs/FinishOAuthParams.md)
 - [IdResponse](docs/IdResponse.md)
 - [IdsList](docs/IdsList.md)
 - [ImpersonateUser](docs/ImpersonateUser.md)
 - [InformationAboutAuthenticationToken](docs/InformationAboutAuthenticationToken.md)
 - [LogEntry](docs/LogEntry.md)
 - [LogEvent](docs/LogEvent.md)
 - [LogoutRequest](docs/LogoutRequest.md)
 - [Mapping](docs/Mapping.md)
 - [MappingStat](docs/MappingStat.md)
 - [MarkerPageLogEntry](docs/MarkerPageLogEntry.md)
 - [MicrosoftOAuthConfig](docs/MicrosoftOAuthConfig.md)
 - [Migration](docs/Migration.md)
 - [MigrationSettings](docs/MigrationSettings.md)
 - [MigrationSettingsReq](docs/MigrationSettingsReq.md)
 - [MigrationSettingsRes](docs/MigrationSettingsRes.md)
 - [MigrationStat](docs/MigrationStat.md)
 - [Money](docs/Money.md)
 - [NewStorageAccount](docs/NewStorageAccount.md)
 - [OAuth2DeviceCodeResponse](docs/OAuth2DeviceCodeResponse.md)
 - [OAuthToken](docs/OAuthToken.md)
 - [Organization](docs/Organization.md)
 - [PageMigration](docs/PageMigration.md)
 - [PageUserStat](docs/PageUserStat.md)
 - [Pageable](docs/Pageable.md)
 - [PasswordResetToken](docs/PasswordResetToken.md)
 - [Payment](docs/Payment.md)
 - [PaymentOptions](docs/PaymentOptions.md)
 - [PolicyRule](docs/PolicyRule.md)
 - [Price](docs/Price.md)
 - [PriceConstraints](docs/PriceConstraints.md)
 - [PriceList](docs/PriceList.md)
 - [PublicAuthenticationConfiguration](docs/PublicAuthenticationConfiguration.md)
 - [PublicManagementServerConfiguration](docs/PublicManagementServerConfiguration.md)
 - [RefreshTokenRequest](docs/RefreshTokenRequest.md)
 - [RequestResetPasswordRequest](docs/RequestResetPasswordRequest.md)
 - [ResetPasswordRequest](docs/ResetPasswordRequest.md)
 - [ResetSsoRequest](docs/ResetSsoRequest.md)
 - [SetLimitsRequest](docs/SetLimitsRequest.md)
 - [SetRolesRequest](docs/SetRolesRequest.md)
 - [SetUserStateRequest](docs/SetUserStateRequest.md)
 - [SignUpRequest](docs/SignUpRequest.md)
 - [SignupCodeReq](docs/SignupCodeReq.md)
 - [SignupCodeRes](docs/SignupCodeRes.md)
 - [SignupCodeStat](docs/SignupCodeStat.md)
 - [SignupResult](docs/SignupResult.md)
 - [Slot](docs/Slot.md)
 - [SlotStat](docs/SlotStat.md)
 - [Sort](docs/Sort.md)
 - [StorageAccount](docs/StorageAccount.md)
 - [StorageAccountSettings](docs/StorageAccountSettings.md)
 - [StorageAccountSettingsReq](docs/StorageAccountSettingsReq.md)
 - [StorageAccountSettingsRes](docs/StorageAccountSettingsRes.md)
 - [StorageAccountStat](docs/StorageAccountStat.md)
 - [StorageAccountWithBuckets](docs/StorageAccountWithBuckets.md)
 - [StorageAccountsRequest](docs/StorageAccountsRequest.md)
 - [StorageProvider](docs/StorageProvider.md)
 - [TokenByDeviceCodeRequest](docs/TokenByDeviceCodeRequest.md)
 - [TokenConfiguration](docs/TokenConfiguration.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [User](docs/User.md)
 - [UserConfig](docs/UserConfig.md)
 - [UserProfile](docs/UserProfile.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserStat](docs/UserStat.md)
 - [VirtualBucket](docs/VirtualBucket.md)
 - [VirtualBucketAccessPolicy](docs/VirtualBucketAccessPolicy.md)
 - [VirtualBucketSettings](docs/VirtualBucketSettings.md)
 - [VirtualBucketStorage](docs/VirtualBucketStorage.md)
 - [VirtualBucketStorageSettings](docs/VirtualBucketStorageSettings.md)
 - [VirtualBucketStoragesRequest](docs/VirtualBucketStoragesRequest.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Contact us:

+ Information: [info@flexify.io](mailto:info@flexify.io)
+ Sales: [sales@flexify.io](mailto:sales@flexify.io)
+ Support: [support@flexify.io](mailto:support@flexify.io)

