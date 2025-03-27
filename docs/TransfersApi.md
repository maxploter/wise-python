# wise_api_client.TransfersApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_profiles_profile_id_partner_licence_transfers_post**](TransfersApi.md#v1_profiles_profile_id_partner_licence_transfers_post) | **POST** /v1/profiles/{profileId}/partner-licence-transfers | Create partner license transfer
[**v1_transfer_requirements_post**](TransfersApi.md#v1_transfer_requirements_post) | **POST** /v1/transfer-requirements | Get transfer requirements
[**v1_transfers_get**](TransfersApi.md#v1_transfers_get) | **GET** /v1/transfers | List transfers
[**v1_transfers_post**](TransfersApi.md#v1_transfers_post) | **POST** /v1/transfers | Create a standard transfer
[**v1_transfers_transfer_id_documents_noc_get**](TransfersApi.md#v1_transfers_transfer_id_documents_noc_get) | **GET** /v1/transfers/{transferId}/documents/noc | Get NOC document
[**v1_transfers_transfer_id_get**](TransfersApi.md#v1_transfers_transfer_id_get) | **GET** /v1/transfers/{transferId} | Get transfer by ID
[**v1_transfers_transfer_id_invoices_bankingpartner_get**](TransfersApi.md#v1_transfers_transfer_id_invoices_bankingpartner_get) | **GET** /v1/transfers/{transferId}/invoices/bankingpartner | Get banking partner invoice (v1)
[**v1_transfers_transfer_id_payments_get**](TransfersApi.md#v1_transfers_transfer_id_payments_get) | **GET** /v1/transfers/{transferId}/payments | List transfer payments
[**v1_transfers_transfer_id_put**](TransfersApi.md#v1_transfers_transfer_id_put) | **PUT** /v1/transfers/{transferId} | Cancel transfer
[**v1_transfers_transfer_id_receipt_pdf_get**](TransfersApi.md#v1_transfers_transfer_id_receipt_pdf_get) | **GET** /v1/transfers/{transferId}/receipt.pdf | Get transfer receipt PDF
[**v2_profiles_profile_id_third_party_transfers_post**](TransfersApi.md#v2_profiles_profile_id_third_party_transfers_post) | **POST** /v2/profiles/{profileId}/third-party-transfers | Create third-party transfer
[**v2_profiles_profile_id_third_party_transfers_transfer_id_get**](TransfersApi.md#v2_profiles_profile_id_third_party_transfers_transfer_id_get) | **GET** /v2/profiles/{profileId}/third-party-transfers/{transferId} | Get third-party transfer
[**v2_transfers_transfer_id_invoices_bankingpartner_get**](TransfersApi.md#v2_transfers_transfer_id_invoices_bankingpartner_get) | **GET** /v2/transfers/{transferId}/invoices/bankingpartner | Get banking partner invoice (v2)
[**v3_profiles_profile_id_transfers_transfer_id_payments_post**](TransfersApi.md#v3_profiles_profile_id_transfers_transfer_id_payments_post) | **POST** /v3/profiles/{profileId}/transfers/{transferId}/payments | Fund a transfer


# **v1_profiles_profile_id_partner_licence_transfers_post**
> OriginatorTransfer v1_profiles_profile_id_partner_licence_transfers_post(profile_id, create_partner_licence_transfer_request)

Create partner license transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_partner_licence_transfer_request import CreatePartnerLicenceTransferRequest
from wise_api_client.models.originator_transfer import OriginatorTransfer
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    profile_id = 'profile_id_example' # str | 
    create_partner_licence_transfer_request = wise_api_client.CreatePartnerLicenceTransferRequest() # CreatePartnerLicenceTransferRequest | 

    try:
        # Create partner license transfer
        api_response = api_instance.v1_profiles_profile_id_partner_licence_transfers_post(profile_id, create_partner_licence_transfer_request)
        print("The response of TransfersApi->v1_profiles_profile_id_partner_licence_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_profiles_profile_id_partner_licence_transfers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **create_partner_licence_transfer_request** | [**CreatePartnerLicenceTransferRequest**](CreatePartnerLicenceTransferRequest.md)|  | 

### Return type

[**OriginatorTransfer**](OriginatorTransfer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfer_requirements_post**
> List[TransferRequirementsResponseInner] v1_transfer_requirements_post(transfer_requirements_request)

Get transfer requirements

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.transfer_requirements_request import TransferRequirementsRequest
from wise_api_client.models.transfer_requirements_response_inner import TransferRequirementsResponseInner
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_requirements_request = wise_api_client.TransferRequirementsRequest() # TransferRequirementsRequest | 

    try:
        # Get transfer requirements
        api_response = api_instance.v1_transfer_requirements_post(transfer_requirements_request)
        print("The response of TransfersApi->v1_transfer_requirements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfer_requirements_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_requirements_request** | [**TransferRequirementsRequest**](TransferRequirementsRequest.md)|  | 

### Return type

[**List[TransferRequirementsResponseInner]**](TransferRequirementsResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer requirements |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_get**
> List[V1TransfersGet200ResponseInner] v1_transfers_get(profile=profile, status=status, source_currency=source_currency, target_currency=target_currency, created_date_start=created_date_start, created_date_end=created_date_end, limit=limit, offset=offset)

List transfers

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.v1_transfers_get200_response_inner import V1TransfersGet200ResponseInner
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    profile = 56 # int |  (optional)
    status = 'status_example' # str |  (optional)
    source_currency = 'source_currency_example' # str |  (optional)
    target_currency = 'target_currency_example' # str |  (optional)
    created_date_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_date_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List transfers
        api_response = api_instance.v1_transfers_get(profile=profile, status=status, source_currency=source_currency, target_currency=target_currency, created_date_start=created_date_start, created_date_end=created_date_end, limit=limit, offset=offset)
        print("The response of TransfersApi->v1_transfers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **source_currency** | **str**|  | [optional] 
 **target_currency** | **str**|  | [optional] 
 **created_date_start** | **datetime**|  | [optional] 
 **created_date_end** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[V1TransfersGet200ResponseInner]**](V1TransfersGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of transfers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_post**
> StandardTransfer v1_transfers_post(create_standard_transfer_request)

Create a standard transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_standard_transfer_request import CreateStandardTransferRequest
from wise_api_client.models.standard_transfer import StandardTransfer
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    create_standard_transfer_request = wise_api_client.CreateStandardTransferRequest() # CreateStandardTransferRequest | 

    try:
        # Create a standard transfer
        api_response = api_instance.v1_transfers_post(create_standard_transfer_request)
        print("The response of TransfersApi->v1_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_standard_transfer_request** | [**CreateStandardTransferRequest**](CreateStandardTransferRequest.md)|  | 

### Return type

[**StandardTransfer**](StandardTransfer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_transfer_id_documents_noc_get**
> bytearray v1_transfers_transfer_id_documents_noc_get(transfer_id)

Get NOC document

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get NOC document
        api_response = api_instance.v1_transfers_transfer_id_documents_noc_get(transfer_id)
        print("The response of TransfersApi->v1_transfers_transfer_id_documents_noc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_transfer_id_documents_noc_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NOC PDF document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_transfer_id_get**
> V1TransfersGet200ResponseInner v1_transfers_transfer_id_get(transfer_id)

Get transfer by ID

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.v1_transfers_get200_response_inner import V1TransfersGet200ResponseInner
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get transfer by ID
        api_response = api_instance.v1_transfers_transfer_id_get(transfer_id)
        print("The response of TransfersApi->v1_transfers_transfer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_transfer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**V1TransfersGet200ResponseInner**](V1TransfersGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_transfer_id_invoices_bankingpartner_get**
> BankingPartnerInvoice v1_transfers_transfer_id_invoices_bankingpartner_get(transfer_id)

Get banking partner invoice (v1)

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.banking_partner_invoice import BankingPartnerInvoice
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get banking partner invoice (v1)
        api_response = api_instance.v1_transfers_transfer_id_invoices_bankingpartner_get(transfer_id)
        print("The response of TransfersApi->v1_transfers_transfer_id_invoices_bankingpartner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_transfer_id_invoices_bankingpartner_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**BankingPartnerInvoice**](BankingPartnerInvoice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Banking partner invoice details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_transfer_id_payments_get**
> List[PaymentsListInner] v1_transfers_transfer_id_payments_get(transfer_id)

List transfer payments

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.payments_list_inner import PaymentsListInner
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # List transfer payments
        api_response = api_instance.v1_transfers_transfer_id_payments_get(transfer_id)
        print("The response of TransfersApi->v1_transfers_transfer_id_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_transfer_id_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**List[PaymentsListInner]**](PaymentsListInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_transfer_id_put**
> V1TransfersGet200ResponseInner v1_transfers_transfer_id_put(transfer_id)

Cancel transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.v1_transfers_get200_response_inner import V1TransfersGet200ResponseInner
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Cancel transfer
        api_response = api_instance.v1_transfers_transfer_id_put(transfer_id)
        print("The response of TransfersApi->v1_transfers_transfer_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_transfer_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**V1TransfersGet200ResponseInner**](V1TransfersGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer cancelled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transfers_transfer_id_receipt_pdf_get**
> bytearray v1_transfers_transfer_id_receipt_pdf_get(transfer_id)

Get transfer receipt PDF

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get transfer receipt PDF
        api_response = api_instance.v1_transfers_transfer_id_receipt_pdf_get(transfer_id)
        print("The response of TransfersApi->v1_transfers_transfer_id_receipt_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v1_transfers_transfer_id_receipt_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF receipt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_profiles_profile_id_third_party_transfers_post**
> OriginatorTransfer v2_profiles_profile_id_third_party_transfers_post(profile_id, create_third_party_transfer_request)

Create third-party transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_third_party_transfer_request import CreateThirdPartyTransferRequest
from wise_api_client.models.originator_transfer import OriginatorTransfer
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    profile_id = 'profile_id_example' # str | 
    create_third_party_transfer_request = wise_api_client.CreateThirdPartyTransferRequest() # CreateThirdPartyTransferRequest | 

    try:
        # Create third-party transfer
        api_response = api_instance.v2_profiles_profile_id_third_party_transfers_post(profile_id, create_third_party_transfer_request)
        print("The response of TransfersApi->v2_profiles_profile_id_third_party_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v2_profiles_profile_id_third_party_transfers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **create_third_party_transfer_request** | [**CreateThirdPartyTransferRequest**](CreateThirdPartyTransferRequest.md)|  | 

### Return type

[**OriginatorTransfer**](OriginatorTransfer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_profiles_profile_id_third_party_transfers_transfer_id_get**
> OriginatorTransfer v2_profiles_profile_id_third_party_transfers_transfer_id_get(profile_id, transfer_id)

Get third-party transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.originator_transfer import OriginatorTransfer
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    profile_id = 'profile_id_example' # str | 
    transfer_id = 56 # int | 

    try:
        # Get third-party transfer
        api_response = api_instance.v2_profiles_profile_id_third_party_transfers_transfer_id_get(profile_id, transfer_id)
        print("The response of TransfersApi->v2_profiles_profile_id_third_party_transfers_transfer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v2_profiles_profile_id_third_party_transfers_transfer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **transfer_id** | **int**|  | 

### Return type

[**OriginatorTransfer**](OriginatorTransfer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_transfers_transfer_id_invoices_bankingpartner_get**
> BankingPartnerInvoice v2_transfers_transfer_id_invoices_bankingpartner_get(transfer_id)

Get banking partner invoice (v2)

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.banking_partner_invoice import BankingPartnerInvoice
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get banking partner invoice (v2)
        api_response = api_instance.v2_transfers_transfer_id_invoices_bankingpartner_get(transfer_id)
        print("The response of TransfersApi->v2_transfers_transfer_id_invoices_bankingpartner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v2_transfers_transfer_id_invoices_bankingpartner_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**BankingPartnerInvoice**](BankingPartnerInvoice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Banking partner invoice details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_profiles_profile_id_transfers_transfer_id_payments_post**
> PaymentResponse v3_profiles_profile_id_transfers_transfer_id_payments_post(profile_id, transfer_id, payment_request)

Fund a transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.payment_request import PaymentRequest
from wise_api_client.models.payment_response import PaymentResponse
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = wise_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.TransfersApi(api_client)
    profile_id = 'profile_id_example' # str | 
    transfer_id = 56 # int | 
    payment_request = wise_api_client.PaymentRequest() # PaymentRequest | 

    try:
        # Fund a transfer
        api_response = api_instance.v3_profiles_profile_id_transfers_transfer_id_payments_post(profile_id, transfer_id, payment_request)
        print("The response of TransfersApi->v3_profiles_profile_id_transfers_transfer_id_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->v3_profiles_profile_id_transfers_transfer_id_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **transfer_id** | **int**|  | 
 **payment_request** | [**PaymentRequest**](PaymentRequest.md)|  | 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

