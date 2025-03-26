# VerificationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routes** | [**List[VerificationStatusResponseRoutesInner]**](VerificationStatusResponseRoutesInner.md) |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.verification_status_response import VerificationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationStatusResponse from a JSON string
verification_status_response_instance = VerificationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(VerificationStatusResponse.to_json())

# convert the object into a dict
verification_status_response_dict = verification_status_response_instance.to_dict()
# create an instance of VerificationStatusResponse from a dict
verification_status_response_from_dict = VerificationStatusResponse.from_dict(verification_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


