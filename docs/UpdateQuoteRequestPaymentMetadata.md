# UpdateQuoteRequestPaymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_nature** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.update_quote_request_payment_metadata import UpdateQuoteRequestPaymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuoteRequestPaymentMetadata from a JSON string
update_quote_request_payment_metadata_instance = UpdateQuoteRequestPaymentMetadata.from_json(json)
# print the JSON string representation of the object
print(UpdateQuoteRequestPaymentMetadata.to_json())

# convert the object into a dict
update_quote_request_payment_metadata_dict = update_quote_request_payment_metadata_instance.to_dict()
# create an instance of UpdateQuoteRequestPaymentMetadata from a dict
update_quote_request_payment_metadata_from_dict = UpdateQuoteRequestPaymentMetadata.from_dict(update_quote_request_payment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


