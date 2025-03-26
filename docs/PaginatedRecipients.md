# PaginatedRecipients


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[Recipient]**](Recipient.md) |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from wise_api_client.models.paginated_recipients import PaginatedRecipients

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRecipients from a JSON string
paginated_recipients_instance = PaginatedRecipients.from_json(json)
# print the JSON string representation of the object
print(PaginatedRecipients.to_json())

# convert the object into a dict
paginated_recipients_dict = paginated_recipients_instance.to_dict()
# create an instance of PaginatedRecipients from a dict
paginated_recipients_from_dict = PaginatedRecipients.from_dict(paginated_recipients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


