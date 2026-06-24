# RetrieveFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**save_path** | **str** | The destination path to save the file. Must be an absolute path. | 

## Example

```python
from oort_sdk_client.models.retrieve_file_request import RetrieveFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveFileRequest from a JSON string
retrieve_file_request_instance = RetrieveFileRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieveFileRequest.to_json())

# convert the object into a dict
retrieve_file_request_dict = retrieve_file_request_instance.to_dict()
# create an instance of RetrieveFileRequest from a dict
retrieve_file_request_from_dict = RetrieveFileRequest.from_dict(retrieve_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


