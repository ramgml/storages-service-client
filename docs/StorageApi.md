# swagger_client.StorageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_id_delete**](StorageApi.md#storage_id_delete) | **DELETE** /storage/{id} | Удалить данные хранилища
[**storage_id_get**](StorageApi.md#storage_id_get) | **GET** /storage/{id} | Получить данные хранилища
[**storage_id_put**](StorageApi.md#storage_id_put) | **PUT** /storage/{id} | Обновить данные хранилища
[**storage_post**](StorageApi.md#storage_post) | **POST** /storage | Добавление хранилища

# **storage_id_delete**
> storage_id_delete(id)

Удалить данные хранилища

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi()
id = 789 # int | ID хранилища полученный при его добавлении

try:
    # Удалить данные хранилища
    api_instance.storage_id_delete(id)
except ApiException as e:
    print("Exception when calling StorageApi->storage_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID хранилища полученный при его добавлении | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_id_get**
> StorageResponse storage_id_get(id)

Получить данные хранилища

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi()
id = 789 # int | ID хранилища полученный при его добавлении

try:
    # Получить данные хранилища
    api_response = api_instance.storage_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->storage_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID хранилища полученный при его добавлении | 

### Return type

[**StorageResponse**](StorageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_id_put**
> StorageResponse storage_id_put(id)

Обновить данные хранилища

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi()
id = 789 # int | ID хранилища полученный при его добавлении

try:
    # Обновить данные хранилища
    api_response = api_instance.storage_id_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->storage_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID хранилища полученный при его добавлении | 

### Return type

[**StorageResponse**](StorageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_post**
> StorageResponse storage_post(body=body)

Добавление хранилища

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi()
body = swagger_client.StorageRequest() # StorageRequest |  (optional)

try:
    # Добавление хранилища
    api_response = api_instance.storage_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->storage_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageRequest**](StorageRequest.md)|  | [optional] 

### Return type

[**StorageResponse**](StorageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

