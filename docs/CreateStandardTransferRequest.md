# CreateStandardTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account** | **int** |  | [optional] 
**target_account** | **int** |  | 
**quote_uuid** | **str** |  | 
**customer_transaction_id** | **str** |  | 
**details** | [**TransferDetails**](TransferDetails.md) |  | 

## Example

```python
from wise_api_client.models.create_standard_transfer_request import CreateStandardTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStandardTransferRequest from a JSON string
create_standard_transfer_request_instance = CreateStandardTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStandardTransferRequest.to_json())

# convert the object into a dict
create_standard_transfer_request_dict = create_standard_transfer_request_instance.to_dict()
# create an instance of CreateStandardTransferRequest from a dict
create_standard_transfer_request_from_dict = CreateStandardTransferRequest.from_dict(create_standard_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


