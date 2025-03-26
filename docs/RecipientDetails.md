# RecipientDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** |  | [optional] 
**sort_code** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.recipient_details import RecipientDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientDetails from a JSON string
recipient_details_instance = RecipientDetails.from_json(json)
# print the JSON string representation of the object
print(RecipientDetails.to_json())

# convert the object into a dict
recipient_details_dict = recipient_details_instance.to_dict()
# create an instance of RecipientDetails from a dict
recipient_details_from_dict = RecipientDetails.from_dict(recipient_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


