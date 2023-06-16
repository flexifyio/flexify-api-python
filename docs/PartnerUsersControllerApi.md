# flexify_api.PartnerUsersControllerApi

All URIs are relative to *https://api.flexify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_state**](PartnerUsersControllerApi.md#change_user_state) | **PUT** /backend/rest/distributor/users/{userId}/state | Change user state
[**change_user_state1**](PartnerUsersControllerApi.md#change_user_state1) | **PUT** /backend/rest/partner/users/{userId}/state | Change user state
[**change_user_state_by_external_id**](PartnerUsersControllerApi.md#change_user_state_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId}/state | Change user state by external ID
[**change_user_state_by_external_id1**](PartnerUsersControllerApi.md#change_user_state_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId}/state | Change user state by external ID
[**change_user_state_by_username**](PartnerUsersControllerApi.md#change_user_state_by_username) | **PUT** /backend/rest/distributor/users/username/{username}/state | Change user state by username
[**change_user_state_by_username1**](PartnerUsersControllerApi.md#change_user_state_by_username1) | **PUT** /backend/rest/partner/users/username/{username}/state | Change user state by username
[**create**](PartnerUsersControllerApi.md#create) | **POST** /backend/rest/distributor/users | Create a user
[**create1**](PartnerUsersControllerApi.md#create1) | **POST** /backend/rest/partner/users | Create a user
[**create_password_reset_token**](PartnerUsersControllerApi.md#create_password_reset_token) | **POST** /backend/rest/distributor/users/{userId}/actions/create-password-reset-token | Create password reset token
[**create_password_reset_token1**](PartnerUsersControllerApi.md#create_password_reset_token1) | **POST** /backend/rest/partner/users/{userId}/actions/create-password-reset-token | Create password reset token
[**create_password_reset_token_by_external_id**](PartnerUsersControllerApi.md#create_password_reset_token_by_external_id) | **POST** /backend/rest/distributor/users/external/{externalId}/actions/create-password-reset-token | Create password reset token by external ID
[**create_password_reset_token_by_external_id1**](PartnerUsersControllerApi.md#create_password_reset_token_by_external_id1) | **POST** /backend/rest/partner/users/external/{externalId}/actions/create-password-reset-token | Create password reset token by external ID
[**create_password_reset_token_by_username**](PartnerUsersControllerApi.md#create_password_reset_token_by_username) | **POST** /backend/rest/distributor/users/username/{username}/actions/create-password-reset-token | Create password reset token by username
[**create_password_reset_token_by_username1**](PartnerUsersControllerApi.md#create_password_reset_token_by_username1) | **POST** /backend/rest/partner/users/username/{username}/actions/create-password-reset-token | Create password reset token by username
[**delete_user**](PartnerUsersControllerApi.md#delete_user) | **DELETE** /backend/rest/distributor/users/{userId} | Delete user
[**delete_user1**](PartnerUsersControllerApi.md#delete_user1) | **DELETE** /backend/rest/partner/users/{userId} | Delete user
[**delete_user_by_external_id**](PartnerUsersControllerApi.md#delete_user_by_external_id) | **DELETE** /backend/rest/distributor/users/external/{externalId} | Delete user by external ID
[**delete_user_by_external_id1**](PartnerUsersControllerApi.md#delete_user_by_external_id1) | **DELETE** /backend/rest/partner/users/external/{externalId} | Delete user by external ID
[**delete_user_by_username**](PartnerUsersControllerApi.md#delete_user_by_username) | **DELETE** /backend/rest/distributor/users/username/{username} | Delete user by username
[**delete_user_by_username1**](PartnerUsersControllerApi.md#delete_user_by_username1) | **DELETE** /backend/rest/partner/users/username/{username} | Delete user by username
[**generate_token**](PartnerUsersControllerApi.md#generate_token) | **POST** /backend/rest/distributor/users/{userId}/tokens | Create token
[**generate_token1**](PartnerUsersControllerApi.md#generate_token1) | **POST** /backend/rest/partner/users/{userId}/tokens | Create token
[**generate_token_by_external_id**](PartnerUsersControllerApi.md#generate_token_by_external_id) | **POST** /backend/rest/distributor/users/external/{externalId}/tokens | Create token by external ID
[**generate_token_by_external_id1**](PartnerUsersControllerApi.md#generate_token_by_external_id1) | **POST** /backend/rest/partner/users/external/{externalId}/tokens | Create token by external ID
[**generate_token_by_username**](PartnerUsersControllerApi.md#generate_token_by_username) | **POST** /backend/rest/distributor/users/username/{username}/tokens | Create token by username
[**generate_token_by_username1**](PartnerUsersControllerApi.md#generate_token_by_username1) | **POST** /backend/rest/partner/users/username/{username}/tokens | Create token by username
[**get_all_users_pageable**](PartnerUsersControllerApi.md#get_all_users_pageable) | **GET** /backend/rest/distributor/users/search | Get users with search, sorting and pagination
[**get_all_users_pageable1**](PartnerUsersControllerApi.md#get_all_users_pageable1) | **GET** /backend/rest/partner/users/search | Get users with search, sorting and pagination
[**get_user**](PartnerUsersControllerApi.md#get_user) | **GET** /backend/rest/distributor/users/{userId} | Get user details
[**get_user1**](PartnerUsersControllerApi.md#get_user1) | **GET** /backend/rest/partner/users/{userId} | Get user details
[**get_user_by_external_id**](PartnerUsersControllerApi.md#get_user_by_external_id) | **GET** /backend/rest/distributor/users/external/{externalId} | Get user details by external ID
[**get_user_by_external_id1**](PartnerUsersControllerApi.md#get_user_by_external_id1) | **GET** /backend/rest/partner/users/external/{externalId} | Get user details by external ID
[**get_user_by_username**](PartnerUsersControllerApi.md#get_user_by_username) | **GET** /backend/rest/distributor/users/username/{username} | Get user details by username
[**get_user_by_username1**](PartnerUsersControllerApi.md#get_user_by_username1) | **GET** /backend/rest/partner/users/username/{username} | Get user details by username
[**get_users**](PartnerUsersControllerApi.md#get_users) | **GET** /backend/rest/distributor/users | Get all users
[**get_users1**](PartnerUsersControllerApi.md#get_users1) | **GET** /backend/rest/partner/users | Get all users
[**send_password_reset_email**](PartnerUsersControllerApi.md#send_password_reset_email) | **POST** /backend/rest/distributor/users/{userId}/actions/send-password-reset-email | Set/reset password
[**send_password_reset_email1**](PartnerUsersControllerApi.md#send_password_reset_email1) | **POST** /backend/rest/partner/users/{userId}/actions/send-password-reset-email | Set/reset password
[**send_password_reset_email_by_external_id**](PartnerUsersControllerApi.md#send_password_reset_email_by_external_id) | **POST** /backend/rest/distributor/users/external/{externalId}/actions/send-password-reset-email | Set/reset password by external ID
[**send_password_reset_email_by_external_id1**](PartnerUsersControllerApi.md#send_password_reset_email_by_external_id1) | **POST** /backend/rest/partner/users/external/{externalId}/actions/send-password-reset-email | Set/reset password by external ID
[**send_password_reset_email_by_username**](PartnerUsersControllerApi.md#send_password_reset_email_by_username) | **POST** /backend/rest/distributor/users/username/{username}/actions/send-password-reset-email | Set/reset password by username
[**send_password_reset_email_by_username1**](PartnerUsersControllerApi.md#send_password_reset_email_by_username1) | **POST** /backend/rest/partner/users/username/{username}/actions/send-password-reset-email | Set/reset password by username
[**set_roles**](PartnerUsersControllerApi.md#set_roles) | **PUT** /backend/rest/distributor/users/{userId}/roles | setRoles
[**set_roles1**](PartnerUsersControllerApi.md#set_roles1) | **PUT** /backend/rest/partner/users/{userId}/roles | setRoles
[**set_roles_by_external_id**](PartnerUsersControllerApi.md#set_roles_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId}/roles | setRolesByExternalId
[**set_roles_by_external_id1**](PartnerUsersControllerApi.md#set_roles_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId}/roles | setRolesByExternalId
[**set_roles_by_username**](PartnerUsersControllerApi.md#set_roles_by_username) | **PUT** /backend/rest/distributor/users/username/{username}/roles | setRolesByUsername
[**set_roles_by_username1**](PartnerUsersControllerApi.md#set_roles_by_username1) | **PUT** /backend/rest/partner/users/username/{username}/roles | setRolesByUsername
[**update_user**](PartnerUsersControllerApi.md#update_user) | **PUT** /backend/rest/distributor/users/{userId} | Update profile
[**update_user1**](PartnerUsersControllerApi.md#update_user1) | **PUT** /backend/rest/partner/users/{userId} | Update profile
[**update_user_by_external_id**](PartnerUsersControllerApi.md#update_user_by_external_id) | **PUT** /backend/rest/distributor/users/external/{externalId} | Update profile by external ID
[**update_user_by_external_id1**](PartnerUsersControllerApi.md#update_user_by_external_id1) | **PUT** /backend/rest/partner/users/external/{externalId} | Update profile by external ID
[**update_user_by_username**](PartnerUsersControllerApi.md#update_user_by_username) | **PUT** /backend/rest/distributor/users/username/{username} | Update profile by username
[**update_user_by_username1**](PartnerUsersControllerApi.md#update_user_by_username1) | **PUT** /backend/rest/partner/users/username/{username} | Update profile by username


# **change_user_state**
> change_user_state(request, user_id)

Change user state

Enables or disables a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetUserStateRequest() # SetUserStateRequest | request
user_id = 789 # int | userId

try:
    # Change user state
    api_instance.change_user_state(request, user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->change_user_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetUserStateRequest**](SetUserStateRequest.md)| request | 
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_state1**
> change_user_state1(request, user_id)

Change user state

Enables or disables a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetUserStateRequest() # SetUserStateRequest | request
user_id = 789 # int | userId

try:
    # Change user state
    api_instance.change_user_state1(request, user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->change_user_state1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetUserStateRequest**](SetUserStateRequest.md)| request | 
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_state_by_external_id**
> change_user_state_by_external_id(external_id, request)

Change user state by external ID

Enables or disables a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.SetUserStateRequest() # SetUserStateRequest | request

try:
    # Change user state by external ID
    api_instance.change_user_state_by_external_id(external_id, request)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->change_user_state_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**SetUserStateRequest**](SetUserStateRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_state_by_external_id1**
> change_user_state_by_external_id1(external_id, request)

Change user state by external ID

Enables or disables a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.SetUserStateRequest() # SetUserStateRequest | request

try:
    # Change user state by external ID
    api_instance.change_user_state_by_external_id1(external_id, request)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->change_user_state_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**SetUserStateRequest**](SetUserStateRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_state_by_username**
> change_user_state_by_username(request, username)

Change user state by username

Enables or disables a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetUserStateRequest() # SetUserStateRequest | request
username = 'username_example' # str | username

try:
    # Change user state by username
    api_instance.change_user_state_by_username(request, username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->change_user_state_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetUserStateRequest**](SetUserStateRequest.md)| request | 
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_state_by_username1**
> change_user_state_by_username1(request, username)

Change user state by username

Enables or disables a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetUserStateRequest() # SetUserStateRequest | request
username = 'username_example' # str | username

try:
    # Change user state by username
    api_instance.change_user_state_by_username1(request, username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->change_user_state_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetUserStateRequest**](SetUserStateRequest.md)| request | 
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> IdResponse create(request)

Create a user

Creates a new user associated with this distributor

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.CreateUserRequest() # CreateUserRequest | Profile and optional external ID of a user to be created

try:
    # Create a user
    api_response = api_instance.create(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateUserRequest**](CreateUserRequest.md)| Profile and optional external ID of a user to be created | 

### Return type

[**IdResponse**](IdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create1**
> IdResponse create1(request)

Create a user

Creates a new user associated with this distributor

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.CreateUserRequest() # CreateUserRequest | Profile and optional external ID of a user to be created

try:
    # Create a user
    api_response = api_instance.create1(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateUserRequest**](CreateUserRequest.md)| Profile and optional external ID of a user to be created | 

### Return type

[**IdResponse**](IdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset_token**
> PasswordResetToken create_password_reset_token(user_id)

Create password reset token

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Create password reset token
    api_response = api_instance.create_password_reset_token(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create_password_reset_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

[**PasswordResetToken**](PasswordResetToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset_token1**
> PasswordResetToken create_password_reset_token1(user_id)

Create password reset token

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Create password reset token
    api_response = api_instance.create_password_reset_token1(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create_password_reset_token1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

[**PasswordResetToken**](PasswordResetToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset_token_by_external_id**
> PasswordResetToken create_password_reset_token_by_external_id(external_id)

Create password reset token by external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Create password reset token by external ID
    api_response = api_instance.create_password_reset_token_by_external_id(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create_password_reset_token_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**PasswordResetToken**](PasswordResetToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset_token_by_external_id1**
> PasswordResetToken create_password_reset_token_by_external_id1(external_id)

Create password reset token by external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Create password reset token by external ID
    api_response = api_instance.create_password_reset_token_by_external_id1(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create_password_reset_token_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**PasswordResetToken**](PasswordResetToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset_token_by_username**
> PasswordResetToken create_password_reset_token_by_username(username)

Create password reset token by username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Create password reset token by username
    api_response = api_instance.create_password_reset_token_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create_password_reset_token_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

[**PasswordResetToken**](PasswordResetToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset_token_by_username1**
> PasswordResetToken create_password_reset_token_by_username1(username)

Create password reset token by username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Create password reset token by username
    api_response = api_instance.create_password_reset_token_by_username1(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->create_password_reset_token_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

[**PasswordResetToken**](PasswordResetToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete user

Deletes (marks as deleted) a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Delete user
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user1**
> delete_user1(user_id)

Delete user

Deletes (marks as deleted) a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Delete user
    api_instance.delete_user1(user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->delete_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_external_id**
> delete_user_by_external_id(external_id)

Delete user by external ID

Deletes (marks as deleted) a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Delete user by external ID
    api_instance.delete_user_by_external_id(external_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->delete_user_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_external_id1**
> delete_user_by_external_id1(external_id)

Delete user by external ID

Deletes (marks as deleted) a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Delete user by external ID
    api_instance.delete_user_by_external_id1(external_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->delete_user_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_username**
> delete_user_by_username(username)

Delete user by username

Deletes (marks as deleted) a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Delete user by username
    api_instance.delete_user_by_username(username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->delete_user_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_username1**
> delete_user_by_username1(username)

Delete user by username

Deletes (marks as deleted) a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Delete user by username
    api_instance.delete_user_by_username1(username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->delete_user_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token**
> InformationAboutAuthenticationToken generate_token(request, user_id)

Create token

Creates new API or integration token for a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.TokenConfiguration() # TokenConfiguration | request
user_id = 789 # int | userId

try:
    # Create token
    api_response = api_instance.generate_token(request, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->generate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TokenConfiguration**](TokenConfiguration.md)| request | 
 **user_id** | **int**| userId | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token1**
> InformationAboutAuthenticationToken generate_token1(request, user_id)

Create token

Creates new API or integration token for a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.TokenConfiguration() # TokenConfiguration | request
user_id = 789 # int | userId

try:
    # Create token
    api_response = api_instance.generate_token1(request, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->generate_token1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TokenConfiguration**](TokenConfiguration.md)| request | 
 **user_id** | **int**| userId | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_by_external_id**
> InformationAboutAuthenticationToken generate_token_by_external_id(external_id, request)

Create token by external ID

Creates new API, impersonation or integration token for a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.TokenConfiguration() # TokenConfiguration | request

try:
    # Create token by external ID
    api_response = api_instance.generate_token_by_external_id(external_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->generate_token_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**TokenConfiguration**](TokenConfiguration.md)| request | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_by_external_id1**
> InformationAboutAuthenticationToken generate_token_by_external_id1(external_id, request)

Create token by external ID

Creates new API, impersonation or integration token for a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.TokenConfiguration() # TokenConfiguration | request

try:
    # Create token by external ID
    api_response = api_instance.generate_token_by_external_id1(external_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->generate_token_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**TokenConfiguration**](TokenConfiguration.md)| request | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_by_username**
> InformationAboutAuthenticationToken generate_token_by_username(request, username)

Create token by username

Creates new API, impersonation or integration token for a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.TokenConfiguration() # TokenConfiguration | request
username = 'username_example' # str | username

try:
    # Create token by username
    api_response = api_instance.generate_token_by_username(request, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->generate_token_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TokenConfiguration**](TokenConfiguration.md)| request | 
 **username** | **str**| username | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_by_username1**
> InformationAboutAuthenticationToken generate_token_by_username1(request, username)

Create token by username

Creates new API, impersonation or integration token for a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.TokenConfiguration() # TokenConfiguration | request
username = 'username_example' # str | username

try:
    # Create token by username
    api_response = api_instance.generate_token_by_username1(request, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->generate_token_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TokenConfiguration**](TokenConfiguration.md)| request | 
 **username** | **str**| username | 

### Return type

[**InformationAboutAuthenticationToken**](InformationAboutAuthenticationToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_pageable**
> PageUserStat get_all_users_pageable(offset, page, paged=paged, page_number=page_number, page_size=page_size, search_string=search_string, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_direction=sort_direction)

Get users with search, sorting and pagination

Gets a list of users managed by this distributor

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
offset = 0 # int | Position of the first migration in the list (or null to start from the beginning)
page = 0 # int | [Deprecated] Page number
paged = true # bool |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
search_string = 'search_string_example' # str | Search string (optional)
size = 100 # int | Max number of entries to return (AKA page size), null means no paging (optional)
sort_sorted = true # bool |  (optional)
sort_unsorted = true # bool |  (optional)
sort_direction = 'ASC' # str | Sort Direction (optional)

try:
    # Get users with search, sorting and pagination
    api_response = api_instance.get_all_users_pageable(offset, page, paged=paged, page_number=page_number, page_size=page_size, search_string=search_string, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_all_users_pageable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Position of the first migration in the list (or null to start from the beginning) | 
 **page** | **int**| [Deprecated] Page number | 
 **paged** | **bool**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **search_string** | **str**| Search string | [optional] 
 **size** | **int**| Max number of entries to return (AKA page size), null means no paging | [optional] 
 **sort_sorted** | **bool**|  | [optional] 
 **sort_unsorted** | **bool**|  | [optional] 
 **sort_direction** | **str**| Sort Direction | [optional] 

### Return type

[**PageUserStat**](PageUserStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_pageable1**
> PageUserStat get_all_users_pageable1(offset, page, paged=paged, page_number=page_number, page_size=page_size, search_string=search_string, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_direction=sort_direction)

Get users with search, sorting and pagination

Gets a list of users managed by this distributor

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
offset = 0 # int | Position of the first migration in the list (or null to start from the beginning)
page = 0 # int | [Deprecated] Page number
paged = true # bool |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
search_string = 'search_string_example' # str | Search string (optional)
size = 100 # int | Max number of entries to return (AKA page size), null means no paging (optional)
sort_sorted = true # bool |  (optional)
sort_unsorted = true # bool |  (optional)
sort_direction = 'ASC' # str | Sort Direction (optional)

try:
    # Get users with search, sorting and pagination
    api_response = api_instance.get_all_users_pageable1(offset, page, paged=paged, page_number=page_number, page_size=page_size, search_string=search_string, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_all_users_pageable1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Position of the first migration in the list (or null to start from the beginning) | 
 **page** | **int**| [Deprecated] Page number | 
 **paged** | **bool**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **search_string** | **str**| Search string | [optional] 
 **size** | **int**| Max number of entries to return (AKA page size), null means no paging | [optional] 
 **sort_sorted** | **bool**|  | [optional] 
 **sort_unsorted** | **bool**|  | [optional] 
 **sort_direction** | **str**| Sort Direction | [optional] 

### Return type

[**PageUserStat**](PageUserStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Get user details

Gets details of a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Get user details
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user1**
> User get_user1(user_id)

Get user details

Gets details of a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Get user details
    api_response = api_instance.get_user1(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_external_id**
> User get_user_by_external_id(external_id)

Get user details by external ID

Gets details of a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Get user details by external ID
    api_response = api_instance.get_user_by_external_id(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_user_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_external_id1**
> User get_user_by_external_id1(external_id)

Get user details by external ID

Gets details of a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Get user details by external ID
    api_response = api_instance.get_user_by_external_id1(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_user_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_username**
> User get_user_by_username(username)

Get user details by username

Gets details of a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Get user details by username
    api_response = api_instance.get_user_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_user_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_username1**
> User get_user_by_username1(username)

Get user details by username

Gets details of a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Get user details by username
    api_response = api_instance.get_user_by_username1(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_user_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[UserStat] get_users()

Get all users

Gets a list of all users managed by this distributor

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get all users
    api_response = api_instance.get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserStat]**](UserStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users1**
> list[UserStat] get_users1()

Get all users

Gets a list of all users managed by this distributor

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))

try:
    # Get all users
    api_response = api_instance.get_users1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->get_users1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserStat]**](UserStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_password_reset_email**
> send_password_reset_email(user_id)

Set/reset password

Sends a user with given ID password recovery email

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Set/reset password
    api_instance.send_password_reset_email(user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->send_password_reset_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_password_reset_email1**
> send_password_reset_email1(user_id)

Set/reset password

Sends a user with given ID password recovery email

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
user_id = 789 # int | userId

try:
    # Set/reset password
    api_instance.send_password_reset_email1(user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->send_password_reset_email1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_password_reset_email_by_external_id**
> send_password_reset_email_by_external_id(external_id)

Set/reset password by external ID

Sends a user with given external ID password recovery email

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Set/reset password by external ID
    api_instance.send_password_reset_email_by_external_id(external_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->send_password_reset_email_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_password_reset_email_by_external_id1**
> send_password_reset_email_by_external_id1(external_id)

Set/reset password by external ID

Sends a user with given external ID password recovery email

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Set/reset password by external ID
    api_instance.send_password_reset_email_by_external_id1(external_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->send_password_reset_email_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_password_reset_email_by_username**
> send_password_reset_email_by_username(username)

Set/reset password by username

Sends a user with given username password recovery email

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Set/reset password by username
    api_instance.send_password_reset_email_by_username(username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->send_password_reset_email_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_password_reset_email_by_username1**
> send_password_reset_email_by_username1(username)

Set/reset password by username

Sends a user with given username password recovery email

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # Set/reset password by username
    api_instance.send_password_reset_email_by_username1(username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->send_password_reset_email_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_roles**
> set_roles(request, user_id)

setRoles

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetRolesRequest() # SetRolesRequest | request
user_id = 789 # int | userId

try:
    # setRoles
    api_instance.set_roles(request, user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->set_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetRolesRequest**](SetRolesRequest.md)| request | 
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_roles1**
> set_roles1(request, user_id)

setRoles

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetRolesRequest() # SetRolesRequest | request
user_id = 789 # int | userId

try:
    # setRoles
    api_instance.set_roles1(request, user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->set_roles1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetRolesRequest**](SetRolesRequest.md)| request | 
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_roles_by_external_id**
> set_roles_by_external_id(external_id, request)

setRolesByExternalId

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.SetRolesRequest() # SetRolesRequest | request

try:
    # setRolesByExternalId
    api_instance.set_roles_by_external_id(external_id, request)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->set_roles_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**SetRolesRequest**](SetRolesRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_roles_by_external_id1**
> set_roles_by_external_id1(external_id, request)

setRolesByExternalId

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.SetRolesRequest() # SetRolesRequest | request

try:
    # setRolesByExternalId
    api_instance.set_roles_by_external_id1(external_id, request)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->set_roles_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**SetRolesRequest**](SetRolesRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_roles_by_username**
> set_roles_by_username(request, username)

setRolesByUsername

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetRolesRequest() # SetRolesRequest | request
username = 'username_example' # str | username

try:
    # setRolesByUsername
    api_instance.set_roles_by_username(request, username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->set_roles_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetRolesRequest**](SetRolesRequest.md)| request | 
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_roles_by_username1**
> set_roles_by_username1(request, username)

setRolesByUsername

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.SetRolesRequest() # SetRolesRequest | request
username = 'username_example' # str | username

try:
    # setRolesByUsername
    api_instance.set_roles_by_username1(request, username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->set_roles_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SetRolesRequest**](SetRolesRequest.md)| request | 
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(request, user_id)

Update profile

Updates profile with a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.UpdateUserRequest() # UpdateUserRequest | request
user_id = 789 # int | userId

try:
    # Update profile
    api_instance.update_user(request, user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user1**
> update_user1(request, user_id)

Update profile

Updates profile with a user with given ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.UpdateUserRequest() # UpdateUserRequest | request
user_id = 789 # int | userId

try:
    # Update profile
    api_instance.update_user1(request, user_id)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->update_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 
 **user_id** | **int**| userId | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_external_id**
> update_user_by_external_id(external_id, request)

Update profile by external ID

Updates profile with a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.UpdateUserRequest() # UpdateUserRequest | request

try:
    # Update profile by external ID
    api_instance.update_user_by_external_id(external_id, request)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->update_user_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_external_id1**
> update_user_by_external_id1(external_id, request)

Update profile by external ID

Updates profile with a user with given external ID

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId
request = flexify_api.UpdateUserRequest() # UpdateUserRequest | request

try:
    # Update profile by external ID
    api_instance.update_user_by_external_id1(external_id, request)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->update_user_by_external_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_username**
> update_user_by_username(request, username)

Update profile by username

Updates profile with a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.UpdateUserRequest() # UpdateUserRequest | request
username = 'username_example' # str | username

try:
    # Update profile by username
    api_instance.update_user_by_username(request, username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->update_user_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_username1**
> update_user_by_username1(request, username)

Update profile by username

Updates profile with a user with given username

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
api_instance = flexify_api.PartnerUsersControllerApi(flexify_api.ApiClient(configuration))
request = flexify_api.UpdateUserRequest() # UpdateUserRequest | request
username = 'username_example' # str | username

try:
    # Update profile by username
    api_instance.update_user_by_username1(request, username)
except ApiException as e:
    print("Exception when calling PartnerUsersControllerApi->update_user_by_username1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateUserRequest**](UpdateUserRequest.md)| request | 
 **username** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

