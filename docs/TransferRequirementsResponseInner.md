# TransferRequirementsResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**fields** | [**List[TransferRequirementsResponseInnerFieldsInner]**](TransferRequirementsResponseInnerFieldsInner.md) |  | [optional] 

## Example

```python
from wise_api_client.models.transfer_requirements_response_inner import TransferRequirementsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequirementsResponseInner from a JSON string
transfer_requirements_response_inner_instance = TransferRequirementsResponseInner.from_json(json)
# print the JSON string representation of the object
print(TransferRequirementsResponseInner.to_json())

# convert the object into a dict
transfer_requirements_response_inner_dict = transfer_requirements_response_inner_instance.to_dict()
# create an instance of TransferRequirementsResponseInner from a dict
transfer_requirements_response_inner_from_dict = TransferRequirementsResponseInner.from_dict(transfer_requirements_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


