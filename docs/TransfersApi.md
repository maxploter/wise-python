# wise_api_client.TransfersApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_transfer_requirements**](TransfersApi.md#calculate_transfer_requirements) | **POST** /v1/transfer-requirements | Get transfer requirements
[**cancel_transfer**](TransfersApi.md#cancel_transfer) | **PUT** /v1/transfers/{transferId} | Cancel transfer
[**create_partner_licence_transfer**](TransfersApi.md#create_partner_licence_transfer) | **POST** /v1/profiles/{profileId}/partner-licence-transfers | Create partner license
[**create_third_party_transfer**](TransfersApi.md#create_third_party_transfer) | **POST** /v2/profiles/{profileId}/third-party-transfers | Create third-party transfer
[**create_transfer**](TransfersApi.md#create_transfer) | **POST** /v1/transfers | Create a standard transfer
[**fund_transfer**](TransfersApi.md#fund_transfer) | **POST** /v3/profiles/{profileId}/transfers/{transferId}/payments | Fund a transfer
[**get_banking_partner_invoice**](TransfersApi.md#get_banking_partner_invoice) | **GET** /v2/transfers/{transferId}/invoices/bankingpartner | Get banking partner invoice (v2)
[**get_noc_document**](TransfersApi.md#get_noc_document) | **GET** /v1/transfers/{transferId}/documents/noc | Get NOC document
[**get_third_party_transfer**](TransfersApi.md#get_third_party_transfer) | **GET** /v2/profiles/{profileId}/third-party-transfers/{transferId} | Get third-party transfer
[**get_transfer_by_id**](TransfersApi.md#get_transfer_by_id) | **GET** /v1/transfers/{transferId} | Get transfer by ID
[**get_transfer_receipt**](TransfersApi.md#get_transfer_receipt) | **GET** /v1/transfers/{transferId}/receipt.pdf | Get transfer receipt PDF
[**list_transfer_payments**](TransfersApi.md#list_transfer_payments) | **GET** /v1/transfers/{transferId}/payments | List transfer payments
[**list_transfers**](TransfersApi.md#list_transfers) | **GET** /v1/transfers | List transfers


# **calculate_transfer_requirements**
> List[TransferRequirementsResponseInner] calculate_transfer_requirements(transfer_requirements_request)

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
        api_response = api_instance.calculate_transfer_requirements(transfer_requirements_request)
        print("The response of TransfersApi->calculate_transfer_requirements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->calculate_transfer_requirements: %s\n" % e)
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

# **cancel_transfer**
> ListTransfers200ResponseInner cancel_transfer(transfer_id)

Cancel transfer

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.list_transfers200_response_inner import ListTransfers200ResponseInner
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
        api_response = api_instance.cancel_transfer(transfer_id)
        print("The response of TransfersApi->cancel_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->cancel_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**ListTransfers200ResponseInner**](ListTransfers200ResponseInner.md)

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

# **create_partner_licence_transfer**
> OriginatorTransfer create_partner_licence_transfer(profile_id, create_partner_licence_transfer_request)

Create partner license

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
        # Create partner license
        api_response = api_instance.create_partner_licence_transfer(profile_id, create_partner_licence_transfer_request)
        print("The response of TransfersApi->create_partner_licence_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->create_partner_licence_transfer: %s\n" % e)
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

# **create_third_party_transfer**
> OriginatorTransfer create_third_party_transfer(profile_id, create_third_party_transfer_request)

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
        api_response = api_instance.create_third_party_transfer(profile_id, create_third_party_transfer_request)
        print("The response of TransfersApi->create_third_party_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->create_third_party_transfer: %s\n" % e)
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

# **create_transfer**
> StandardTransfer create_transfer(create_standard_transfer_request)

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
        api_response = api_instance.create_transfer(create_standard_transfer_request)
        print("The response of TransfersApi->create_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->create_transfer: %s\n" % e)
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

# **fund_transfer**
> PaymentResponse fund_transfer(profile_id, transfer_id, payment_request)

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
        api_response = api_instance.fund_transfer(profile_id, transfer_id, payment_request)
        print("The response of TransfersApi->fund_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->fund_transfer: %s\n" % e)
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

# **get_banking_partner_invoice**
> BankingPartnerInvoice get_banking_partner_invoice(transfer_id)

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
        api_response = api_instance.get_banking_partner_invoice(transfer_id)
        print("The response of TransfersApi->get_banking_partner_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->get_banking_partner_invoice: %s\n" % e)
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

# **get_noc_document**
> bytearray get_noc_document(transfer_id)

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
        api_response = api_instance.get_noc_document(transfer_id)
        print("The response of TransfersApi->get_noc_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->get_noc_document: %s\n" % e)
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

# **get_third_party_transfer**
> OriginatorTransfer get_third_party_transfer(profile_id, transfer_id)

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
        api_response = api_instance.get_third_party_transfer(profile_id, transfer_id)
        print("The response of TransfersApi->get_third_party_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->get_third_party_transfer: %s\n" % e)
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

# **get_transfer_by_id**
> ListTransfers200ResponseInner get_transfer_by_id(transfer_id)

Get transfer by ID

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.list_transfers200_response_inner import ListTransfers200ResponseInner
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
        api_response = api_instance.get_transfer_by_id(transfer_id)
        print("The response of TransfersApi->get_transfer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->get_transfer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**|  | 

### Return type

[**ListTransfers200ResponseInner**](ListTransfers200ResponseInner.md)

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

# **get_transfer_receipt**
> bytearray get_transfer_receipt(transfer_id)

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
        api_response = api_instance.get_transfer_receipt(transfer_id)
        print("The response of TransfersApi->get_transfer_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->get_transfer_receipt: %s\n" % e)
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

# **list_transfer_payments**
> List[PaymentsListInner] list_transfer_payments(transfer_id)

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
        api_response = api_instance.list_transfer_payments(transfer_id)
        print("The response of TransfersApi->list_transfer_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->list_transfer_payments: %s\n" % e)
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

# **list_transfers**
> List[ListTransfers200ResponseInner] list_transfers(profile=profile, status=status, source_currency=source_currency, target_currency=target_currency, created_date_start=created_date_start, created_date_end=created_date_end, limit=limit, offset=offset)

List transfers

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.list_transfers200_response_inner import ListTransfers200ResponseInner
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
        api_response = api_instance.list_transfers(profile=profile, status=status, source_currency=source_currency, target_currency=target_currency, created_date_start=created_date_start, created_date_end=created_date_end, limit=limit, offset=offset)
        print("The response of TransfersApi->list_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->list_transfers: %s\n" % e)
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

[**List[ListTransfers200ResponseInner]**](ListTransfers200ResponseInner.md)

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

