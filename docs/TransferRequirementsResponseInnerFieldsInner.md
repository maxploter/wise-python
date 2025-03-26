# TransferRequirementsResponseInnerFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**group** | [**List[RequirementField]**](RequirementField.md) |  | [optional] 

## Example

```python
from wise_api_client.models.transfer_requirements_response_inner_fields_inner import TransferRequirementsResponseInnerFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequirementsResponseInnerFieldsInner from a JSON string
transfer_requirements_response_inner_fields_inner_instance = TransferRequirementsResponseInnerFieldsInner.from_json(json)
# print the JSON string representation of the object
print(TransferRequirementsResponseInnerFieldsInner.to_json())

# convert the object into a dict
transfer_requirements_response_inner_fields_inner_dict = transfer_requirements_response_inner_fields_inner_instance.to_dict()
# create an instance of TransferRequirementsResponseInnerFieldsInner from a dict
transfer_requirements_response_inner_fields_inner_from_dict = TransferRequirementsResponseInnerFieldsInner.from_dict(transfer_requirements_response_inner_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


