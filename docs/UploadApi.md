# swagger_client.UploadApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_post**](UploadApi.md#upload_post) | **POST** /upload | Загрузка файла

# **upload_post**
> upload_post(storage_id=storage_id, path=path, file=file)

Загрузка файла

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApi()
storage_id = 789 # int |  (optional)
path = 'path_example' # str |  (optional)
file = 'file_example' # str |  (optional)

try:
    # Загрузка файла
    api_instance.upload_post(storage_id=storage_id, path=path, file=file)
except ApiException as e:
    print("Exception when calling UploadApi->upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **int**|  | [optional] 
 **path** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

