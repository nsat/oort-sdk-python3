# DeliveryHints

Delivery hints used to inform the reveiver about the expected destination of the file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_path** | **str** | Path of the file on the destination filesystem | 
**mode** | **str** | File mode in octal form. For example: \&quot;760\&quot; means that the user can read+write+execute, the group can read+write, and others have no access  | 

## Example

```python
from oort_sdk_client.models.delivery_hints import DeliveryHints

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryHints from a JSON string
delivery_hints_instance = DeliveryHints.from_json(json)
# print the JSON string representation of the object
print(DeliveryHints.to_json())

# convert the object into a dict
delivery_hints_dict = delivery_hints_instance.to_dict()
# create an instance of DeliveryHints from a dict
delivery_hints_from_dict = DeliveryHints.from_dict(delivery_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


