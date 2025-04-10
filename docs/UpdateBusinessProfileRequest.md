# UpdateBusinessProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | [optional] 
**registration_number** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.update_business_profile_request import UpdateBusinessProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBusinessProfileRequest from a JSON string
update_business_profile_request_instance = UpdateBusinessProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBusinessProfileRequest.to_json())

# convert the object into a dict
update_business_profile_request_dict = update_business_profile_request_instance.to_dict()
# create an instance of UpdateBusinessProfileRequest from a dict
update_business_profile_request_from_dict = UpdateBusinessProfileRequest.from_dict(update_business_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


