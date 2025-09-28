# ListTransfers200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique transfer identifier | 
**user** | **int** |  | 
**target_account** | **int** |  | 
**source_account** | **int** |  | [optional] 
**quote** | **int** |  | [optional] 
**quote_uuid** | **str** | A unique quote identifier in GUID format | 
**status** | **str** | The current status of the transfer. Common values include pending, processing, funded, cancelled, outgoing_payment_sent, funds_refunded. This list may be extended by the API provider. | 
**reference** | **str** |  | [optional] 
**rate** | **float** |  | 
**created** | **datetime** |  | 
**business** | **int** |  | [optional] 
**transfer_request** | **int** |  | [optional] 
**details** | [**TransferDetails**](TransferDetails.md) |  | 
**has_active_issues** | **bool** |  | [optional] 
**source_currency** | **str** | ISO 4217 three-letter currency code | 
**source_value** | **float** |  | 
**target_currency** | **str** | ISO 4217 three-letter currency code | 
**target_value** | **float** |  | 
**customer_transaction_id** | **str** |  | [optional] 
**originator** | [**Originator**](Originator.md) |  | 
**original_transfer_id** | **str** |  | 

## Example

```python
from wise_api_client.models.list_transfers200_response_inner import ListTransfers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransfers200ResponseInner from a JSON string
list_transfers200_response_inner_instance = ListTransfers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListTransfers200ResponseInner.to_json())

# convert the object into a dict
list_transfers200_response_inner_dict = list_transfers200_response_inner_instance.to_dict()
# create an instance of ListTransfers200ResponseInner from a dict
list_transfers200_response_inner_from_dict = ListTransfers200ResponseInner.from_dict(list_transfers200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


