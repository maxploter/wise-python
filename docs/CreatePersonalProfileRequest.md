# CreatePersonalProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**address** | [**CreatePersonalProfileRequestAddress**](CreatePersonalProfileRequestAddress.md) |  | 
**contact_details** | [**CreatePersonalProfileRequestContactDetails**](CreatePersonalProfileRequestContactDetails.md) |  | 

## Example

```python
from wise_api_client.models.create_personal_profile_request import CreatePersonalProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonalProfileRequest from a JSON string
create_personal_profile_request_instance = CreatePersonalProfileRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePersonalProfileRequest.to_json())

# convert the object into a dict
create_personal_profile_request_dict = create_personal_profile_request_instance.to_dict()
# create an instance of CreatePersonalProfileRequest from a dict
create_personal_profile_request_from_dict = CreatePersonalProfileRequest.from_dict(create_personal_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


