# BillingAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **str** | System Account state (Updated by Administrator) | [optional] 
**aggregate_state** | **str** | Aggregated Account state (ACTIVE only if admin state and billing state are ACTIVE) | [optional] 
**billing_state** | **str** | Billing Account state (Depend on balance and max credit) | [optional] 
**created_date** | **datetime** | Created Timestamp | [optional] 
**distributor** | [**Distributor**](Distributor.md) | Distributor that manages this account | [optional] 
**id** | **int** | Account Id | [optional] 
**max_credit** | [**Money**](Money.md) | Account Maximum Credit | [optional] 
**name** | **str** | Account Name | [optional] 
**price_list** | [**PriceList**](PriceList.md) | Price list (without prices) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


