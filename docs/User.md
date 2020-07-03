# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**BillingAccount**](BillingAccount.md) | Billing Account | [optional] 
**actual_limits** | [**UserConfig**](UserConfig.md) | Actual limits thar are currently in force | [optional] 
**delete_requested** | **datetime** | Time when user resueted to delete account | [optional] 
**external_id** | **str** | External ID of the user if specified | [optional] 
**id** | **int** | User ID in the system | [optional] 
**org** | [**Organization**](Organization.md) | Owning Organization | [optional] 
**profile** | [**UserProfile**](UserProfile.md) | User Profile | [optional] 
**registered** | **datetime** | Registration time | [optional] 
**require_license_terms** | **bool** | Indicates that this user does not have a password and needs to accept EULA | [optional] 
**roles** | **list[str]** | User Roles | [optional] 
**sign_up_code** | **str** | Sign up code used for sign up | [optional] 
**state** | **str** | User State | [optional] 
**user_limits** | [**UserConfig**](UserConfig.md) | Limits defined for this user | [optional] 
**username** | **str** | Username | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


