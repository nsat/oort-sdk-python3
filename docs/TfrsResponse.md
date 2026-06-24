# TfrsResponse

TFRS time and position

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **float** | age of the cached value | 
**utc_time** | **int** | unix epoch time | 
**ecef_pos_x** | **float** | ECEF X position | 
**ecef_pos_y** | **float** | ECEF Y position | 
**ecef_pos_z** | **float** | ECEF Z position | 
**ecef_vel_x** | **float** | ECEF X velocity | 
**ecef_vel_y** | **float** | ECEF Y velocity | 
**ecef_vel_z** | **float** | ECEF Z velocity | 

## Example

```python
from oort_sdk_client.models.tfrs_response import TfrsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TfrsResponse from a JSON string
tfrs_response_instance = TfrsResponse.from_json(json)
# print the JSON string representation of the object
print(TfrsResponse.to_json())

# convert the object into a dict
tfrs_response_dict = tfrs_response_instance.to_dict()
# create an instance of TfrsResponse from a dict
tfrs_response_from_dict = TfrsResponse.from_dict(tfrs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


