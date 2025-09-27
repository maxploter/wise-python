# CreateUnauthenticatedTargetAmountQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | ISO 4217 three-letter currency code | 
**target_currency** | **str** | ISO 4217 three-letter currency code | 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 
**target_amount** | **float** | The amount in the target currency. Must be greater than 0. | 

## Example

```python
from wise_api_client.models.create_unauthenticated_target_amount_quote_request import CreateUnauthenticatedTargetAmountQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnauthenticatedTargetAmountQuoteRequest from a JSON string
create_unauthenticated_target_amount_quote_request_instance = CreateUnauthenticatedTargetAmountQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUnauthenticatedTargetAmountQuoteRequest.to_json())

# convert the object into a dict
create_unauthenticated_target_amount_quote_request_dict = create_unauthenticated_target_amount_quote_request_instance.to_dict()
# create an instance of CreateUnauthenticatedTargetAmountQuoteRequest from a dict
create_unauthenticated_target_amount_quote_request_from_dict = CreateUnauthenticatedTargetAmountQuoteRequest.from_dict(create_unauthenticated_target_amount_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


