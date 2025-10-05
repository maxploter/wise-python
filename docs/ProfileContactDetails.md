# ProfileContactDetails

Contact information for a profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.profile_contact_details import ProfileContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileContactDetails from a JSON string
profile_contact_details_instance = ProfileContactDetails.from_json(json)
# print the JSON string representation of the object
print(ProfileContactDetails.to_json())

# convert the object into a dict
profile_contact_details_dict = profile_contact_details_instance.to_dict()
# create an instance of ProfileContactDetails from a dict
profile_contact_details_from_dict = ProfileContactDetails.from_dict(profile_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


