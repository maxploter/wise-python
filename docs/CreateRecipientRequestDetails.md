# CreateRecipientRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_type** | **str** |  | 
**sort_code** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 

## Example

```python
from wise_api_client.models.create_recipient_request_details import CreateRecipientRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipientRequestDetails from a JSON string
create_recipient_request_details_instance = CreateRecipientRequestDetails.from_json(json)
# print the JSON string representation of the object
print(CreateRecipientRequestDetails.to_json())

# convert the object into a dict
create_recipient_request_details_dict = create_recipient_request_details_instance.to_dict()
# create an instance of CreateRecipientRequestDetails from a dict
create_recipient_request_details_from_dict = CreateRecipientRequestDetails.from_dict(create_recipient_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


