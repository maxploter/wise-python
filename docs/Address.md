# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**address_first_line** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country_iso2_code** | **str** |  | [optional] 
**country_iso3_code** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


