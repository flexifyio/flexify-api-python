# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**BillingAccount**](BillingAccount.md) | Billing Account associated with this user | [optional] 
**actual_limits** | [**UserConfig**](UserConfig.md) | Actual limits thar are currently in force | [optional] 
**delete_requested** | **datetime** | If not null - time when the user requested to delete his or her account | [optional] 
**external_id** | **str** | External ID of the user, if specified | [optional] 
**id** | **int** | User ID in the system | [optional] 
**org** | [**Organization**](Organization.md) | Organization owning this user | [optional] 
**profile** | [**UserProfile**](UserProfile.md) | User&#39;s profile | [optional] 
**registered** | **datetime** | Registration time | [optional] 
**require_license_terms** | **bool** | Indicates that this user does not have a password and needs to accept EULA | [optional] 
**roles** | **list[str]** | Roles associated with this user | [optional] 
**settings** | [**UserSettings**](UserSettings.md) | User&#39;s settings | [optional] 
**sign_up_code** | **str** | Sign up code that the user used when signing up | [optional] 
**state** | **str** | State of this user | [optional] 
**user_limits** | [**UserConfig**](UserConfig.md) | Limits defined for this user | [optional] 
**username** | **str** | Username, always the same as user&#39;s email | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


