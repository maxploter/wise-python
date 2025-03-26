# VerificationStatusResponseRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** |  | [optional] 
**maximum_entitled_amount** | **float** |  | [optional] 
**current_status** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.verification_status_response_routes_inner import VerificationStatusResponseRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationStatusResponseRoutesInner from a JSON string
verification_status_response_routes_inner_instance = VerificationStatusResponseRoutesInner.from_json(json)
# print the JSON string representation of the object
print(VerificationStatusResponseRoutesInner.to_json())

# convert the object into a dict
verification_status_response_routes_inner_dict = verification_status_response_routes_inner_instance.to_dict()
# create an instance of VerificationStatusResponseRoutesInner from a dict
verification_status_response_routes_inner_from_dict = VerificationStatusResponseRoutesInner.from_dict(verification_status_response_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


