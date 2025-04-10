# CreateRefundRecipientAccountRequestName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.create_refund_recipient_account_request_name import CreateRefundRecipientAccountRequestName

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundRecipientAccountRequestName from a JSON string
create_refund_recipient_account_request_name_instance = CreateRefundRecipientAccountRequestName.from_json(json)
# print the JSON string representation of the object
print(CreateRefundRecipientAccountRequestName.to_json())

# convert the object into a dict
create_refund_recipient_account_request_name_dict = create_refund_recipient_account_request_name_instance.to_dict()
# create an instance of CreateRefundRecipientAccountRequestName from a dict
create_refund_recipient_account_request_name_from_dict = CreateRefundRecipientAccountRequestName.from_dict(create_refund_recipient_account_request_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


