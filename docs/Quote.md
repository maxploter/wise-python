# Quote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID format quote ID | [optional] 
**source_currency** | **str** |  | [optional] 
**target_currency** | **str** |  | [optional] 
**source_amount** | **float** |  | [optional] 
**target_amount** | **float** |  | [optional] 
**pay_out** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**profile** | **int** |  | [optional] 
**rate_type** | **str** |  | [optional] 
**rate_expiration_time** | **datetime** |  | [optional] 
**provided_amount_type** | **str** |  | [optional] 
**pricing_configuration** | [**PricingConfiguration**](PricingConfiguration.md) |  | [optional] 
**payment_options** | [**List[PaymentOption]**](PaymentOption.md) |  | [optional] 
**status** | **str** |  | [optional] 
**expiration_time** | **datetime** |  | [optional] 
**notices** | [**List[Notice]**](Notice.md) |  | [optional] 

## Example

```python
from wise_api_client.models.quote import Quote

# TODO update the JSON string below
json = "{}"
# create an instance of Quote from a JSON string
quote_instance = Quote.from_json(json)
# print the JSON string representation of the object
print(Quote.to_json())

# convert the object into a dict
quote_dict = quote_instance.to_dict()
# create an instance of Quote from a dict
quote_from_dict = Quote.from_dict(quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


