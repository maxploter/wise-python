# AccountRequirementsInnerFieldsInnerGroupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**validation_regexp** | **str** |  | [optional] 
**values_allowed** | [**List[AccountRequirementsInnerFieldsInnerGroupInnerValuesAllowedInner]**](AccountRequirementsInnerFieldsInnerGroupInnerValuesAllowedInner.md) |  | [optional] 

## Example

```python
from wise_api_client.models.account_requirements_inner_fields_inner_group_inner import AccountRequirementsInnerFieldsInnerGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequirementsInnerFieldsInnerGroupInner from a JSON string
account_requirements_inner_fields_inner_group_inner_instance = AccountRequirementsInnerFieldsInnerGroupInner.from_json(json)
# print the JSON string representation of the object
print(AccountRequirementsInnerFieldsInnerGroupInner.to_json())

# convert the object into a dict
account_requirements_inner_fields_inner_group_inner_dict = account_requirements_inner_fields_inner_group_inner_instance.to_dict()
# create an instance of AccountRequirementsInnerFieldsInnerGroupInner from a dict
account_requirements_inner_fields_inner_group_inner_from_dict = AccountRequirementsInnerFieldsInnerGroupInner.from_dict(account_requirements_inner_fields_inner_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


