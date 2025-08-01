# coding: utf-8

"""
    MemicOS - Inference Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1.0
    Contact: johnny@memicos.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from memicos_inference_client.models.np_steer_feature import NPSteerFeature
from memicos_inference_client.models.np_steer_method import NPSteerMethod
from memicos_inference_client.models.np_steer_type import NPSteerType
from memicos_inference_client.models.np_steer_vector import NPSteerVector
from typing import Optional, Set
from typing_extensions import Self

class SteerCompletionRequest(BaseModel):
    """
    Base request for steering
    """ # noqa: E501
    prompt: StrictStr = Field(description="Text to pass the model for completion")
    model: StrictStr = Field(description="Name of the model")
    steer_method: NPSteerMethod
    normalize_steering: StrictBool
    types: Annotated[List[NPSteerType], Field(min_length=1)] = Field(description="Array that specifies whether or not to generate STEERED output, DEFAULT (non-steered) output, or both.")
    features: Optional[List[NPSteerFeature]] = Field(default=None, description="Features to steer towards or away from")
    vectors: Optional[List[NPSteerVector]] = None
    n_completion_tokens: Annotated[int, Field(strict=True, ge=1)] = Field(description="Number of completion tokens to generate")
    temperature: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]
    strength_multiplier: Union[StrictFloat, StrictInt] = Field(description="The steering strength will be multiplied by this number")
    freq_penalty: Union[StrictFloat, StrictInt]
    seed: Union[StrictFloat, StrictInt]
    stream: Optional[StrictBool] = Field(default=False, description="Whether or not to stream responses using Server Side Events (SSE). Note that the OpenAPI spec does not support SSE - you will receive multiple responses with the same format as non-streaming, except with the \"output\" field chunked.")
    __properties: ClassVar[List[str]] = ["prompt", "model", "steer_method", "normalize_steering", "types", "features", "vectors", "n_completion_tokens", "temperature", "strength_multiplier", "freq_penalty", "seed", "stream"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SteerCompletionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vectors (list)
        _items = []
        if self.vectors:
            for _item_vectors in self.vectors:
                if _item_vectors:
                    _items.append(_item_vectors.to_dict())
            _dict['vectors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SteerCompletionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prompt": obj.get("prompt"),
            "model": obj.get("model"),
            "steer_method": obj.get("steer_method"),
            "normalize_steering": obj.get("normalize_steering") if obj.get("normalize_steering") is not None else False,
            "types": obj.get("types"),
            "features": [NPSteerFeature.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "vectors": [NPSteerVector.from_dict(_item) for _item in obj["vectors"]] if obj.get("vectors") is not None else None,
            "n_completion_tokens": obj.get("n_completion_tokens"),
            "temperature": obj.get("temperature"),
            "strength_multiplier": obj.get("strength_multiplier"),
            "freq_penalty": obj.get("freq_penalty"),
            "seed": obj.get("seed"),
            "stream": obj.get("stream") if obj.get("stream") is not None else False
        })
        return _obj


