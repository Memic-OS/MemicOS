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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ActivationTopkByTokenPostRequest(BaseModel):
    """
    Get activations for either a specific feature in an SAE (specified by \"source\" + \"index\") or a custom vector (specified by \"vector\" + \"hook\")
    """ # noqa: E501
    prompt: StrictStr = Field(description="Input text prompt to get activations for")
    model: StrictStr = Field(description="Name of the model to test activations on")
    source: StrictStr = Field(description="Source identifier - could be an SAE ID (eg 5-gemmascope-res-16k). Must be specified with \"index\", or not at NPActivationAllRequest.")
    top_k: Optional[StrictInt] = Field(default=None, description="The number of features to include for each token position.")
    ignore_bos: StrictBool = Field(description="Whether or not to include features whose highest activation value is the BOS token.")
    __properties: ClassVar[List[str]] = ["prompt", "model", "source", "top_k", "ignore_bos"]

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
        """Create an instance of ActivationTopkByTokenPostRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActivationTopkByTokenPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prompt": obj.get("prompt"),
            "model": obj.get("model"),
            "source": obj.get("source"),
            "top_k": obj.get("top_k"),
            "ignore_bos": obj.get("ignore_bos") if obj.get("ignore_bos") is not None else True
        })
        return _obj


