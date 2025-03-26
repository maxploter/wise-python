# PaymentOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**estimated_delivery** | **datetime** |  | [optional] 
**formatted_estimated_delivery** | **str** |  | [optional] 
**fee** | [**FeeDetails**](FeeDetails.md) |  | [optional] 
**price** | [**PriceDetails**](PriceDetails.md) |  | [optional] 
**pay_in** | **str** |  | [optional] 
**pay_out** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.payment_option import PaymentOption

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOption from a JSON string
payment_option_instance = PaymentOption.from_json(json)
# print the JSON string representation of the object
print(PaymentOption.to_json())

# convert the object into a dict
payment_option_dict = payment_option_instance.to_dict()
# create an instance of PaymentOption from a dict
payment_option_from_dict = PaymentOption.from_dict(payment_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


