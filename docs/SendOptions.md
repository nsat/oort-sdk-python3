# SendOptions

options to apply to a send request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl_params** | [**TTLParams**](TTLParams.md) |  | [optional] 
**reliable** | **bool** | whether to send an item reliably, i.e., with retries | [optional] [default to True]
**tags** | **Dict[str, str]** | a structure for optional file tags | [optional] 
**delivery_hints** | [**DeliveryHints**](DeliveryHints.md) |  | [optional] 

## Example

```python
from oort_sdk_client.models.send_options import SendOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SendOptions from a JSON string
send_options_instance = SendOptions.from_json(json)
# print the JSON string representation of the object
print(SendOptions.to_json())

# convert the object into a dict
send_options_dict = send_options_instance.to_dict()
# create an instance of SendOptions from a dict
send_options_from_dict = SendOptions.from_dict(send_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


