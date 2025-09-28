# FeeConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The fee calculation method. OVERRIDE means the fee is a fixed amount regardless of the transfer amount. | 
**variable** | **float** |  | 
**fixed** | **float** |  | 

## Example

```python
from wise_api_client.models.fee_configuration import FeeConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of FeeConfiguration from a JSON string
fee_configuration_instance = FeeConfiguration.from_json(json)
# print the JSON string representation of the object
print(FeeConfiguration.to_json())

# convert the object into a dict
fee_configuration_dict = fee_configuration_instance.to_dict()
# create an instance of FeeConfiguration from a dict
fee_configuration_from_dict = FeeConfiguration.from_dict(fee_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


