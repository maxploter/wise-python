# OriginatorName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**given_name** | **str** |  | 
**middle_names** | **List[str]** |  | [optional] 
**family_name** | **str** |  | 
**patronymic_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.originator_name import OriginatorName

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatorName from a JSON string
originator_name_instance = OriginatorName.from_json(json)
# print the JSON string representation of the object
print(OriginatorName.to_json())

# convert the object into a dict
originator_name_dict = originator_name_instance.to_dict()
# create an instance of OriginatorName from a dict
originator_name_from_dict = OriginatorName.from_dict(originator_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


