# CreateAuthenticatedQuoteRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | ISO 4217 three-letter currency code | 
**target_currency** | **str** | ISO 4217 three-letter currency code | 
**target_account** | **int** | The ID of the recipient&#39;s account. This ID must exist in the system. | [optional] 
**payment_metadata** | [**CreateAuthenticatedQuoteRequestBasePaymentMetadata**](CreateAuthenticatedQuoteRequestBasePaymentMetadata.md) |  | [optional] 
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


