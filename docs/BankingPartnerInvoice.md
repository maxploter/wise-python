# BankingPartnerInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor_name** | **str** |  | [optional] 
**delivery_mode** | **str** |  | [optional] 
**banking_partner_reference** | **str** |  | [optional] 
**banking_partner_name** | **str** |  | [optional] 
**mt103** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.banking_partner_invoice import BankingPartnerInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of BankingPartnerInvoice from a JSON string
banking_partner_invoice_instance = BankingPartnerInvoice.from_json(json)
# print the JSON string representation of the object
print(BankingPartnerInvoice.to_json())

# convert the object into a dict
banking_partner_invoice_dict = banking_partner_invoice_instance.to_dict()
# create an instance of BankingPartnerInvoice from a dict
banking_partner_invoice_from_dict = BankingPartnerInvoice.from_dict(banking_partner_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


