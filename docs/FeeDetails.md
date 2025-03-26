# FeeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 

## Example

```python
from wise_api_client.models.fee_details import FeeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FeeDetails from a JSON string
fee_details_instance = FeeDetails.from_json(json)
# print the JSON string representation of the object
print(FeeDetails.to_json())

# convert the object into a dict
fee_details_dict = fee_details_instance.to_dict()
# create an instance of FeeDetails from a dict
fee_details_from_dict = FeeDetails.from_dict(fee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


