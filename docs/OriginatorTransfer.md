# OriginatorTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique transfer identifier | 
**user** | **int** |  | 
**target_account** | **int** |  | 
**source_account** | **int** |  | [optional] 
**quote** | **str** | quote ID | [optional] 
**status** | **str** | The current status of the transfer. Common values include pending, processing, funded, cancelled, outgoing_payment_sent, funds_refunded. This list may be extended by the API provider. | 
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
**original_transfer_id** | **str** | Unique identifier randomly generated per transfer request by the calling client | 
**payin_session_id** | **str** | ID of the Payin Session generated for the transfer | [optional] 
**originator** | [**Originator**](Originator.md) |  | 

## Example

```python
from wise_api_client.models.originator_transfer import OriginatorTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatorTransfer from a JSON string
originator_transfer_instance = OriginatorTransfer.from_json(json)
# print the JSON string representation of the object
print(OriginatorTransfer.to_json())

# convert the object into a dict
originator_transfer_dict = originator_transfer_instance.to_dict()
# create an instance of OriginatorTransfer from a dict
originator_transfer_from_dict = OriginatorTransfer.from_dict(originator_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


