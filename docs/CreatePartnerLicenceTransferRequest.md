# CreatePartnerLicenceTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account** | **int** |  | [optional] 
**target_account** | **int** |  | 
**quote** | **str** |  | 
**customer_transaction_id** | **str** |  | 
**details** | [**TransferDetails**](TransferDetails.md) |  | [optional] 
**originator** | [**Originator**](Originator.md) |  | 

## Example

```python
from wise_api_client.models.create_partner_licence_transfer_request import CreatePartnerLicenceTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePartnerLicenceTransferRequest from a JSON string
create_partner_licence_transfer_request_instance = CreatePartnerLicenceTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePartnerLicenceTransferRequest.to_json())

# convert the object into a dict
create_partner_licence_transfer_request_dict = create_partner_licence_transfer_request_instance.to_dict()
# create an instance of CreatePartnerLicenceTransferRequest from a dict
create_partner_licence_transfer_request_from_dict = CreatePartnerLicenceTransferRequest.from_dict(create_partner_licence_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


