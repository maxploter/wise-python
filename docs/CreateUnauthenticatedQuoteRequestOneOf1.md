# CreateUnauthenticatedQuoteRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_amount** | **float** | The amount in the target currency. Must be greater than 0. | 

## Example

```python
from wise_api_client.models.create_unauthenticated_quote_request_one_of1 import CreateUnauthenticatedQuoteRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnauthenticatedQuoteRequestOneOf1 from a JSON string
create_unauthenticated_quote_request_one_of1_instance = CreateUnauthenticatedQuoteRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(CreateUnauthenticatedQuoteRequestOneOf1.to_json())

# convert the object into a dict
create_unauthenticated_quote_request_one_of1_dict = create_unauthenticated_quote_request_one_of1_instance.to_dict()
# create an instance of CreateUnauthenticatedQuoteRequestOneOf1 from a dict
create_unauthenticated_quote_request_one_of1_from_dict = CreateUnauthenticatedQuoteRequestOneOf1.from_dict(create_unauthenticated_quote_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


