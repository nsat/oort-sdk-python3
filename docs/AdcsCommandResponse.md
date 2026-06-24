# AdcsCommandResponse

Response to ADCS command request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | [optional] 
**mode** | **str** |  | 
**target** | [**AdcsTarget**](AdcsTarget.md) |  | [optional] 
**vector** | [**AdcsXyzFloatT**](AdcsXyzFloatT.md) |  | [optional] 
**quat** | [**AdcsQuatT**](AdcsQuatT.md) |  | [optional] 

## Example

```python
from oort_sdk_client.models.adcs_command_response import AdcsCommandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdcsCommandResponse from a JSON string
adcs_command_response_instance = AdcsCommandResponse.from_json(json)
# print the JSON string representation of the object
print(AdcsCommandResponse.to_json())

# convert the object into a dict
adcs_command_response_dict = adcs_command_response_instance.to_dict()
# create an instance of AdcsCommandResponse from a dict
adcs_command_response_from_dict = AdcsCommandResponse.from_dict(adcs_command_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


