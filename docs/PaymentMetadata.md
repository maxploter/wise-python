# PaymentMetadata

Metadata object used to pass additional information about the intended transfer, particularly for BRL transfers where transfer nature affects tax calculations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_nature** | **str** | Optional. Used to pass transfer nature for calculating proper tax amounts (IOF) for transfers to and from BRL. | [optional] 

## Example

```python
from wise_api_client.models.payment_metadata import PaymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMetadata from a JSON string
payment_metadata_instance = PaymentMetadata.from_json(json)
# print the JSON string representation of the object
print(PaymentMetadata.to_json())

# convert the object into a dict
payment_metadata_dict = payment_metadata_instance.to_dict()
# create an instance of PaymentMetadata from a dict
payment_metadata_from_dict = PaymentMetadata.from_dict(payment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


