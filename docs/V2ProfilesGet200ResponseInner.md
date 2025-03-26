# V2ProfilesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**details** | [**BusinessProfileDetails**](BusinessProfileDetails.md) |  | [optional] 

## Example

```python
from wise_api_client.models.v2_profiles_get200_response_inner import V2ProfilesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2ProfilesGet200ResponseInner from a JSON string
v2_profiles_get200_response_inner_instance = V2ProfilesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(V2ProfilesGet200ResponseInner.to_json())

# convert the object into a dict
v2_profiles_get200_response_inner_dict = v2_profiles_get200_response_inner_instance.to_dict()
# create an instance of V2ProfilesGet200ResponseInner from a dict
v2_profiles_get200_response_inner_from_dict = V2ProfilesGet200ResponseInner.from_dict(v2_profiles_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


