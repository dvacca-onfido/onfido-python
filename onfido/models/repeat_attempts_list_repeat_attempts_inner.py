# coding: utf-8

"""
    Onfido API v3.6

    The Onfido API (v3.6)

    The version of the OpenAPI document: v3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RepeatAttemptsListRepeatAttemptsInner(BaseModel):
    """
    RepeatAttemptsListRepeatAttemptsInner
    """ # noqa: E501
    report_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the matching Document report.")
    applicant_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the applicant for the matching Document report.")
    date_of_birth: Optional[StrictStr] = Field(default=None, description="Whether the dates of birth are exactly the same or are different.")
    names: Optional[StrictStr] = Field(default=None, description="Whether the names are exactly the same or are different.")
    result: Optional[StrictStr] = Field(default=None, description="The report result of this attempt.")
    created_at: Optional[datetime] = Field(default=None, description="When the matching report was created.")
    completed_at: Optional[datetime] = Field(default=None, description="When the matching report was completed.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["report_id", "applicant_id", "date_of_birth", "names", "result", "created_at", "completed_at"]

    @field_validator('date_of_birth')
    def date_of_birth_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['match', 'mismatch']):
            raise ValueError("must be one of enum values ('match', 'mismatch')")
        return value

    @field_validator('names')
    def names_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['match', 'mismatch']):
            raise ValueError("must be one of enum values ('match', 'mismatch')")
        return value

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['clear', 'consider']):
            raise ValueError("must be one of enum values ('clear', 'consider')")
        return value

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
        """Create an instance of RepeatAttemptsListRepeatAttemptsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RepeatAttemptsListRepeatAttemptsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "report_id": obj.get("report_id"),
            "applicant_id": obj.get("applicant_id"),
            "date_of_birth": obj.get("date_of_birth"),
            "names": obj.get("names"),
            "result": obj.get("result"),
            "created_at": obj.get("created_at"),
            "completed_at": obj.get("completed_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

