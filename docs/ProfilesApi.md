# wise_api_client.ProfilesApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_profile**](ProfilesApi.md#create_business_profile) | **POST** /v2/profiles/business-profile | Create a business profile
[**create_personal_profile**](ProfilesApi.md#create_personal_profile) | **POST** /v2/profiles/personal-profile | Create a personal profile
[**v1_profiles_profile_id_directors_get**](ProfilesApi.md#v1_profiles_profile_id_directors_get) | **GET** /v1/profiles/{profileId}/directors | List directors
[**v1_profiles_profile_id_directors_post**](ProfilesApi.md#v1_profiles_profile_id_directors_post) | **POST** /v1/profiles/{profileId}/directors | Add directors
[**v1_profiles_profile_id_directors_put**](ProfilesApi.md#v1_profiles_profile_id_directors_put) | **PUT** /v1/profiles/{profileId}/directors | Update directors
[**v1_profiles_profile_id_verification_documents_post**](ProfilesApi.md#v1_profiles_profile_id_verification_documents_post) | **POST** /v1/profiles/{profileId}/verification-documents | Create identification document
[**v2_profiles_get**](ProfilesApi.md#v2_profiles_get) | **GET** /v2/profiles | List profiles for a user account
[**v2_profiles_profile_id_business_profile_put**](ProfilesApi.md#v2_profiles_profile_id_business_profile_put) | **PUT** /v2/profiles/{profileId}/business-profile | Update a business profile
[**v2_profiles_profile_id_get**](ProfilesApi.md#v2_profiles_profile_id_get) | **GET** /v2/profiles/{profileId} | Retrieve a profile by ID
[**v2_profiles_profile_id_personal_profile_put**](ProfilesApi.md#v2_profiles_profile_id_personal_profile_put) | **PUT** /v2/profiles/{profileId}/personal-profile | Update a personal profile
[**v3_profiles_profile_id_verification_status_bank_transfer_post**](ProfilesApi.md#v3_profiles_profile_id_verification_status_bank_transfer_post) | **POST** /v3/profiles/{profileId}/verification-status/bank-transfer | Check verification status


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
    api_instance = wise_api_client.ProfilesApi(api_client)
    create_business_profile_request = wise_api_client.CreateBusinessProfileRequest() # CreateBusinessProfileRequest | 

    try:
        # Create a business profile
        api_response = api_instance.create_business_profile(create_business_profile_request)
        print("The response of ProfilesApi->create_business_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_business_profile: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    create_personal_profile_request = wise_api_client.CreatePersonalProfileRequest() # CreatePersonalProfileRequest | 

    try:
        # Create a personal profile
        api_response = api_instance.create_personal_profile(create_personal_profile_request)
        print("The response of ProfilesApi->create_personal_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_personal_profile: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 

    try:
        # List directors
        api_response = api_instance.v1_profiles_profile_id_directors_get(profile_id)
        print("The response of ProfilesApi->v1_profiles_profile_id_directors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v1_profiles_profile_id_directors_get: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 
    director = [wise_api_client.Director()] # List[Director] |  (optional)

    try:
        # Add directors
        api_response = api_instance.v1_profiles_profile_id_directors_post(profile_id, director=director)
        print("The response of ProfilesApi->v1_profiles_profile_id_directors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v1_profiles_profile_id_directors_post: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 
    director = [wise_api_client.Director()] # List[Director] |  (optional)

    try:
        # Update directors
        api_response = api_instance.v1_profiles_profile_id_directors_put(profile_id, director=director)
        print("The response of ProfilesApi->v1_profiles_profile_id_directors_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v1_profiles_profile_id_directors_put: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 
    v1_profiles_profile_id_verification_documents_post_request = wise_api_client.V1ProfilesProfileIdVerificationDocumentsPostRequest() # V1ProfilesProfileIdVerificationDocumentsPostRequest |  (optional)

    try:
        # Create identification document
        api_response = api_instance.v1_profiles_profile_id_verification_documents_post(profile_id, v1_profiles_profile_id_verification_documents_post_request=v1_profiles_profile_id_verification_documents_post_request)
        print("The response of ProfilesApi->v1_profiles_profile_id_verification_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v1_profiles_profile_id_verification_documents_post: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)

    try:
        # List profiles for a user account
        api_response = api_instance.v2_profiles_get()
        print("The response of ProfilesApi->v2_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v2_profiles_get: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 
    v2_profiles_profile_id_business_profile_put_request = wise_api_client.V2ProfilesProfileIdBusinessProfilePutRequest() # V2ProfilesProfileIdBusinessProfilePutRequest | 

    try:
        # Update a business profile
        api_response = api_instance.v2_profiles_profile_id_business_profile_put(profile_id, v2_profiles_profile_id_business_profile_put_request)
        print("The response of ProfilesApi->v2_profiles_profile_id_business_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v2_profiles_profile_id_business_profile_put: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 

    try:
        # Retrieve a profile by ID
        api_response = api_instance.v2_profiles_profile_id_get(profile_id)
        print("The response of ProfilesApi->v2_profiles_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v2_profiles_profile_id_get: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 
    v2_profiles_profile_id_personal_profile_put_request = wise_api_client.V2ProfilesProfileIdPersonalProfilePutRequest() # V2ProfilesProfileIdPersonalProfilePutRequest | 

    try:
        # Update a personal profile
        api_response = api_instance.v2_profiles_profile_id_personal_profile_put(profile_id, v2_profiles_profile_id_personal_profile_put_request)
        print("The response of ProfilesApi->v2_profiles_profile_id_personal_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v2_profiles_profile_id_personal_profile_put: %s\n" % e)
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
    api_instance = wise_api_client.ProfilesApi(api_client)
    profile_id = 56 # int | 
    source_currencies = ['source_currencies_example'] # List[str] | 

    try:
        # Check verification status
        api_response = api_instance.v3_profiles_profile_id_verification_status_bank_transfer_post(profile_id, source_currencies)
        print("The response of ProfilesApi->v3_profiles_profile_id_verification_status_bank_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->v3_profiles_profile_id_verification_status_bank_transfer_post: %s\n" % e)
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

