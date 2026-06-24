# SendFileResponse

Response to a send file request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 

## Example

```python
from oort_sdk_client.models.send_file_response import SendFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendFileResponse from a JSON string
send_file_response_instance = SendFileResponse.from_json(json)
# print the JSON string representation of the object
print(SendFileResponse.to_json())

# convert the object into a dict
send_file_response_dict = send_file_response_instance.to_dict()
# create an instance of SendFileResponse from a dict
send_file_response_from_dict = SendFileResponse.from_dict(send_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


