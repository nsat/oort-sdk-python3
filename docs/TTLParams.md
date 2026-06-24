# TTLParams

TTL parameters for a sent item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urgent** | **int** | TTL in seconds for urgent items | [optional] [default to 9000]
**bulk** | **int** | TTL in seconds for bulk items | [optional] [default to 43200]
**surplus** | **int** | TTL in seconds for surplus items | [optional] [default to 172800]

## Example

```python
from oort_sdk_client.models.ttl_params import TTLParams

# TODO update the JSON string below
json = "{}"
# create an instance of TTLParams from a JSON string
ttl_params_instance = TTLParams.from_json(json)
# print the JSON string representation of the object
print(TTLParams.to_json())

# convert the object into a dict
ttl_params_dict = ttl_params_instance.to_dict()
# create an instance of TTLParams from a dict
ttl_params_from_dict = TTLParams.from_dict(ttl_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


