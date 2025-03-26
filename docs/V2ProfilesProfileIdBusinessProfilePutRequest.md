# V2ProfilesProfileIdBusinessProfilePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | [optional] 
**registration_number** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.v2_profiles_profile_id_business_profile_put_request import V2ProfilesProfileIdBusinessProfilePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2ProfilesProfileIdBusinessProfilePutRequest from a JSON string
v2_profiles_profile_id_business_profile_put_request_instance = V2ProfilesProfileIdBusinessProfilePutRequest.from_json(json)
# print the JSON string representation of the object
print(V2ProfilesProfileIdBusinessProfilePutRequest.to_json())

# convert the object into a dict
v2_profiles_profile_id_business_profile_put_request_dict = v2_profiles_profile_id_business_profile_put_request_instance.to_dict()
# create an instance of V2ProfilesProfileIdBusinessProfilePutRequest from a dict
v2_profiles_profile_id_business_profile_put_request_from_dict = V2ProfilesProfileIdBusinessProfilePutRequest.from_dict(v2_profiles_profile_id_business_profile_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


