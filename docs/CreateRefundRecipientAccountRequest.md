# CreateRefundRecipientAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**profile** | **int** |  | [optional] 
**legal_entity_type** | **str** |  | [optional] 
**name** | [**CreateRefundRecipientAccountRequestName**](CreateRefundRecipientAccountRequestName.md) |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from wise_api_client.models.create_refund_recipient_account_request import CreateRefundRecipientAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundRecipientAccountRequest from a JSON string
create_refund_recipient_account_request_instance = CreateRefundRecipientAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRefundRecipientAccountRequest.to_json())

# convert the object into a dict
create_refund_recipient_account_request_dict = create_refund_recipient_account_request_instance.to_dict()
# create an instance of CreateRefundRecipientAccountRequest from a dict
create_refund_recipient_account_request_from_dict = CreateRefundRecipientAccountRequest.from_dict(create_refund_recipient_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


