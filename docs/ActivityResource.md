# ActivityResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActivityResourceType**](ActivityResourceType.md) |  | 
**id** | **str** | Resource identifier | 

## Example

```python
from wise_api_client.models.activity_resource import ActivityResource

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityResource from a JSON string
activity_resource_instance = ActivityResource.from_json(json)
# print the JSON string representation of the object
print(ActivityResource.to_json())

# convert the object into a dict
activity_resource_dict = activity_resource_instance.to_dict()
# create an instance of ActivityResource from a dict
activity_resource_from_dict = ActivityResource.from_dict(activity_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


