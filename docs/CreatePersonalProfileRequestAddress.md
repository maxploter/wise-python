# CreatePersonalProfileRequestAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_first_line** | **str** |  | 
**city** | **str** |  | 
**country_iso3_code** | **str** |  | 

## Example

```python
from wise_api_client.models.create_personal_profile_request_address import CreatePersonalProfileRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonalProfileRequestAddress from a JSON string
create_personal_profile_request_address_instance = CreatePersonalProfileRequestAddress.from_json(json)
# print the JSON string representation of the object
print(CreatePersonalProfileRequestAddress.to_json())

# convert the object into a dict
create_personal_profile_request_address_dict = create_personal_profile_request_address_instance.to_dict()
# create an instance of CreatePersonalProfileRequestAddress from a dict
create_personal_profile_request_address_from_dict = CreatePersonalProfileRequestAddress.from_dict(create_personal_profile_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


