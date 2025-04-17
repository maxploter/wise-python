# GetProfileById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**details** | [**BusinessProfileDetails**](BusinessProfileDetails.md) |  | [optional] 

## Example

```python
from wise_api_client.models.get_profile_by_id200_response import GetProfileById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfileById200Response from a JSON string
get_profile_by_id200_response_instance = GetProfileById200Response.from_json(json)
# print the JSON string representation of the object
print(GetProfileById200Response.to_json())

# convert the object into a dict
get_profile_by_id200_response_dict = get_profile_by_id200_response_instance.to_dict()
# create an instance of GetProfileById200Response from a dict
get_profile_by_id200_response_from_dict = GetProfileById200Response.from_dict(get_profile_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


