# CreateAuthenticatedQuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** |  | 
**target_currency** | **str** |  | 
**source_amount** | **float** |  | [optional] 
**target_amount** | **float** |  | [optional] 
**target_account** | **int** |  | [optional] 
**payment_metadata** | **object** |  | [optional] 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 

## Example

```python
from wise_api_client.models.create_authenticated_quote_request import CreateAuthenticatedQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatedQuoteRequest from a JSON string
create_authenticated_quote_request_instance = CreateAuthenticatedQuoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatedQuoteRequest.to_json())

# convert the object into a dict
create_authenticated_quote_request_dict = create_authenticated_quote_request_instance.to_dict()
# create an instance of CreateAuthenticatedQuoteRequest from a dict
create_authenticated_quote_request_from_dict = CreateAuthenticatedQuoteRequest.from_dict(create_authenticated_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


