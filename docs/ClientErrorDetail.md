# ClientErrorDetail

Detailed error information for client errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code | 
**message** | **str** | Human-readable error message | 
**path** | **str** | The field path that caused the error | 
**arguments** | **List[str]** | Additional arguments related to the error | 

## Example

```python
from wise_api_client.models.client_error_detail import ClientErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClientErrorDetail from a JSON string
client_error_detail_instance = ClientErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ClientErrorDetail.to_json())

# convert the object into a dict
client_error_detail_dict = client_error_detail_instance.to_dict()
# create an instance of ClientErrorDetail from a dict
client_error_detail_from_dict = ClientErrorDetail.from_dict(client_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


