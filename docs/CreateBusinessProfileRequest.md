# CreateBusinessProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | 
**registration_number** | **str** |  | 
**company_type** | **str** |  | 

## Example

```python
from wise_api_client.models.create_business_profile_request import CreateBusinessProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBusinessProfileRequest from a JSON string
create_business_profile_request_instance = CreateBusinessProfileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBusinessProfileRequest.to_json())

# convert the object into a dict
create_business_profile_request_dict = create_business_profile_request_instance.to_dict()
# create an instance of CreateBusinessProfileRequest from a dict
create_business_profile_request_from_dict = CreateBusinessProfileRequest.from_dict(create_business_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


