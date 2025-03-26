# V2ProfilesProfileIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**details** | [**BusinessProfileDetails**](BusinessProfileDetails.md) |  | [optional] 

## Example

```python
from wise_api_client.models.v2_profiles_profile_id_get200_response import V2ProfilesProfileIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2ProfilesProfileIdGet200Response from a JSON string
v2_profiles_profile_id_get200_response_instance = V2ProfilesProfileIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V2ProfilesProfileIdGet200Response.to_json())

# convert the object into a dict
v2_profiles_profile_id_get200_response_dict = v2_profiles_profile_id_get200_response_instance.to_dict()
# create an instance of V2ProfilesProfileIdGet200Response from a dict
v2_profiles_profile_id_get200_response_from_dict = V2ProfilesProfileIdGet200Response.from_dict(v2_profiles_profile_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


