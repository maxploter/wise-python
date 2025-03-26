# BusinessProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**details** | [**BusinessProfileDetails**](BusinessProfileDetails.md) |  | [optional] 

## Example

```python
from wise_api_client.models.business_profile import BusinessProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessProfile from a JSON string
business_profile_instance = BusinessProfile.from_json(json)
# print the JSON string representation of the object
print(BusinessProfile.to_json())

# convert the object into a dict
business_profile_dict = business_profile_instance.to_dict()
# create an instance of BusinessProfile from a dict
business_profile_from_dict = BusinessProfile.from_dict(business_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


