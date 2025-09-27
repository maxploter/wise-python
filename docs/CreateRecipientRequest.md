# CreateRecipientRequest

Beyond the fixed fields, this object accepts a dynamic set of properties based on the response from the `/v1/quotes/{quoteId}/account-requirements` endpoint. This can include simple fields or nested objects like 'details' and 'address' when required for a specific currency route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | ISO 4217 three-letter currency code | 
**type** | **str** | The type of recipient account, determined from the account requirements. | 
**profile** | **int** | A unique profile identifier | 
**account_holder_name** | **str** | The recipient&#39;s full name. | 
**owned_by_customer** | **bool** | Whether this account is owned by the sending user. | [optional] 

## Example

```python
from wise_api_client.models.create_recipient_request import CreateRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipientRequest from a JSON string
create_recipient_request_instance = CreateRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRecipientRequest.to_json())

# convert the object into a dict
create_recipient_request_dict = create_recipient_request_instance.to_dict()
# create an instance of CreateRecipientRequest from a dict
create_recipient_request_from_dict = CreateRecipientRequest.from_dict(create_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


