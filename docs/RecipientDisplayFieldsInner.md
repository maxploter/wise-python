# RecipientDisplayFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.recipient_display_fields_inner import RecipientDisplayFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientDisplayFieldsInner from a JSON string
recipient_display_fields_inner_instance = RecipientDisplayFieldsInner.from_json(json)
# print the JSON string representation of the object
print(RecipientDisplayFieldsInner.to_json())

# convert the object into a dict
recipient_display_fields_inner_dict = recipient_display_fields_inner_instance.to_dict()
# create an instance of RecipientDisplayFieldsInner from a dict
recipient_display_fields_inner_from_dict = RecipientDisplayFieldsInner.from_dict(recipient_display_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


