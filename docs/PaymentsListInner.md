# PaymentsListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**method** | **str** |  | [optional] 
**pricing_variant** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**time_updated** | **datetime** |  | [optional] 

## Example

```python
from wise_api_client.models.payments_list_inner import PaymentsListInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsListInner from a JSON string
payments_list_inner_instance = PaymentsListInner.from_json(json)
# print the JSON string representation of the object
print(PaymentsListInner.to_json())

# convert the object into a dict
payments_list_inner_dict = payments_list_inner_instance.to_dict()
# create an instance of PaymentsListInner from a dict
payments_list_inner_from_dict = PaymentsListInner.from_dict(payments_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


