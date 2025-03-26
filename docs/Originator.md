# Originator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_entity_type** | **str** |  | 
**reference** | **str** |  | 
**name** | [**OriginatorName**](OriginatorName.md) |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**business_registration_code** | **str** |  | [optional] 
**address** | [**OriginatorAddress**](OriginatorAddress.md) |  | 
**account_details** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.originator import Originator

# TODO update the JSON string below
json = "{}"
# create an instance of Originator from a JSON string
originator_instance = Originator.from_json(json)
# print the JSON string representation of the object
print(Originator.to_json())

# convert the object into a dict
originator_dict = originator_instance.to_dict()
# create an instance of Originator from a dict
originator_from_dict = Originator.from_dict(originator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


