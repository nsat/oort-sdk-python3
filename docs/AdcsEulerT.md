# AdcsEulerT

ADCS Euler angles -- roll, pitch, yaw

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roll** | **float** |  | 
**pitch** | **float** |  | 
**yaw** | **float** |  | 

## Example

```python
from oort_sdk_client.models.adcs_euler_t import AdcsEulerT

# TODO update the JSON string below
json = "{}"
# create an instance of AdcsEulerT from a JSON string
adcs_euler_t_instance = AdcsEulerT.from_json(json)
# print the JSON string representation of the object
print(AdcsEulerT.to_json())

# convert the object into a dict
adcs_euler_t_dict = adcs_euler_t_instance.to_dict()
# create an instance of AdcsEulerT from a dict
adcs_euler_t_from_dict = AdcsEulerT.from_dict(adcs_euler_t_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


