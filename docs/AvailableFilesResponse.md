# AvailableFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileInfo]**](FileInfo.md) |  | 
**overflow** | **bool** | true if there are more files available than could be returned in this call | [optional] 

## Example

```python
from oort_sdk_client.models.available_files_response import AvailableFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableFilesResponse from a JSON string
available_files_response_instance = AvailableFilesResponse.from_json(json)
# print the JSON string representation of the object
print(AvailableFilesResponse.to_json())

# convert the object into a dict
available_files_response_dict = available_files_response_instance.to_dict()
# create an instance of AvailableFilesResponse from a dict
available_files_response_from_dict = AvailableFilesResponse.from_dict(available_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


