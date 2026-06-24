# AdcsCommandRequest

Request to set ADCS mode and parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | SPACS attitude control command | 
**aperture** | **str** | Aperture (imager, antenna, etc) name to use in ADCS pointing requests | [optional] 
**target** | [**AdcsTarget**](AdcsTarget.md) |  | [optional] 
**angle** | **float** |  | [optional] 
**vector** | [**AdcsXyzFloatT**](AdcsXyzFloatT.md) |  | [optional] 
**quat** | [**AdcsQuatT**](AdcsQuatT.md) |  | [optional] 

## Example

```python
from oort_sdk_client.models.adcs_command_request import AdcsCommandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdcsCommandRequest from a JSON string
adcs_command_request_instance = AdcsCommandRequest.from_json(json)
# print the JSON string representation of the object
print(AdcsCommandRequest.to_json())

# convert the object into a dict
adcs_command_request_dict = adcs_command_request_instance.to_dict()
# create an instance of AdcsCommandRequest from a dict
adcs_command_request_from_dict = AdcsCommandRequest.from_dict(adcs_command_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


