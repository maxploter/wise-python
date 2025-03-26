# PersonalProfileDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**occupations** | [**List[PersonalProfileDetailsOccupationsInner]**](PersonalProfileDetailsOccupationsInner.md) |  | [optional] 
**primary_address** | **int** |  | [optional] 
**first_name_in_kana** | **str** |  | [optional] 
**last_name_in_kana** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.personal_profile_details import PersonalProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalProfileDetails from a JSON string
personal_profile_details_instance = PersonalProfileDetails.from_json(json)
# print the JSON string representation of the object
print(PersonalProfileDetails.to_json())

# convert the object into a dict
personal_profile_details_dict = personal_profile_details_instance.to_dict()
# create an instance of PersonalProfileDetails from a dict
personal_profile_details_from_dict = PersonalProfileDetails.from_dict(personal_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


