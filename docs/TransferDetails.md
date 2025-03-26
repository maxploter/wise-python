# TransferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** |  | 
**transfer_purpose** | **str** |  | [optional] 
**transfer_purpose_sub_transfer_purpose** | **str** |  | [optional] 
**transfer_purpose_invoice_number** | **str** |  | [optional] 
**source_of_funds** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.transfer_details import TransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDetails from a JSON string
transfer_details_instance = TransferDetails.from_json(json)
# print the JSON string representation of the object
print(TransferDetails.to_json())

# convert the object into a dict
transfer_details_dict = transfer_details_instance.to_dict()
# create an instance of TransferDetails from a dict
transfer_details_from_dict = TransferDetails.from_dict(transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


