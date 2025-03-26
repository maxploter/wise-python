# V1TransfersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user** | **int** |  | 
**target_account** | **int** |  | 
**source_account** | **int** |  | [optional] 
**quote** | **int** |  | [optional] 
**quote_uuid** | **str** |  | 
**status** | **str** |  | 
**reference** | **str** |  | [optional] 
**rate** | **float** |  | 
**created** | **datetime** |  | 
**business** | **int** |  | [optional] 
**transfer_request** | **int** |  | [optional] 
**details** | [**TransferDetails**](TransferDetails.md) |  | 
**has_active_issues** | **bool** |  | [optional] 
**source_currency** | **str** |  | 
**source_value** | **float** |  | 
**target_currency** | **str** |  | 
**target_value** | **float** |  | 
**customer_transaction_id** | **str** |  | [optional] 
**originator** | [**Originator**](Originator.md) |  | 
**original_transfer_id** | **str** |  | 

## Example

```python
from wise_api_client.models.v1_transfers_get200_response_inner import V1TransfersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1TransfersGet200ResponseInner from a JSON string
v1_transfers_get200_response_inner_instance = V1TransfersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(V1TransfersGet200ResponseInner.to_json())

# convert the object into a dict
v1_transfers_get200_response_inner_dict = v1_transfers_get200_response_inner_instance.to_dict()
# create an instance of V1TransfersGet200ResponseInner from a dict
v1_transfers_get200_response_inner_from_dict = V1TransfersGet200ResponseInner.from_dict(v1_transfers_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


