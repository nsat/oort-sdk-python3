# oort_sdk_client.SdkApi

All URIs are relative to *http://localhost:2005/sdk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command_adcs**](SdkApi.md#command_adcs) | **POST** /adcs | 
[**get_adcs**](SdkApi.md#get_adcs) | **GET** /adcs | 
[**get_tfrs**](SdkApi.md#get_tfrs) | **GET** /tfrs | 
[**query_available_files**](SdkApi.md#query_available_files) | **GET** /query_available_files/{topic} | 
[**retrieve_file**](SdkApi.md#retrieve_file) | **POST** /retrieve_file | 
[**send_file**](SdkApi.md#send_file) | **POST** /send_file | 


# **command_adcs**
> AdcsCommandResponse command_adcs(adcs_command_request)

request adcs operation

### Example


```python
import oort_sdk_client
from oort_sdk_client.models.adcs_command_request import AdcsCommandRequest
from oort_sdk_client.models.adcs_command_response import AdcsCommandResponse
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:2005/sdk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oort_sdk_client.Configuration(
    host = "http://localhost:2005/sdk/v1"
)


# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    adcs_command_request = oort_sdk_client.AdcsCommandRequest() # AdcsCommandRequest | The file and parameters for sending

    try:
        api_response = api_instance.command_adcs(adcs_command_request)
        print("The response of SdkApi->command_adcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkApi->command_adcs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adcs_command_request** | [**AdcsCommandRequest**](AdcsCommandRequest.md)| The file and parameters for sending | 

### Return type

[**AdcsCommandResponse**](AdcsCommandResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | ERROR |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_adcs**
> AdcsResponse get_adcs()

query adcs status

### Example


```python
import oort_sdk_client
from oort_sdk_client.models.adcs_response import AdcsResponse
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:2005/sdk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oort_sdk_client.Configuration(
    host = "http://localhost:2005/sdk/v1"
)


# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)

    try:
        api_response = api_instance.get_adcs()
        print("The response of SdkApi->get_adcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkApi->get_adcs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AdcsResponse**](AdcsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tfrs**
> TfrsResponse get_tfrs()

get tfrs values

### Example


```python
import oort_sdk_client
from oort_sdk_client.models.tfrs_response import TfrsResponse
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:2005/sdk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oort_sdk_client.Configuration(
    host = "http://localhost:2005/sdk/v1"
)


# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)

    try:
        api_response = api_instance.get_tfrs()
        print("The response of SdkApi->get_tfrs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkApi->get_tfrs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TfrsResponse**](TfrsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_available_files**
> AvailableFilesResponse query_available_files(topic)

### Example


```python
import oort_sdk_client
from oort_sdk_client.models.available_files_response import AvailableFilesResponse
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:2005/sdk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oort_sdk_client.Configuration(
    host = "http://localhost:2005/sdk/v1"
)


# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    topic = 'topic_example' # str | 

    try:
        api_response = api_instance.query_available_files(topic)
        print("The response of SdkApi->query_available_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkApi->query_available_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 

### Return type

[**AvailableFilesResponse**](AvailableFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> FileInfo retrieve_file(retrieve_file_request)

### Example


```python
import oort_sdk_client
from oort_sdk_client.models.file_info import FileInfo
from oort_sdk_client.models.retrieve_file_request import RetrieveFileRequest
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:2005/sdk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oort_sdk_client.Configuration(
    host = "http://localhost:2005/sdk/v1"
)


# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    retrieve_file_request = oort_sdk_client.RetrieveFileRequest() # RetrieveFileRequest | 

    try:
        api_response = api_instance.retrieve_file(retrieve_file_request)
        print("The response of SdkApi->retrieve_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkApi->retrieve_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_file_request** | [**RetrieveFileRequest**](RetrieveFileRequest.md)|  | 

### Return type

[**FileInfo**](FileInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_file**
> SendFileResponse send_file(send_file_request)

### Example


```python
import oort_sdk_client
from oort_sdk_client.models.send_file_request import SendFileRequest
from oort_sdk_client.models.send_file_response import SendFileResponse
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:2005/sdk/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oort_sdk_client.Configuration(
    host = "http://localhost:2005/sdk/v1"
)


# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    send_file_request = oort_sdk_client.SendFileRequest() # SendFileRequest | The file and parameters for sending

    try:
        api_response = api_instance.send_file(send_file_request)
        print("The response of SdkApi->send_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkApi->send_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_file_request** | [**SendFileRequest**](SendFileRequest.md)| The file and parameters for sending | 

### Return type

[**SendFileResponse**](SendFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

