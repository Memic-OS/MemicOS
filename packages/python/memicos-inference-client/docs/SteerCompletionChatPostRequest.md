# SteerCompletionChatPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | [**List[NPSteerChatMessage]**](NPSteerChatMessage.md) | Array of chat messages to pass to the model | 
**model** | **str** | Name of the model | 
**steer_method** | [**NPSteerMethod**](NPSteerMethod.md) |  | 
**normalize_steering** | **bool** |  | [default to False]
**types** | [**List[NPSteerType]**](NPSteerType.md) | Array that specifies whether or not to generate STEERED output, DEFAULT (non-steered) output, or both. | 
**features** | [**List[NPSteerFeature]**](NPSteerFeature.md) | Features to steer towards or away from | [optional] 
**vectors** | [**List[NPSteerVector]**](NPSteerVector.md) |  | [optional] 
**n_completion_tokens** | **int** | Number of completion tokens to generate | 
**temperature** | **float** |  | 
**strength_multiplier** | **float** | The steering strength will be multiplied by this number | 
**freq_penalty** | **float** |  | 
**seed** | **float** |  | 
**stream** | **bool** | Whether or not to stream responses using Server Side Events (SSE). Note that the OpenAPI spec does not support SSE - you will receive multiple responses with the same format as non-streaming, except with the \&quot;output\&quot; field chunked. | [optional] [default to False]
**steer_special_tokens** | **bool** |  | [default to True]

## Example

```python
from memicos_inference_client.models.steer_completion_chat_post_request import SteerCompletionChatPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SteerCompletionChatPostRequest from a JSON string
steer_completion_chat_post_request_instance = SteerCompletionChatPostRequest.from_json(json)
# print the JSON string representation of the object
print(SteerCompletionChatPostRequest.to_json())

# convert the object into a dict
steer_completion_chat_post_request_dict = steer_completion_chat_post_request_instance.to_dict()
# create an instance of SteerCompletionChatPostRequest from a dict
steer_completion_chat_post_request_from_dict = SteerCompletionChatPostRequest.from_dict(steer_completion_chat_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


