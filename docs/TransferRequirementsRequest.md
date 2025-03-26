# TransferRequirementsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_account** | **int** |  | 
**quote_uuid** | **str** |  | 
**details** | **object** |  | [optional] 
**customer_transaction_id** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.transfer_requirements_request import TransferRequirementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequirementsRequest from a JSON string
transfer_requirements_request_instance = TransferRequirementsRequest.from_json(json)
# print the JSON string representation of the object
print(TransferRequirementsRequest.to_json())

# convert the object into a dict
transfer_requirements_request_dict = transfer_requirements_request_instance.to_dict()
# create an instance of TransferRequirementsRequest from a dict
transfer_requirements_request_from_dict = TransferRequirementsRequest.from_dict(transfer_requirements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


