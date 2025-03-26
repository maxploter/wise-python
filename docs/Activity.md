# Activity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique activity identifier | 
**type** | [**ActivityType**](ActivityType.md) |  | 
**resource** | [**ActivityResource**](ActivityResource.md) |  | 
**title** | **str** | Title with custom formatting tags: &lt;strong&gt;, &lt;positive&gt;, &lt;negative&gt;, &lt;strikethrough&gt;  | 
**description** | **str** | Brief activity summary | [optional] 
**primary_amount** | **str** | Currency-formatted primary amount (e.g., \&quot;100 USD\&quot;) | [optional] 
**secondary_amount** | **str** | Currency-formatted secondary amount (optional) | [optional] 
**status** | [**ActivityStatus**](ActivityStatus.md) |  | 
**created_on** | **datetime** |  | 
**updated_on** | **datetime** |  | 

## Example

```python
from wise_api_client.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


