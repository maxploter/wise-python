# BusinessProfileDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**registration_number** | **str** |  | [optional] 
**company_type** | **str** |  | [optional] 
**primary_address** | **int** |  | [optional] 

## Example

```python
from wise_api_client.models.business_profile_details import BusinessProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessProfileDetails from a JSON string
business_profile_details_instance = BusinessProfileDetails.from_json(json)
# print the JSON string representation of the object
print(BusinessProfileDetails.to_json())

# convert the object into a dict
business_profile_details_dict = business_profile_details_instance.to_dict()
# create an instance of BusinessProfileDetails from a dict
business_profile_details_from_dict = BusinessProfileDetails.from_dict(business_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


