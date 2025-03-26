# OriginatorAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_line** | **str** |  | 
**city** | **str** |  | 
**state_code** | **str** |  | [optional] 
**country_code** | **str** |  | 
**post_code** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.originator_address import OriginatorAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatorAddress from a JSON string
originator_address_instance = OriginatorAddress.from_json(json)
# print the JSON string representation of the object
print(OriginatorAddress.to_json())

# convert the object into a dict
originator_address_dict = originator_address_instance.to_dict()
# create an instance of OriginatorAddress from a dict
originator_address_from_dict = OriginatorAddress.from_dict(originator_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


