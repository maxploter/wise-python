# CreateVerificationDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from wise_api_client.models.create_verification_document_response import CreateVerificationDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVerificationDocumentResponse from a JSON string
create_verification_document_response_instance = CreateVerificationDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateVerificationDocumentResponse.to_json())

# convert the object into a dict
create_verification_document_response_dict = create_verification_document_response_instance.to_dict()
# create an instance of CreateVerificationDocumentResponse from a dict
create_verification_document_response_from_dict = CreateVerificationDocumentResponse.from_dict(create_verification_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


