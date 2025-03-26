# ActivitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Pagination cursor for next page | [optional] 
**activities** | [**List[Activity]**](Activity.md) |  | [optional] 

## Example

```python
from wise_api_client.models.activities_response import ActivitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitiesResponse from a JSON string
activities_response_instance = ActivitiesResponse.from_json(json)
# print the JSON string representation of the object
print(ActivitiesResponse.to_json())

# convert the object into a dict
activities_response_dict = activities_response_instance.to_dict()
# create an instance of ActivitiesResponse from a dict
activities_response_from_dict = ActivitiesResponse.from_dict(activities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


