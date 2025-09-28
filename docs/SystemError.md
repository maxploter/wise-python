# SystemError

System errors are not typically caused by the end user and often require involvement to remedy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error code identifier | 
**error_description** | **str** | Error description or identifier | 

## Example

```python
from wise_api_client.models.system_error import SystemError

# TODO update the JSON string below
json = "{}"
# create an instance of SystemError from a JSON string
system_error_instance = SystemError.from_json(json)
# print the JSON string representation of the object
print(SystemError.to_json())

# convert the object into a dict
system_error_dict = system_error_instance.to_dict()
# create an instance of SystemError from a dict
system_error_from_dict = SystemError.from_dict(system_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


