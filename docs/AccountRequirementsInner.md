# AccountRequirementsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**fields** | [**List[AccountRequirementsInnerFieldsInner]**](AccountRequirementsInnerFieldsInner.md) |  | [optional] 

## Example

```python
from wise_api_client.models.account_requirements_inner import AccountRequirementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequirementsInner from a JSON string
account_requirements_inner_instance = AccountRequirementsInner.from_json(json)
# print the JSON string representation of the object
print(AccountRequirementsInner.to_json())

# convert the object into a dict
account_requirements_inner_dict = account_requirements_inner_instance.to_dict()
# create an instance of AccountRequirementsInner from a dict
account_requirements_inner_from_dict = AccountRequirementsInner.from_dict(account_requirements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


