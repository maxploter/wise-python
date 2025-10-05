# BusinessProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique profile identifier | [optional] 
**type** | **str** |  | [optional] 
**public_id** | **str** | Public identifier for the profile | [optional] 
**user_id** | **int** | A unique user identifier | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**email** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**current_state** | **str** | The current state of the profile. Common values include VISIBLE, HIDDEN, SUSPENDED. | [optional] 
**contact_details** | [**ProfileContactDetails**](ProfileContactDetails.md) |  | [optional] 
**business_name** | **str** |  | [optional] 
**registration_number** | **str** |  | [optional] 
**description_of_business** | **str** | Business activity category. Common values include SOFTWARE_DEVELOPMENT, CONSULTING, RETAIL, MANUFACTURING, etc. | [optional] 
**webpage** | **str** |  | [optional] 
**company_type** | **str** | The type of business entity. Common values include LIMITED_COMPANY, PARTNERSHIP, SOLE_TRADER, etc. | [optional] 
**business_free_form_description** | **str** |  | [optional] 
**first_level_category** | **str** | Primary business category. Common values include TECHNOLOGY, FINANCE, RETAIL, etc. | [optional] 
**second_level_category** | **str** | Secondary business category. Common values include SOFTWARE_SERVICES, CONSULTING_SERVICES, etc. | [optional] 
**operational_addresses** | [**List[Address]**](Address.md) |  | [optional] 
**full_name** | **str** |  | [optional] 

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


