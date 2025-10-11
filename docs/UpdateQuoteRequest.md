# UpdateQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | ISO 4217 three-letter currency code | [optional] 
**target_currency** | **str** | ISO 4217 three-letter currency code | [optional] 
**target_account** | **int** | A unique recipient account identifier | [optional] 
**target_amount** | **float** | The amount in the target currency. Must be greater than 0. | [optional] 
**source_amount** | **float** | The amount in the source currency. Must be greater than 0. | [optional] 
**pay_out** | **str** |  | [optional] 
**payment_metadata** | [**PaymentMetadata**](PaymentMetadata.md) |  | [optional] 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 

## Example

```python
from wise_api_client.models.update_quote_request import UpdateQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuoteRequest from a JSON string
update_quote_request_instance = UpdateQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateQuoteRequest.to_json())

# convert the object into a dict
update_quote_request_dict = update_quote_request_instance.to_dict()
# create an instance of UpdateQuoteRequest from a dict
update_quote_request_from_dict = UpdateQuoteRequest.from_dict(update_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


