# BillingAccountWithMoney

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **str** | System Account state (Updated by Administrator) | [optional] 
**aggregate_state** | **str** | Aggregated Account state (ACTIVE only if admin state and billing state are ACTIVE) | [optional] 
**balance** | [**Money**](Money.md) | Account Current Balance | [optional] 
**billing_state** | **str** | Billing Account state (Depend on balance and max credit) | [optional] 
**created_date** | **datetime** | Created Timestamp | [optional] 
**credit_exceeded** | **bool** | Is credit exceeded | [optional] 
**distributor** | [**Distributor**](Distributor.md) | Distributor that manages this account | [optional] 
**id** | **int** | Account Id | [optional] 
**max_credit** | [**Money**](Money.md) | Account Maximum Credit | [optional] 
**name** | **str** | Account Name | [optional] 
**price_list** | [**PriceList**](PriceList.md) | Price list (without prices) | [optional] 
**total_cost** | [**Money**](Money.md) | Account Total Cost | [optional] 
**total_paid** | [**Money**](Money.md) | Account Total Paid | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


