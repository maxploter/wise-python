# PaginatedRecipientsSort

Sort information for the results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 
**sorted** | **bool** |  | [optional] 
**unsorted** | **bool** |  | [optional] 

## Example

```python
from wise_api_client.models.paginated_recipients_sort import PaginatedRecipientsSort

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRecipientsSort from a JSON string
paginated_recipients_sort_instance = PaginatedRecipientsSort.from_json(json)
# print the JSON string representation of the object
print(PaginatedRecipientsSort.to_json())

# convert the object into a dict
paginated_recipients_sort_dict = paginated_recipients_sort_instance.to_dict()
# create an instance of PaginatedRecipientsSort from a dict
paginated_recipients_sort_from_dict = PaginatedRecipientsSort.from_dict(paginated_recipients_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


