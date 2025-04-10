# wise_api_client.RecipientsApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recipient_account**](RecipientsApi.md#create_recipient_account) | **POST** /v1/accounts | Create a recipient account
[**create_refund_recipient_account**](RecipientsApi.md#create_refund_recipient_account) | **POST** /v1/refund-accounts | Create a refund recipient account
[**deactivate_recipient_account**](RecipientsApi.md#deactivate_recipient_account) | **DELETE** /v2/accounts/{accountId} | Deactivate a recipient account
[**get_account_requirements**](RecipientsApi.md#get_account_requirements) | **GET** /v1/quotes/{quoteId}/account-requirements | Get account requirements for a quote
[**get_recipient_account_by_id**](RecipientsApi.md#get_recipient_account_by_id) | **GET** /v2/accounts/{accountId} | Get recipient account by ID
[**list_recipient_accounts**](RecipientsApi.md#list_recipient_accounts) | **GET** /v2/accounts | List recipient accounts


# **create_recipient_account**
> Recipient create_recipient_account(create_recipient_request)

Create a recipient account

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_recipient_request import CreateRecipientRequest
from wise_api_client.models.recipient import Recipient
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
    api_instance = wise_api_client.RecipientsApi(api_client)
    create_recipient_request = wise_api_client.CreateRecipientRequest() # CreateRecipientRequest | 

    try:
        # Create a recipient account
        api_response = api_instance.create_recipient_account(create_recipient_request)
        print("The response of RecipientsApi->create_recipient_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientsApi->create_recipient_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_recipient_request** | [**CreateRecipientRequest**](CreateRecipientRequest.md)|  | 

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created recipient account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund_recipient_account**
> Recipient create_refund_recipient_account(create_refund_recipient_account_request)

Create a refund recipient account

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_refund_recipient_account_request import CreateRefundRecipientAccountRequest
from wise_api_client.models.recipient import Recipient
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
    api_instance = wise_api_client.RecipientsApi(api_client)
    create_refund_recipient_account_request = wise_api_client.CreateRefundRecipientAccountRequest() # CreateRefundRecipientAccountRequest | 

    try:
        # Create a refund recipient account
        api_response = api_instance.create_refund_recipient_account(create_refund_recipient_account_request)
        print("The response of RecipientsApi->create_refund_recipient_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientsApi->create_refund_recipient_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_refund_recipient_account_request** | [**CreateRefundRecipientAccountRequest**](CreateRefundRecipientAccountRequest.md)|  | 

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created refund recipient |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_recipient_account**
> Recipient deactivate_recipient_account(account_id)

Deactivate a recipient account

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.recipient import Recipient
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
    api_instance = wise_api_client.RecipientsApi(api_client)
    account_id = 56 # int | 

    try:
        # Deactivate a recipient account
        api_response = api_instance.deactivate_recipient_account(account_id)
        print("The response of RecipientsApi->deactivate_recipient_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientsApi->deactivate_recipient_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deactivated recipient |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_requirements**
> List[AccountRequirementsInner] get_account_requirements(quote_id, originator_legal_entity_type=originator_legal_entity_type, accept_minor_version=accept_minor_version)

Get account requirements for a quote

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.account_requirements_inner import AccountRequirementsInner
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
    api_instance = wise_api_client.RecipientsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    originator_legal_entity_type = 'originator_legal_entity_type_example' # str |  (optional)
    accept_minor_version = '1' # str |  (optional) (default to '1')

    try:
        # Get account requirements for a quote
        api_response = api_instance.get_account_requirements(quote_id, originator_legal_entity_type=originator_legal_entity_type, accept_minor_version=accept_minor_version)
        print("The response of RecipientsApi->get_account_requirements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientsApi->get_account_requirements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **originator_legal_entity_type** | **str**|  | [optional] 
 **accept_minor_version** | **str**|  | [optional] [default to &#39;1&#39;]

### Return type

[**List[AccountRequirementsInner]**](AccountRequirementsInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account requirements |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_account_by_id**
> Recipient get_recipient_account_by_id(account_id)

Get recipient account by ID

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.recipient import Recipient
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
    api_instance = wise_api_client.RecipientsApi(api_client)
    account_id = 56 # int | 

    try:
        # Get recipient account by ID
        api_response = api_instance.get_recipient_account_by_id(account_id)
        print("The response of RecipientsApi->get_recipient_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientsApi->get_recipient_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recipient account details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recipient_accounts**
> PaginatedRecipients list_recipient_accounts(profile_id=profile_id, currency=currency, size=size, seek_position=seek_position)

List recipient accounts

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.paginated_recipients import PaginatedRecipients
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
    api_instance = wise_api_client.RecipientsApi(api_client)
    profile_id = 56 # int |  (optional)
    currency = 'currency_example' # str |  (optional)
    size = 56 # int |  (optional)
    seek_position = 56 # int |  (optional)

    try:
        # List recipient accounts
        api_response = api_instance.list_recipient_accounts(profile_id=profile_id, currency=currency, size=size, seek_position=seek_position)
        print("The response of RecipientsApi->list_recipient_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientsApi->list_recipient_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **size** | **int**|  | [optional] 
 **seek_position** | **int**|  | [optional] 

### Return type

[**PaginatedRecipients**](PaginatedRecipients.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of recipient accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

