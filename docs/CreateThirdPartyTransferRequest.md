# CreateThirdPartyTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_account** | **int** |  | 
**quote** | **str** |  | 
**original_transfer_id** | **str** |  | 
**details** | [**TransferDetails**](TransferDetails.md) |  | [optional] 
**originator** | [**Originator**](Originator.md) |  | 

## Example

```python
from wise_api_client.models.create_third_party_transfer_request import CreateThirdPartyTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThirdPartyTransferRequest from a JSON string
create_third_party_transfer_request_instance = CreateThirdPartyTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateThirdPartyTransferRequest.to_json())

# convert the object into a dict
create_third_party_transfer_request_dict = create_third_party_transfer_request_instance.to_dict()
# create an instance of CreateThirdPartyTransferRequest from a dict
create_third_party_transfer_request_from_dict = CreateThirdPartyTransferRequest.from_dict(create_third_party_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


