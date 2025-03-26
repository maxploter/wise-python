# RecipientCommonFieldMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code_field** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.recipient_common_field_map import RecipientCommonFieldMap

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientCommonFieldMap from a JSON string
recipient_common_field_map_instance = RecipientCommonFieldMap.from_json(json)
# print the JSON string representation of the object
print(RecipientCommonFieldMap.to_json())

# convert the object into a dict
recipient_common_field_map_dict = recipient_common_field_map_instance.to_dict()
# create an instance of RecipientCommonFieldMap from a dict
recipient_common_field_map_from_dict = RecipientCommonFieldMap.from_dict(recipient_common_field_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


