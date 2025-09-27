# CreateAuthenticatedQuoteRequestBase


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

## Example

```python
from wise_api_client.models.create_authenticated_quote_request_base import CreateAuthenticatedQuoteRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatedQuoteRequestBase from a JSON string
create_authenticated_quote_request_base_instance = CreateAuthenticatedQuoteRequestBase.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatedQuoteRequestBase.to_json())

# convert the object into a dict
create_authenticated_quote_request_base_dict = create_authenticated_quote_request_base_instance.to_dict()
# create an instance of CreateAuthenticatedQuoteRequestBase from a dict
create_authenticated_quote_request_base_from_dict = CreateAuthenticatedQuoteRequestBase.from_dict(create_authenticated_quote_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


