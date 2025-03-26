# PricingConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**FeeConfiguration**](FeeConfiguration.md) |  | [optional] 

## Example

```python
from wise_api_client.models.pricing_configuration import PricingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PricingConfiguration from a JSON string
pricing_configuration_instance = PricingConfiguration.from_json(json)
# print the JSON string representation of the object
print(PricingConfiguration.to_json())

# convert the object into a dict
pricing_configuration_dict = pricing_configuration_instance.to_dict()
# create an instance of PricingConfiguration from a dict
pricing_configuration_from_dict = PricingConfiguration.from_dict(pricing_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


