# Director


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**country_of_residence_iso3_code** | **str** |  | [optional] 

## Example

```python
from wise_api_client.models.director import Director

# TODO update the JSON string below
json = "{}"
# create an instance of Director from a JSON string
director_instance = Director.from_json(json)
# print the JSON string representation of the object
print(Director.to_json())

# convert the object into a dict
director_dict = director_instance.to_dict()
# create an instance of Director from a dict
director_from_dict = Director.from_dict(director_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


