# PersonalProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique profile identifier | [optional] 
**type** | **str** |  | [optional] 
**details** | [**PersonalProfileDetails**](PersonalProfileDetails.md) |  | [optional] 

## Example

```python
from wise_api_client.models.personal_profile import PersonalProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalProfile from a JSON string
personal_profile_instance = PersonalProfile.from_json(json)
# print the JSON string representation of the object
print(PersonalProfile.to_json())

# convert the object into a dict
personal_profile_dict = personal_profile_instance.to_dict()
# create an instance of PersonalProfile from a dict
personal_profile_from_dict = PersonalProfile.from_dict(personal_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


