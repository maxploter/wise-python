# CreateVerificationDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**unique_identifier** | **str** |  | 

## Example

```python
from wise_api_client.models.create_verification_document_request import CreateVerificationDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationDocumentRequest from a JSON string
create_verification_document_request_instance = CreateVerificationDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationDocumentRequest.to_json())

# convert the object into a dict
create_verification_document_request_dict = create_verification_document_request_instance.to_dict()
# create an instance of CreateVerificationDocumentRequest from a dict
create_verification_document_request_from_dict = CreateVerificationDocumentRequest.from_dict(create_verification_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


