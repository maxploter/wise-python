# Recipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**creator_id** | **int** | A unique user identifier | [optional] 
**profile_id** | **int** | A unique profile identifier | [optional] 
**name** | [**RecipientName**](RecipientName.md) |  | [optional] 
**currency** | **str** | ISO 4217 three-letter currency code | [optional] 
**country** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**legal_entity_type** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**details** | [**RecipientDetails**](RecipientDetails.md) |  | [optional] 
**common_field_map** | [**RecipientCommonFieldMap**](RecipientCommonFieldMap.md) |  | [optional] 
**hash** | **str** |  | [optional] 
**account_summary** | **str** |  | [optional] 
**long_account_summary** | **str** |  | [optional] 
**display_fields** | [**List[RecipientDisplayFieldsInner]**](RecipientDisplayFieldsInner.md) |  | [optional] 
**owned_by_customer** | **bool** |  | [optional] 

## Example

```python
from wise_api_client.models.recipient import Recipient

# TODO update the JSON string below
json = "{}"
# create an instance of Recipient from a JSON string
recipient_instance = Recipient.from_json(json)
# print the JSON string representation of the object
print(Recipient.to_json())

# convert the object into a dict
recipient_dict = recipient_instance.to_dict()
# create an instance of Recipient from a dict
recipient_from_dict = Recipient.from_dict(recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


