# wise_api_client.ActivitiesApi

All URIs are relative to *https://api.sandbox.transferwise.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_profiles_profile_id_activities_get**](ActivitiesApi.md#v1_profiles_profile_id_activities_get) | **GET** /v1/profiles/{profileId}/activities | List activities for a profile


# **v1_profiles_profile_id_activities_get**
> ActivitiesResponse v1_profiles_profile_id_activities_get(profile_id, monetary_resource_type=monetary_resource_type, status=status, since=since, until=until, next_cursor=next_cursor, size=size)

List activities for a profile

Retrieve paginated list of activities for a user profile with filtering options

### Example

* Bearer Authentication (BearerAuth):

```python
import wise_api_client
from wise_api_client.models.activities_response import ActivitiesResponse
from wise_api_client.models.activity_resource_type import ActivityResourceType
from wise_api_client.models.activity_status import ActivityStatus
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
    api_instance = wise_api_client.ActivitiesApi(api_client)
    profile_id = 'profile_id_example' # str | ID of the user profile
    monetary_resource_type = wise_api_client.ActivityResourceType() # ActivityResourceType | Filter by resource type (optional)
    status = wise_api_client.ActivityStatus() # ActivityStatus | Filter by activity status (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | Filter activities created after this timestamp (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | Filter activities created before this timestamp (optional)
    next_cursor = 'next_cursor_example' # str | Pagination cursor for next page (optional)
    size = 10 # int | Number of results per page (optional) (default to 10)

    try:
        # List activities for a profile
        api_response = api_instance.v1_profiles_profile_id_activities_get(profile_id, monetary_resource_type=monetary_resource_type, status=status, since=since, until=until, next_cursor=next_cursor, size=size)
        print("The response of ActivitiesApi->v1_profiles_profile_id_activities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->v1_profiles_profile_id_activities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| ID of the user profile | 
 **monetary_resource_type** | [**ActivityResourceType**](.md)| Filter by resource type | [optional] 
 **status** | [**ActivityStatus**](.md)| Filter by activity status | [optional] 
 **since** | **datetime**| Filter activities created after this timestamp | [optional] 
 **until** | **datetime**| Filter activities created before this timestamp | [optional] 
 **next_cursor** | **str**| Pagination cursor for next page | [optional] 
 **size** | **int**| Number of results per page | [optional] [default to 10]

### Return type

[**ActivitiesResponse**](ActivitiesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with activities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

