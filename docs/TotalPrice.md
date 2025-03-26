# TotalPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from wise_api_client.models.total_price import TotalPrice

# TODO update the JSON string below
json = "{}"
# create an instance of TotalPrice from a JSON string
total_price_instance = TotalPrice.from_json(json)
# print the JSON string representation of the object
print(TotalPrice.to_json())

# convert the object into a dict
total_price_dict = total_price_instance.to_dict()
# create an instance of TotalPrice from a dict
total_price_from_dict = TotalPrice.from_dict(total_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


