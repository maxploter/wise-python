# wise_api_client.QuotesApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_profiles_profile_id_quotes_post**](QuotesApi.md#v3_profiles_profile_id_quotes_post) | **POST** /v3/profiles/{profileId}/quotes | Create an authenticated quote
[**v3_profiles_profile_id_quotes_quote_id_get**](QuotesApi.md#v3_profiles_profile_id_quotes_quote_id_get) | **GET** /v3/profiles/{profileId}/quotes/{quoteId} | Retrieve a quote by ID
[**v3_profiles_profile_id_quotes_quote_id_patch**](QuotesApi.md#v3_profiles_profile_id_quotes_quote_id_patch) | **PATCH** /v3/profiles/{profileId}/quotes/{quoteId} | Update a quote
[**v3_quotes_post**](QuotesApi.md#v3_quotes_post) | **POST** /v3/quotes | Create an unauthenticated quote


# **v3_profiles_profile_id_quotes_post**
> Quote v3_profiles_profile_id_quotes_post(profile_id, create_authenticated_quote_request)

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
    api_instance = wise_api_client.QuotesApi(api_client)
    profile_id = 56 # int | 
    create_authenticated_quote_request = wise_api_client.CreateAuthenticatedQuoteRequest() # CreateAuthenticatedQuoteRequest | 

    try:
        # Create an authenticated quote
        api_response = api_instance.v3_profiles_profile_id_quotes_post(profile_id, create_authenticated_quote_request)
        print("The response of QuotesApi->v3_profiles_profile_id_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->v3_profiles_profile_id_quotes_post: %s\n" % e)
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
**200** | Successfully created authenticated quote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_profiles_profile_id_quotes_quote_id_get**
> Quote v3_profiles_profile_id_quotes_quote_id_get(profile_id, quote_id)

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
    api_instance = wise_api_client.QuotesApi(api_client)
    profile_id = 56 # int | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Retrieve a quote by ID
        api_response = api_instance.v3_profiles_profile_id_quotes_quote_id_get(profile_id, quote_id)
        print("The response of QuotesApi->v3_profiles_profile_id_quotes_quote_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->v3_profiles_profile_id_quotes_quote_id_get: %s\n" % e)
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

# **v3_profiles_profile_id_quotes_quote_id_patch**
> Quote v3_profiles_profile_id_quotes_quote_id_patch(profile_id, quote_id, update_quote_request)

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
    api_instance = wise_api_client.QuotesApi(api_client)
    profile_id = 56 # int | 
    quote_id = 'quote_id_example' # str | 
    update_quote_request = wise_api_client.UpdateQuoteRequest() # UpdateQuoteRequest | 

    try:
        # Update a quote
        api_response = api_instance.v3_profiles_profile_id_quotes_quote_id_patch(profile_id, quote_id, update_quote_request)
        print("The response of QuotesApi->v3_profiles_profile_id_quotes_quote_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->v3_profiles_profile_id_quotes_quote_id_patch: %s\n" % e)
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

# **v3_quotes_post**
> Quote v3_quotes_post(create_unauthenticated_quote_request)

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
    api_instance = wise_api_client.QuotesApi(api_client)
    create_unauthenticated_quote_request = wise_api_client.CreateUnauthenticatedQuoteRequest() # CreateUnauthenticatedQuoteRequest | 

    try:
        # Create an unauthenticated quote
        api_response = api_instance.v3_quotes_post(create_unauthenticated_quote_request)
        print("The response of QuotesApi->v3_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->v3_quotes_post: %s\n" % e)
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

