# ListProfiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**details** | [**BusinessProfileDetails**](BusinessProfileDetails.md) |  | [optional] 

## Example

```python
from wise_api_client.models.list_profiles200_response_inner import ListProfiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListProfiles200ResponseInner from a JSON string
list_profiles200_response_inner_instance = ListProfiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListProfiles200ResponseInner.to_json())

# convert the object into a dict
list_profiles200_response_inner_dict = list_profiles200_response_inner_instance.to_dict()
# create an instance of ListProfiles200ResponseInner from a dict
list_profiles200_response_inner_from_dict = ListProfiles200ResponseInner.from_dict(list_profiles200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


