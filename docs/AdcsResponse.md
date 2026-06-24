# AdcsResponse

ADCS Orientation and status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | The current ADCS mode | 
**age** | **float** | Time in seconds since last live reading from ACDS | 
**controller** | **str** | the controlling payload at the time of the last live reading | [optional] 
**hk** | [**AdcsHk**](AdcsHk.md) |  | [optional] 

## Example

```python
from oort_sdk_client.models.adcs_response import AdcsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdcsResponse from a JSON string
adcs_response_instance = AdcsResponse.from_json(json)
# print the JSON string representation of the object
print(AdcsResponse.to_json())

# convert the object into a dict
adcs_response_dict = adcs_response_instance.to_dict()
# create an instance of AdcsResponse from a dict
adcs_response_from_dict = AdcsResponse.from_dict(adcs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


