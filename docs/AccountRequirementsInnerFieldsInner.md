# AccountRequirementsInnerFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**group** | [**List[AccountRequirementsInnerFieldsInnerGroupInner]**](AccountRequirementsInnerFieldsInnerGroupInner.md) |  | [optional] 

## Example

```python
from wise_api_client.models.account_requirements_inner_fields_inner import AccountRequirementsInnerFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequirementsInnerFieldsInner from a JSON string
account_requirements_inner_fields_inner_instance = AccountRequirementsInnerFieldsInner.from_json(json)
# print the JSON string representation of the object
print(AccountRequirementsInnerFieldsInner.to_json())

# convert the object into a dict
account_requirements_inner_fields_inner_dict = account_requirements_inner_fields_inner_instance.to_dict()
# create an instance of AccountRequirementsInnerFieldsInner from a dict
account_requirements_inner_fields_inner_from_dict = AccountRequirementsInnerFieldsInner.from_dict(account_requirements_inner_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


