# CreateUnauthenticatedQuoteRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_amount** | **float** | The amount in the source currency. Must be greater than 0. | 

## Example

```python
from wise_api_client.models.create_unauthenticated_quote_request_one_of import CreateUnauthenticatedQuoteRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnauthenticatedQuoteRequestOneOf from a JSON string
create_unauthenticated_quote_request_one_of_instance = CreateUnauthenticatedQuoteRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(CreateUnauthenticatedQuoteRequestOneOf.to_json())

# convert the object into a dict
create_unauthenticated_quote_request_one_of_dict = create_unauthenticated_quote_request_one_of_instance.to_dict()
# create an instance of CreateUnauthenticatedQuoteRequestOneOf from a dict
create_unauthenticated_quote_request_one_of_from_dict = CreateUnauthenticatedQuoteRequestOneOf.from_dict(create_unauthenticated_quote_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


