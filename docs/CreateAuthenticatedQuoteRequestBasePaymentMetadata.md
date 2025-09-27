# CreateAuthenticatedQuoteRequestBasePaymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_nature** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.create_authenticated_quote_request_base_payment_metadata import CreateAuthenticatedQuoteRequestBasePaymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatedQuoteRequestBasePaymentMetadata from a JSON string
create_authenticated_quote_request_base_payment_metadata_instance = CreateAuthenticatedQuoteRequestBasePaymentMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatedQuoteRequestBasePaymentMetadata.to_json())

# convert the object into a dict
create_authenticated_quote_request_base_payment_metadata_dict = create_authenticated_quote_request_base_payment_metadata_instance.to_dict()
# create an instance of CreateAuthenticatedQuoteRequestBasePaymentMetadata from a dict
create_authenticated_quote_request_base_payment_metadata_from_dict = CreateAuthenticatedQuoteRequestBasePaymentMetadata.from_dict(create_authenticated_quote_request_base_payment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


