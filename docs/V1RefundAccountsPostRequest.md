# V1RefundAccountsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**profile** | **int** |  | [optional] 
**legal_entity_type** | **str** |  | [optional] 
**name** | [**V1RefundAccountsPostRequestName**](V1RefundAccountsPostRequestName.md) |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from wise_api_client.models.v1_refund_accounts_post_request import V1RefundAccountsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1RefundAccountsPostRequest from a JSON string
v1_refund_accounts_post_request_instance = V1RefundAccountsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1RefundAccountsPostRequest.to_json())

# convert the object into a dict
v1_refund_accounts_post_request_dict = v1_refund_accounts_post_request_instance.to_dict()
# create an instance of V1RefundAccountsPostRequest from a dict
v1_refund_accounts_post_request_from_dict = V1RefundAccountsPostRequest.from_dict(v1_refund_accounts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


