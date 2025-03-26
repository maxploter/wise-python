# UBO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**country_of_residence_iso3_code** | **str** |  | [optional] 
**address_first_line** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**ownership_percentage** | **int** |  | [optional] 

## Example

```python
from wise_api_client.models.ubo import UBO

# TODO update the JSON string below
json = "{}"
# create an instance of UBO from a JSON string
ubo_instance = UBO.from_json(json)
# print the JSON string representation of the object
print(UBO.to_json())

# convert the object into a dict
ubo_dict = ubo_instance.to_dict()
# create an instance of UBO from a dict
ubo_from_dict = UBO.from_dict(ubo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


