# UpdatePersonalProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.update_personal_profile_request import UpdatePersonalProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePersonalProfileRequest from a JSON string
update_personal_profile_request_instance = UpdatePersonalProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePersonalProfileRequest.to_json())

# convert the object into a dict
update_personal_profile_request_dict = update_personal_profile_request_instance.to_dict()
# create an instance of UpdatePersonalProfileRequest from a dict
update_personal_profile_request_from_dict = UpdatePersonalProfileRequest.from_dict(update_personal_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


