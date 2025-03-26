# RecipientName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.recipient_name import RecipientName

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientName from a JSON string
recipient_name_instance = RecipientName.from_json(json)
# print the JSON string representation of the object
print(RecipientName.to_json())

# convert the object into a dict
recipient_name_dict = recipient_name_instance.to_dict()
# create an instance of RecipientName from a dict
recipient_name_from_dict = RecipientName.from_dict(recipient_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


