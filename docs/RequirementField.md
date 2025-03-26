# RequirementField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**refresh_requirements_on_change** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**display_format** | **str** |  | [optional] 
**example** | **str** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**validation_regexp** | **str** |  | [optional] 
**values_allowed** | [**List[AccountRequirementsInnerFieldsInnerGroupInnerValuesAllowedInner]**](AccountRequirementsInnerFieldsInnerGroupInnerValuesAllowedInner.md) |  | [optional] 

## Example

```python
from wise_api_client.models.requirement_field import RequirementField

# TODO update the JSON string below
json = "{}"
# create an instance of RequirementField from a JSON string
requirement_field_instance = RequirementField.from_json(json)
# print the JSON string representation of the object
print(RequirementField.to_json())

# convert the object into a dict
requirement_field_dict = requirement_field_instance.to_dict()
# create an instance of RequirementField from a dict
requirement_field_from_dict = RequirementField.from_dict(requirement_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


