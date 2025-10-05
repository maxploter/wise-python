# PersonalProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** | A unique profile identifier | [optional] 
**public_id** | **str** | Public identifier for the profile | [optional] 
**user_id** | **int** | A unique user identifier | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**email** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**avatar** | **str** |  | [optional] 
**current_state** | **str** | The current state of the profile. Common values include VISIBLE, HIDDEN, SUSPENDED. | [optional] 
**contact_details** | [**ProfileContactDetails**](ProfileContactDetails.md) |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**preferred_name** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**secondary_addresses** | [**List[Address]**](Address.md) |  | [optional] 
**full_name** | **str** |  | [optional] 

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


