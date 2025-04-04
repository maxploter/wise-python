# CreateAuthenticatedQuoteRequestPaymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_nature** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.create_authenticated_quote_request_payment_metadata import CreateAuthenticatedQuoteRequestPaymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatedQuoteRequestPaymentMetadata from a JSON string
create_authenticated_quote_request_payment_metadata_instance = CreateAuthenticatedQuoteRequestPaymentMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatedQuoteRequestPaymentMetadata.to_json())

# convert the object into a dict
create_authenticated_quote_request_payment_metadata_dict = create_authenticated_quote_request_payment_metadata_instance.to_dict()
# create an instance of CreateAuthenticatedQuoteRequestPaymentMetadata from a dict
create_authenticated_quote_request_payment_metadata_from_dict = CreateAuthenticatedQuoteRequestPaymentMetadata.from_dict(create_authenticated_quote_request_payment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


