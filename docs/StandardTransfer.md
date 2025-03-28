# StandardTransfer


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

## Example

```python
from wise_api_client.models.standard_transfer import StandardTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of StandardTransfer from a JSON string
standard_transfer_instance = StandardTransfer.from_json(json)
# print the JSON string representation of the object
print(StandardTransfer.to_json())

# convert the object into a dict
standard_transfer_dict = standard_transfer_instance.to_dict()
# create an instance of StandardTransfer from a dict
standard_transfer_from_dict = StandardTransfer.from_dict(standard_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


