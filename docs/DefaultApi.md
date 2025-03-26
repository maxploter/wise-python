# wise_api_client.DefaultApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_profile**](DefaultApi.md#create_business_profile) | **POST** /v2/profiles/business-profile | Create a business profile
[**create_personal_profile**](DefaultApi.md#create_personal_profile) | **POST** /v2/profiles/personal-profile | Create a personal profile
[**profiles_profile_id_quotes_post**](DefaultApi.md#profiles_profile_id_quotes_post) | **POST** /profiles/{profileId}/quotes | Create an authenticated quote
[**profiles_profile_id_quotes_quote_id_get**](DefaultApi.md#profiles_profile_id_quotes_quote_id_get) | **GET** /profiles/{profileId}/quotes/{quoteId} | Retrieve a quote by ID
[**profiles_profile_id_quotes_quote_id_patch**](DefaultApi.md#profiles_profile_id_quotes_quote_id_patch) | **PATCH** /profiles/{profileId}/quotes/{quoteId} | Update a quote
[**quotes_post**](DefaultApi.md#quotes_post) | **POST** /quotes | Create an unauthenticated quote
[**v1_accounts_post**](DefaultApi.md#v1_accounts_post) | **POST** /v1/accounts | Create a recipient account
[**v1_profiles_profile_id_directors_get**](DefaultApi.md#v1_profiles_profile_id_directors_get) | **GET** /v1/profiles/{profileId}/directors | List directors
[**v1_profiles_profile_id_directors_post**](DefaultApi.md#v1_profiles_profile_id_directors_post) | **POST** /v1/profiles/{profileId}/directors | Add directors
[**v1_profiles_profile_id_directors_put**](DefaultApi.md#v1_profiles_profile_id_directors_put) | **PUT** /v1/profiles/{profileId}/directors | Update directors
[**v1_profiles_profile_id_partner_licence_transfers_post**](DefaultApi.md#v1_profiles_profile_id_partner_licence_transfers_post) | **POST** /v1/profiles/{profileId}/partner-licence-transfers | Create partner license transfer
[**v1_profiles_profile_id_verification_documents_post**](DefaultApi.md#v1_profiles_profile_id_verification_documents_post) | **POST** /v1/profiles/{profileId}/verification-documents | Create identification document
[**v1_quotes_quote_id_account_requirements_get**](DefaultApi.md#v1_quotes_quote_id_account_requirements_get) | **GET** /v1/quotes/{quoteId}/account-requirements | Get account requirements for a quote
[**v1_refund_accounts_post**](DefaultApi.md#v1_refund_accounts_post) | **POST** /v1/refund-accounts | Create a refund recipient account
[**v1_transfer_requirements_post**](DefaultApi.md#v1_transfer_requirements_post) | **POST** /v1/transfer-requirements | Get transfer requirements
[**v1_transfers_get**](DefaultApi.md#v1_transfers_get) | **GET** /v1/transfers | List transfers
[**v1_transfers_post**](DefaultApi.md#v1_transfers_post) | **POST** /v1/transfers | Create a standard transfer
[**v1_transfers_transfer_id_documents_noc_get**](DefaultApi.md#v1_transfers_transfer_id_documents_noc_get) | **GET** /v1/transfers/{transferId}/documents/noc | Get NOC document
[**v1_transfers_transfer_id_get**](DefaultApi.md#v1_transfers_transfer_id_get) | **GET** /v1/transfers/{transferId} | Get transfer by ID
[**v1_transfers_transfer_id_invoices_bankingpartner_get**](DefaultApi.md#v1_transfers_transfer_id_invoices_bankingpartner_get) | **GET** /v1/transfers/{transferId}/invoices/bankingpartner | Get banking partner invoice (v1)
[**v1_transfers_transfer_id_payments_get**](DefaultApi.md#v1_transfers_transfer_id_payments_get) | **GET** /v1/transfers/{transferId}/payments | List transfer payments
[**v1_transfers_transfer_id_put**](DefaultApi.md#v1_transfers_transfer_id_put) | **PUT** /v1/transfers/{transferId} | Cancel transfer
[**v1_transfers_transfer_id_receipt_pdf_get**](DefaultApi.md#v1_transfers_transfer_id_receipt_pdf_get) | **GET** /v1/transfers/{transferId}/receipt.pdf | Get transfer receipt PDF
[**v2_accounts_account_id_delete**](DefaultApi.md#v2_accounts_account_id_delete) | **DELETE** /v2/accounts/{accountId} | Deactivate a recipient account
[**v2_accounts_account_id_get**](DefaultApi.md#v2_accounts_account_id_get) | **GET** /v2/accounts/{accountId} | Get recipient account by ID
[**v2_accounts_get**](DefaultApi.md#v2_accounts_get) | **GET** /v2/accounts | List recipient accounts
[**v2_profiles_get**](DefaultApi.md#v2_profiles_get) | **GET** /v2/profiles | List profiles for a user account
[**v2_profiles_profile_id_business_profile_put**](DefaultApi.md#v2_profiles_profile_id_business_profile_put) | **PUT** /v2/profiles/{profileId}/business-profile | Update a business profile
[**v2_profiles_profile_id_get**](DefaultApi.md#v2_profiles_profile_id_get) | **GET** /v2/profiles/{profileId} | Retrieve a profile by ID
[**v2_profiles_profile_id_personal_profile_put**](DefaultApi.md#v2_profiles_profile_id_personal_profile_put) | **PUT** /v2/profiles/{profileId}/personal-profile | Update a personal profile
[**v2_profiles_profile_id_third_party_transfers_post**](DefaultApi.md#v2_profiles_profile_id_third_party_transfers_post) | **POST** /v2/profiles/{profileId}/third-party-transfers | Create third-party transfer
[**v2_profiles_profile_id_third_party_transfers_transfer_id_get**](DefaultApi.md#v2_profiles_profile_id_third_party_transfers_transfer_id_get) | **GET** /v2/profiles/{profileId}/third-party-transfers/{transferId} | Get third-party transfer
[**v2_transfers_transfer_id_invoices_bankingpartner_get**](DefaultApi.md#v2_transfers_transfer_id_invoices_bankingpartner_get) | **GET** /v2/transfers/{transferId}/invoices/bankingpartner | Get banking partner invoice (v2)
[**v3_profiles_profile_id_transfers_transfer_id_payments_post**](DefaultApi.md#v3_profiles_profile_id_transfers_transfer_id_payments_post) | **POST** /v3/profiles/{profileId}/transfers/{transferId}/payments | Fund a transfer
[**v3_profiles_profile_id_verification_status_bank_transfer_post**](DefaultApi.md#v3_profiles_profile_id_verification_status_bank_transfer_post) | **POST** /v3/profiles/{profileId}/verification-status/bank-transfer | Check verification status


# **create_business_profile**
> BusinessProfile create_business_profile(create_business_profile_request)

Create a business profile

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.business_profile import BusinessProfile
from wise_api_client.models.create_business_profile_request import CreateBusinessProfileRequest
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
    api_instance = wise_api_client.DefaultApi(api_client)
    create_business_profile_request = wise_api_client.CreateBusinessProfileRequest() # CreateBusinessProfileRequest | 

    try:
        # Create a business profile
        api_response = api_instance.create_business_profile(create_business_profile_request)
        print("The response of DefaultApi->create_business_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_business_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_business_profile_request** | [**CreateBusinessProfileRequest**](CreateBusinessProfileRequest.md)|  | 

### Return type

[**BusinessProfile**](BusinessProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Business profile created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_personal_profile**
> PersonalProfile create_personal_profile(create_personal_profile_request)

Create a personal profile

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_personal_profile_request import CreatePersonalProfileRequest
from wise_api_client.models.personal_profile import PersonalProfile
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
    api_instance = wise_api_client.DefaultApi(api_client)
    create_personal_profile_request = wise_api_client.CreatePersonalProfileRequest() # CreatePersonalProfileRequest | 

    try:
        # Create a personal profile
        api_response = api_instance.create_personal_profile(create_personal_profile_request)
        print("The response of DefaultApi->create_personal_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_personal_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_personal_profile_request** | [**CreatePersonalProfileRequest**](CreatePersonalProfileRequest.md)|  | 

### Return type

[**PersonalProfile**](PersonalProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Personal profile created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_profile_id_quotes_post**
> Quote profiles_profile_id_quotes_post(profile_id, create_authenticated_quote_request)

Create an authenticated quote

Creates a quote associated with a profile. Requires user authentication.

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_authenticated_quote_request import CreateAuthenticatedQuoteRequest
from wise_api_client.models.quote import Quote
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    create_authenticated_quote_request = wise_api_client.CreateAuthenticatedQuoteRequest() # CreateAuthenticatedQuoteRequest | 

    try:
        # Create an authenticated quote
        api_response = api_instance.profiles_profile_id_quotes_post(profile_id, create_authenticated_quote_request)
        print("The response of DefaultApi->profiles_profile_id_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profiles_profile_id_quotes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **create_authenticated_quote_request** | [**CreateAuthenticatedQuoteRequest**](CreateAuthenticatedQuoteRequest.md)|  | 

### Return type

[**Quote**](Quote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created authenticated quote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_profile_id_quotes_quote_id_get**
> Quote profiles_profile_id_quotes_quote_id_get(profile_id, quote_id)

Retrieve a quote by ID

Retrieves a quote by its ID. Expired quotes are available for ~48 hours.

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.quote import Quote
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Retrieve a quote by ID
        api_response = api_instance.profiles_profile_id_quotes_quote_id_get(profile_id, quote_id)
        print("The response of DefaultApi->profiles_profile_id_quotes_quote_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profiles_profile_id_quotes_quote_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **quote_id** | **str**|  | 

### Return type

[**Quote**](Quote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved quote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_profile_id_quotes_quote_id_patch**
> Quote profiles_profile_id_quotes_quote_id_patch(profile_id, quote_id, update_quote_request)

Update a quote

Updates a quote with recipient information or payment metadata.

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.quote import Quote
from wise_api_client.models.update_quote_request import UpdateQuoteRequest
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    quote_id = 'quote_id_example' # str | 
    update_quote_request = wise_api_client.UpdateQuoteRequest() # UpdateQuoteRequest | 

    try:
        # Update a quote
        api_response = api_instance.profiles_profile_id_quotes_quote_id_patch(profile_id, quote_id, update_quote_request)
        print("The response of DefaultApi->profiles_profile_id_quotes_quote_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profiles_profile_id_quotes_quote_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **quote_id** | **str**|  | 
 **update_quote_request** | [**UpdateQuoteRequest**](UpdateQuoteRequest.md)|  | 

### Return type

[**Quote**](Quote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated quote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotes_post**
> Quote quotes_post(create_unauthenticated_quote_request)

Create an unauthenticated quote

Creates an example quote for illustration purposes. The returned quote cannot be used to create transfers.

### Example


```python
import wise_api_client
from wise_api_client.models.create_unauthenticated_quote_request import CreateUnauthenticatedQuoteRequest
from wise_api_client.models.quote import Quote
from wise_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sandbox.transferwise.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = wise_api_client.Configuration(
    host = "https://api.sandbox.transferwise.tech"
)


# Enter a context with an instance of the API client
with wise_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wise_api_client.DefaultApi(api_client)
    create_unauthenticated_quote_request = wise_api_client.CreateUnauthenticatedQuoteRequest() # CreateUnauthenticatedQuoteRequest | 

    try:
        # Create an unauthenticated quote
        api_response = api_instance.quotes_post(create_unauthenticated_quote_request)
        print("The response of DefaultApi->quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->quotes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_unauthenticated_quote_request** | [**CreateUnauthenticatedQuoteRequest**](CreateUnauthenticatedQuoteRequest.md)|  | 

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created unauthenticated quote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_accounts_post**
> Recipient v1_accounts_post(create_recipient_request)

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
    api_instance = wise_api_client.DefaultApi(api_client)
    create_recipient_request = wise_api_client.CreateRecipientRequest() # CreateRecipientRequest | 

    try:
        # Create a recipient account
        api_response = api_instance.v1_accounts_post(create_recipient_request)
        print("The response of DefaultApi->v1_accounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_accounts_post: %s\n" % e)
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

# **v1_profiles_profile_id_directors_get**
> List[Director] v1_profiles_profile_id_directors_get(profile_id)

List directors

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.director import Director
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 

    try:
        # List directors
        api_response = api_instance.v1_profiles_profile_id_directors_get(profile_id)
        print("The response of DefaultApi->v1_profiles_profile_id_directors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_profiles_profile_id_directors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 

### Return type

[**List[Director]**](Director.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of directors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_profiles_profile_id_directors_post**
> List[Director] v1_profiles_profile_id_directors_post(profile_id, director=director)

Add directors

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.director import Director
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    director = [wise_api_client.Director()] # List[Director] |  (optional)

    try:
        # Add directors
        api_response = api_instance.v1_profiles_profile_id_directors_post(profile_id, director=director)
        print("The response of DefaultApi->v1_profiles_profile_id_directors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_profiles_profile_id_directors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **director** | [**List[Director]**](Director.md)|  | [optional] 

### Return type

[**List[Director]**](Director.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Directors added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_profiles_profile_id_directors_put**
> List[Director] v1_profiles_profile_id_directors_put(profile_id, director=director)

Update directors

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.director import Director
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    director = [wise_api_client.Director()] # List[Director] |  (optional)

    try:
        # Update directors
        api_response = api_instance.v1_profiles_profile_id_directors_put(profile_id, director=director)
        print("The response of DefaultApi->v1_profiles_profile_id_directors_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_profiles_profile_id_directors_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **director** | [**List[Director]**](Director.md)|  | [optional] 

### Return type

[**List[Director]**](Director.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Directors updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 
    create_partner_licence_transfer_request = wise_api_client.CreatePartnerLicenceTransferRequest() # CreatePartnerLicenceTransferRequest | 

    try:
        # Create partner license transfer
        api_response = api_instance.v1_profiles_profile_id_partner_licence_transfers_post(profile_id, create_partner_licence_transfer_request)
        print("The response of DefaultApi->v1_profiles_profile_id_partner_licence_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_profiles_profile_id_partner_licence_transfers_post: %s\n" % e)
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

# **v1_profiles_profile_id_verification_documents_post**
> Error v1_profiles_profile_id_verification_documents_post(profile_id, v1_profiles_profile_id_verification_documents_post_request=v1_profiles_profile_id_verification_documents_post_request)

Create identification document

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.error import Error
from wise_api_client.models.v1_profiles_profile_id_verification_documents_post_request import V1ProfilesProfileIdVerificationDocumentsPostRequest
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    v1_profiles_profile_id_verification_documents_post_request = wise_api_client.V1ProfilesProfileIdVerificationDocumentsPostRequest() # V1ProfilesProfileIdVerificationDocumentsPostRequest |  (optional)

    try:
        # Create identification document
        api_response = api_instance.v1_profiles_profile_id_verification_documents_post(profile_id, v1_profiles_profile_id_verification_documents_post_request=v1_profiles_profile_id_verification_documents_post_request)
        print("The response of DefaultApi->v1_profiles_profile_id_verification_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_profiles_profile_id_verification_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **v1_profiles_profile_id_verification_documents_post_request** | [**V1ProfilesProfileIdVerificationDocumentsPostRequest**](V1ProfilesProfileIdVerificationDocumentsPostRequest.md)|  | [optional] 

### Return type

[**Error**](Error.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_quotes_quote_id_account_requirements_get**
> List[AccountRequirementsInner] v1_quotes_quote_id_account_requirements_get(quote_id, originator_legal_entity_type=originator_legal_entity_type, accept_minor_version=accept_minor_version)

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
    api_instance = wise_api_client.DefaultApi(api_client)
    quote_id = 'quote_id_example' # str | 
    originator_legal_entity_type = 'originator_legal_entity_type_example' # str |  (optional)
    accept_minor_version = '1' # str |  (optional) (default to '1')

    try:
        # Get account requirements for a quote
        api_response = api_instance.v1_quotes_quote_id_account_requirements_get(quote_id, originator_legal_entity_type=originator_legal_entity_type, accept_minor_version=accept_minor_version)
        print("The response of DefaultApi->v1_quotes_quote_id_account_requirements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_quotes_quote_id_account_requirements_get: %s\n" % e)
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

# **v1_refund_accounts_post**
> Recipient v1_refund_accounts_post(v1_refund_accounts_post_request)

Create a refund recipient account

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.recipient import Recipient
from wise_api_client.models.v1_refund_accounts_post_request import V1RefundAccountsPostRequest
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
    api_instance = wise_api_client.DefaultApi(api_client)
    v1_refund_accounts_post_request = wise_api_client.V1RefundAccountsPostRequest() # V1RefundAccountsPostRequest | 

    try:
        # Create a refund recipient account
        api_response = api_instance.v1_refund_accounts_post(v1_refund_accounts_post_request)
        print("The response of DefaultApi->v1_refund_accounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_refund_accounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_refund_accounts_post_request** | [**V1RefundAccountsPostRequest**](V1RefundAccountsPostRequest.md)|  | 

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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_requirements_request = wise_api_client.TransferRequirementsRequest() # TransferRequirementsRequest | 

    try:
        # Get transfer requirements
        api_response = api_instance.v1_transfer_requirements_post(transfer_requirements_request)
        print("The response of DefaultApi->v1_transfer_requirements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfer_requirements_post: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
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
        print("The response of DefaultApi->v1_transfers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    create_standard_transfer_request = wise_api_client.CreateStandardTransferRequest() # CreateStandardTransferRequest | 

    try:
        # Create a standard transfer
        api_response = api_instance.v1_transfers_post(create_standard_transfer_request)
        print("The response of DefaultApi->v1_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_post: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get NOC document
        api_response = api_instance.v1_transfers_transfer_id_documents_noc_get(transfer_id)
        print("The response of DefaultApi->v1_transfers_transfer_id_documents_noc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_transfer_id_documents_noc_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get transfer by ID
        api_response = api_instance.v1_transfers_transfer_id_get(transfer_id)
        print("The response of DefaultApi->v1_transfers_transfer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_transfer_id_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get banking partner invoice (v1)
        api_response = api_instance.v1_transfers_transfer_id_invoices_bankingpartner_get(transfer_id)
        print("The response of DefaultApi->v1_transfers_transfer_id_invoices_bankingpartner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_transfer_id_invoices_bankingpartner_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # List transfer payments
        api_response = api_instance.v1_transfers_transfer_id_payments_get(transfer_id)
        print("The response of DefaultApi->v1_transfers_transfer_id_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_transfer_id_payments_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Cancel transfer
        api_response = api_instance.v1_transfers_transfer_id_put(transfer_id)
        print("The response of DefaultApi->v1_transfers_transfer_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_transfer_id_put: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get transfer receipt PDF
        api_response = api_instance.v1_transfers_transfer_id_receipt_pdf_get(transfer_id)
        print("The response of DefaultApi->v1_transfers_transfer_id_receipt_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transfers_transfer_id_receipt_pdf_get: %s\n" % e)
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

# **v2_accounts_account_id_delete**
> Recipient v2_accounts_account_id_delete(account_id)

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
    api_instance = wise_api_client.DefaultApi(api_client)
    account_id = 56 # int | 

    try:
        # Deactivate a recipient account
        api_response = api_instance.v2_accounts_account_id_delete(account_id)
        print("The response of DefaultApi->v2_accounts_account_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_accounts_account_id_delete: %s\n" % e)
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

# **v2_accounts_account_id_get**
> Recipient v2_accounts_account_id_get(account_id)

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
    api_instance = wise_api_client.DefaultApi(api_client)
    account_id = 56 # int | 

    try:
        # Get recipient account by ID
        api_response = api_instance.v2_accounts_account_id_get(account_id)
        print("The response of DefaultApi->v2_accounts_account_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_accounts_account_id_get: %s\n" % e)
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

# **v2_accounts_get**
> PaginatedRecipients v2_accounts_get(profile_id=profile_id, currency=currency, size=size, seek_position=seek_position)

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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int |  (optional)
    currency = 'currency_example' # str |  (optional)
    size = 56 # int |  (optional)
    seek_position = 56 # int |  (optional)

    try:
        # List recipient accounts
        api_response = api_instance.v2_accounts_get(profile_id=profile_id, currency=currency, size=size, seek_position=seek_position)
        print("The response of DefaultApi->v2_accounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_accounts_get: %s\n" % e)
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

# **v2_profiles_get**
> List[V2ProfilesGet200ResponseInner] v2_profiles_get()

List profiles for a user account

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.v2_profiles_get200_response_inner import V2ProfilesGet200ResponseInner
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
    api_instance = wise_api_client.DefaultApi(api_client)

    try:
        # List profiles for a user account
        api_response = api_instance.v2_profiles_get()
        print("The response of DefaultApi->v2_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_profiles_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[V2ProfilesGet200ResponseInner]**](V2ProfilesGet200ResponseInner.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_profiles_profile_id_business_profile_put**
> BusinessProfile v2_profiles_profile_id_business_profile_put(profile_id, v2_profiles_profile_id_business_profile_put_request)

Update a business profile

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.business_profile import BusinessProfile
from wise_api_client.models.v2_profiles_profile_id_business_profile_put_request import V2ProfilesProfileIdBusinessProfilePutRequest
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    v2_profiles_profile_id_business_profile_put_request = wise_api_client.V2ProfilesProfileIdBusinessProfilePutRequest() # V2ProfilesProfileIdBusinessProfilePutRequest | 

    try:
        # Update a business profile
        api_response = api_instance.v2_profiles_profile_id_business_profile_put(profile_id, v2_profiles_profile_id_business_profile_put_request)
        print("The response of DefaultApi->v2_profiles_profile_id_business_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_profiles_profile_id_business_profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **v2_profiles_profile_id_business_profile_put_request** | [**V2ProfilesProfileIdBusinessProfilePutRequest**](V2ProfilesProfileIdBusinessProfilePutRequest.md)|  | 

### Return type

[**BusinessProfile**](BusinessProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Business profile updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_profiles_profile_id_get**
> V2ProfilesProfileIdGet200Response v2_profiles_profile_id_get(profile_id)

Retrieve a profile by ID

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.v2_profiles_profile_id_get200_response import V2ProfilesProfileIdGet200Response
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 

    try:
        # Retrieve a profile by ID
        api_response = api_instance.v2_profiles_profile_id_get(profile_id)
        print("The response of DefaultApi->v2_profiles_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_profiles_profile_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 

### Return type

[**V2ProfilesProfileIdGet200Response**](V2ProfilesProfileIdGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_profiles_profile_id_personal_profile_put**
> PersonalProfile v2_profiles_profile_id_personal_profile_put(profile_id, v2_profiles_profile_id_personal_profile_put_request)

Update a personal profile

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.personal_profile import PersonalProfile
from wise_api_client.models.v2_profiles_profile_id_personal_profile_put_request import V2ProfilesProfileIdPersonalProfilePutRequest
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    v2_profiles_profile_id_personal_profile_put_request = wise_api_client.V2ProfilesProfileIdPersonalProfilePutRequest() # V2ProfilesProfileIdPersonalProfilePutRequest | 

    try:
        # Update a personal profile
        api_response = api_instance.v2_profiles_profile_id_personal_profile_put(profile_id, v2_profiles_profile_id_personal_profile_put_request)
        print("The response of DefaultApi->v2_profiles_profile_id_personal_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_profiles_profile_id_personal_profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **v2_profiles_profile_id_personal_profile_put_request** | [**V2ProfilesProfileIdPersonalProfilePutRequest**](V2ProfilesProfileIdPersonalProfilePutRequest.md)|  | 

### Return type

[**PersonalProfile**](PersonalProfile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Personal profile updated |  -  |

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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 
    create_third_party_transfer_request = wise_api_client.CreateThirdPartyTransferRequest() # CreateThirdPartyTransferRequest | 

    try:
        # Create third-party transfer
        api_response = api_instance.v2_profiles_profile_id_third_party_transfers_post(profile_id, create_third_party_transfer_request)
        print("The response of DefaultApi->v2_profiles_profile_id_third_party_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_profiles_profile_id_third_party_transfers_post: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 
    transfer_id = 56 # int | 

    try:
        # Get third-party transfer
        api_response = api_instance.v2_profiles_profile_id_third_party_transfers_transfer_id_get(profile_id, transfer_id)
        print("The response of DefaultApi->v2_profiles_profile_id_third_party_transfers_transfer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_profiles_profile_id_third_party_transfers_transfer_id_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    transfer_id = 56 # int | 

    try:
        # Get banking partner invoice (v2)
        api_response = api_instance.v2_transfers_transfer_id_invoices_bankingpartner_get(transfer_id)
        print("The response of DefaultApi->v2_transfers_transfer_id_invoices_bankingpartner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_transfers_transfer_id_invoices_bankingpartner_get: %s\n" % e)
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 
    transfer_id = 56 # int | 
    payment_request = wise_api_client.PaymentRequest() # PaymentRequest | 

    try:
        # Fund a transfer
        api_response = api_instance.v3_profiles_profile_id_transfers_transfer_id_payments_post(profile_id, transfer_id, payment_request)
        print("The response of DefaultApi->v3_profiles_profile_id_transfers_transfer_id_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_profiles_profile_id_transfers_transfer_id_payments_post: %s\n" % e)
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

# **v3_profiles_profile_id_verification_status_bank_transfer_post**
> VerificationStatusResponse v3_profiles_profile_id_verification_status_bank_transfer_post(profile_id, source_currencies)

Check verification status

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.verification_status_response import VerificationStatusResponse
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
    api_instance = wise_api_client.DefaultApi(api_client)
    profile_id = 56 # int | 
    source_currencies = ['source_currencies_example'] # List[str] | 

    try:
        # Check verification status
        api_response = api_instance.v3_profiles_profile_id_verification_status_bank_transfer_post(profile_id, source_currencies)
        print("The response of DefaultApi->v3_profiles_profile_id_verification_status_bank_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_profiles_profile_id_verification_status_bank_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **source_currencies** | [**List[str]**](str.md)|  | 

### Return type

[**VerificationStatusResponse**](VerificationStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

