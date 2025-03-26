# CreatePersonalProfileRequestContactDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**phone_number** | **str** |  | 

## Example

```python
from wise_api_client.models.create_personal_profile_request_contact_details import CreatePersonalProfileRequestContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonalProfileRequestContactDetails from a JSON string
create_personal_profile_request_contact_details_instance = CreatePersonalProfileRequestContactDetails.from_json(json)
# print the JSON string representation of the object
print(CreatePersonalProfileRequestContactDetails.to_json())

# convert the object into a dict
create_personal_profile_request_contact_details_dict = create_personal_profile_request_contact_details_instance.to_dict()
# create an instance of CreatePersonalProfileRequestContactDetails from a dict
create_personal_profile_request_contact_details_from_dict = CreatePersonalProfileRequestContactDetails.from_dict(create_personal_profile_request_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


