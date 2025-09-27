# CreateUnauthenticatedQuoteRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | ISO 4217 three-letter currency code | 
**target_currency** | **str** | ISO 4217 three-letter currency code | 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 

## Example

```python
from wise_api_client.models.create_unauthenticated_quote_request_base import CreateUnauthenticatedQuoteRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnauthenticatedQuoteRequestBase from a JSON string
create_unauthenticated_quote_request_base_instance = CreateUnauthenticatedQuoteRequestBase.from_json(json)
# print the JSON string representation of the object
print(CreateUnauthenticatedQuoteRequestBase.to_json())

# convert the object into a dict
create_unauthenticated_quote_request_base_dict = create_unauthenticated_quote_request_base_instance.to_dict()
# create an instance of CreateUnauthenticatedQuoteRequestBase from a dict
create_unauthenticated_quote_request_base_from_dict = CreateUnauthenticatedQuoteRequestBase.from_dict(create_unauthenticated_quote_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


