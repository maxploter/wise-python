# CreateAuthenticatedTargetAmountQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | ISO 4217 three-letter currency code | 
**target_currency** | **str** | ISO 4217 three-letter currency code | 
**target_account** | **int** | A unique recipient account identifier | [optional] 
**pay_out** | **str** | Optional. Preferred payout method. Default value is BANK_TRANSFER. Common values include BANK_TRANSFER, BALANCE, SWIFT, SWIFT_OUR, INTERAC, but other values may be supported. | [optional] 
**preferred_pay_in** | **str** | Optional. Preferred payin method. Use BANK_TRANSFER to return this method at the top of the response&#39;s results. Common values include BANK_TRANSFER, BALANCE, SWIFT, SWIFT_OUR, INTERAC, but other values may be supported. | [optional] 
**payment_metadata** | [**PaymentMetadata**](PaymentMetadata.md) |  | [optional] 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 
**target_amount** | **float** | The amount in the target currency. Must be greater than 0. | 

## Example

```python
from wise_api_client.models.create_authenticated_target_amount_quote_request import CreateAuthenticatedTargetAmountQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatedTargetAmountQuoteRequest from a JSON string
create_authenticated_target_amount_quote_request_instance = CreateAuthenticatedTargetAmountQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatedTargetAmountQuoteRequest.to_json())

# convert the object into a dict
create_authenticated_target_amount_quote_request_dict = create_authenticated_target_amount_quote_request_instance.to_dict()
# create an instance of CreateAuthenticatedTargetAmountQuoteRequest from a dict
create_authenticated_target_amount_quote_request_from_dict = CreateAuthenticatedTargetAmountQuoteRequest.from_dict(create_authenticated_target_amount_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


