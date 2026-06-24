# SendFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | the destination to send the file to | 
**filepath** | **str** | The source filepath.  Must be an absolute path. | 
**topic** | **str** | the pipeline topic to send the file to | 
**options** | [**SendOptions**](SendOptions.md) |  | [optional] 

## Example

```python
from oort_sdk_client.models.send_file_request import SendFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendFileRequest from a JSON string
send_file_request_instance = SendFileRequest.from_json(json)
# print the JSON string representation of the object
print(SendFileRequest.to_json())

# convert the object into a dict
send_file_request_dict = send_file_request_instance.to_dict()
# create an instance of SendFileRequest from a dict
send_file_request_from_dict = SendFileRequest.from_dict(send_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


