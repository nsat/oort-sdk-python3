# AdcsTarget

A ground location for the satellite to point at

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | latitide in degrees | 
**lon** | **float** | longitude in degrees | 

## Example

```python
from oort_sdk_client.models.adcs_target import AdcsTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AdcsTarget from a JSON string
adcs_target_instance = AdcsTarget.from_json(json)
# print the JSON string representation of the object
print(AdcsTarget.to_json())

# convert the object into a dict
adcs_target_dict = adcs_target_instance.to_dict()
# create an instance of AdcsTarget from a dict
adcs_target_from_dict = AdcsTarget.from_dict(adcs_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


