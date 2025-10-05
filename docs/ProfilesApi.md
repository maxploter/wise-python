# wise_api_client.ProfilesApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_directors**](ProfilesApi.md#add_directors) | **POST** /v1/profiles/{profileId}/directors | Add directors
[**check_verification_status**](ProfilesApi.md#check_verification_status) | **POST** /v3/profiles/{profileId}/verification-status/bank-transfer | Check verification status
[**create_business_profile**](ProfilesApi.md#create_business_profile) | **POST** /v2/profiles/business-profile | Create a business profile
[**create_personal_profile**](ProfilesApi.md#create_personal_profile) | **POST** /v2/profiles/personal-profile | Create a personal profile
[**create_verification_document**](ProfilesApi.md#create_verification_document) | **POST** /v1/profiles/{profileId}/verification-documents | Create identification document
[**get_profile_by_id**](ProfilesApi.md#get_profile_by_id) | **GET** /v2/profiles/{profileId} | Retrieve a profile by ID
[**list_directors**](ProfilesApi.md#list_directors) | **GET** /v1/profiles/{profileId}/directors | List directors
[**list_profiles**](ProfilesApi.md#list_profiles) | **GET** /v2/profiles | List profiles for a user account
[**update_business_profile**](ProfilesApi.md#update_business_profile) | **PUT** /v2/profiles/{profileId}/business-profile | Update a business profile
[**update_directors**](ProfilesApi.md#update_directors) | **PUT** /v1/profiles/{profileId}/directors | Update directors
[**update_personal_profile**](ProfilesApi.md#update_personal_profile) | **PUT** /v2/profiles/{profileId}/personal-profile | Update a personal profile


# **add_directors**
> List[Director] add_directors(profile_id, director=director)

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
        api_response = api_instance.add_directors(profile_id, director=director)
        print("The response of ProfilesApi->add_directors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->add_directors: %s\n" % e)
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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_verification_status**
> VerificationStatusResponse check_verification_status(profile_id, source_currencies)

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
        api_response = api_instance.check_verification_status(profile_id, source_currencies)
        print("The response of ProfilesApi->check_verification_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->check_verification_status: %s\n" % e)
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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_verification_document**
> CreateVerificationDocumentResponse create_verification_document(profile_id, create_verification_document_request=create_verification_document_request)

Create identification document

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.create_verification_document_request import CreateVerificationDocumentRequest
from wise_api_client.models.create_verification_document_response import CreateVerificationDocumentResponse
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
    create_verification_document_request = wise_api_client.CreateVerificationDocumentRequest() # CreateVerificationDocumentRequest |  (optional)

    try:
        # Create identification document
        api_response = api_instance.create_verification_document(profile_id, create_verification_document_request=create_verification_document_request)
        print("The response of ProfilesApi->create_verification_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_verification_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **create_verification_document_request** | [**CreateVerificationDocumentRequest**](CreateVerificationDocumentRequest.md)|  | [optional] 

### Return type

[**CreateVerificationDocumentResponse**](CreateVerificationDocumentResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document created |  -  |
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_id**
> GetProfileById200Response get_profile_by_id(profile_id)

Retrieve a profile by ID

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.get_profile_by_id200_response import GetProfileById200Response
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
        api_response = api_instance.get_profile_by_id(profile_id)
        print("The response of ProfilesApi->get_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 

### Return type

[**GetProfileById200Response**](GetProfileById200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile details |  -  |
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_directors**
> List[Director] list_directors(profile_id)

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
        api_response = api_instance.list_directors(profile_id)
        print("The response of ProfilesApi->list_directors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->list_directors: %s\n" % e)
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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profiles**
> List[GetProfileById200Response] list_profiles()

List profiles for a user account

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.get_profile_by_id200_response import GetProfileById200Response
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
        api_response = api_instance.list_profiles()
        print("The response of ProfilesApi->list_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->list_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetProfileById200Response]**](GetProfileById200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of profiles |  -  |
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_profile**
> BusinessProfile update_business_profile(profile_id, update_business_profile_request)

Update a business profile

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.business_profile import BusinessProfile
from wise_api_client.models.update_business_profile_request import UpdateBusinessProfileRequest
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
    update_business_profile_request = wise_api_client.UpdateBusinessProfileRequest() # UpdateBusinessProfileRequest | 

    try:
        # Update a business profile
        api_response = api_instance.update_business_profile(profile_id, update_business_profile_request)
        print("The response of ProfilesApi->update_business_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_business_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **update_business_profile_request** | [**UpdateBusinessProfileRequest**](UpdateBusinessProfileRequest.md)|  | 

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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_directors**
> List[Director] update_directors(profile_id, director=director)

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
        api_response = api_instance.update_directors(profile_id, director=director)
        print("The response of ProfilesApi->update_directors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_directors: %s\n" % e)
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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_personal_profile**
> PersonalProfile update_personal_profile(profile_id, update_personal_profile_request)

Update a personal profile

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.personal_profile import PersonalProfile
from wise_api_client.models.update_personal_profile_request import UpdatePersonalProfileRequest
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
    update_personal_profile_request = wise_api_client.UpdatePersonalProfileRequest() # UpdatePersonalProfileRequest | 

    try:
        # Update a personal profile
        api_response = api_instance.update_personal_profile(profile_id, update_personal_profile_request)
        print("The response of ProfilesApi->update_personal_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_personal_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **int**|  | 
 **update_personal_profile_request** | [**UpdatePersonalProfileRequest**](UpdatePersonalProfileRequest.md)|  | 

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
**400** | Bad request. Request message data did not pass validation. |  -  |
**401** | Unauthorised. Not authorised to access requested data. |  -  |
**403** | Forbidden. Access to requested data is forbidden. |  -  |
**404** | Not Found. Requested resource does not exist. |  -  |
**408** | Timeout. Operation timed out. |  -  |
**422** | Unprocessable entity. Request message data did not pass validation. |  -  |
**429** | Too Many Requests |  -  |
**500** | Server error. |  -  |
**4XX** | Client Error - Bad request, unauthorized, forbidden, not found, or validation error |  -  |
**5XX** | Server Error - Internal server error or service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

