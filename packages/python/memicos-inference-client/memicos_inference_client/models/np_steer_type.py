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
import json
from enum import Enum
from typing_extensions import Self


class NPSteerType(str, Enum):
    """
    NPSteerType
    """

    """
    allowed enum values
    """
    STEERED = 'STEERED'
    DEFAULT = 'DEFAULT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NPSteerType from a JSON string"""
        return cls(json.loads(json_str))


