# CreateUnauthenticatedQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | ISO 4217 three-letter currency code | 
**target_currency** | **str** | ISO 4217 three-letter currency code | 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 
**source_amount** | **float** | The amount in the source currency. Must be greater than 0. | 
**target_amount** | **float** | The amount in the target currency. Must be greater than 0. | 

## Example

```python
from wise_api_client.models.create_unauthenticated_quote_request import CreateUnauthenticatedQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnauthenticatedQuoteRequest from a JSON string
create_unauthenticated_quote_request_instance = CreateUnauthenticatedQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUnauthenticatedQuoteRequest.to_json())

# convert the object into a dict
create_unauthenticated_quote_request_dict = create_unauthenticated_quote_request_instance.to_dict()
# create an instance of CreateUnauthenticatedQuoteRequest from a dict
create_unauthenticated_quote_request_from_dict = CreateUnauthenticatedQuoteRequest.from_dict(create_unauthenticated_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


