# AdcsQuatT

ADCS QBO type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q1** | **float** |  | 
**q2** | **float** |  | 
**q3** | **float** |  | 
**q4** | **float** |  | 

## Example

```python
from oort_sdk_client.models.adcs_quat_t import AdcsQuatT

# TODO update the JSON string below
json = "{}"
# create an instance of AdcsQuatT from a JSON string
adcs_quat_t_instance = AdcsQuatT.from_json(json)
# print the JSON string representation of the object
print(AdcsQuatT.to_json())

# convert the object into a dict
adcs_quat_t_dict = adcs_quat_t_instance.to_dict()
# create an instance of AdcsQuatT from a dict
adcs_quat_t_from_dict = AdcsQuatT.from_dict(adcs_quat_t_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


