# coding: utf-8

"""
    Onfido API v3.6

    The Onfido API (v3.6)

    The version of the OpenAPI document: v3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ReportName(str, Enum):
    """
    ReportName
    """

    """
    allowed enum values
    """
    DOCUMENT = 'document'
    DOCUMENT_VIDEO = 'document_video'
    DOCUMENT_VIDEO_WITH_ADDRESS_INFORMATION = 'document_video_with_address_information'
    DOCUMENT_WITH_ADDRESS_INFORMATION = 'document_with_address_information'
    DOCUMENT_WITH_DRIVING_LICENCE_INFORMATION = 'document_with_driving_licence_information'
    DOCUMENT_WITH_DRIVER_VERIFICATION = 'document_with_driver_verification'
    FACIAL_SIMILARITY_PHOTO = 'facial_similarity_photo'
    FACIAL_SIMILARITY_PHOTO_FULLY_AUTO = 'facial_similarity_photo_fully_auto'
    FACIAL_SIMILARITY_VIDEO = 'facial_similarity_video'
    FACIAL_SIMILARITY_MOTION = 'facial_similarity_motion'
    KNOWN_FACES = 'known_faces'
    IDENTITY_ENHANCED = 'identity_enhanced'
    WATCHLIST_AML = 'watchlist_aml'
    WATCHLIST_ENHANCED = 'watchlist_enhanced'
    WATCHLIST_STANDARD = 'watchlist_standard'
    WATCHLIST_PEPS_ONLY = 'watchlist_peps_only'
    WATCHLIST_SANCTIONS_ONLY = 'watchlist_sanctions_only'
    PROOF_OF_ADDRESS = 'proof_of_address'
    US_DRIVING_LICENCE = 'us_driving_licence'
    DEVICE_INTELLIGENCE = 'device_intelligence'
    INDIA_PAN = 'india_pan'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReportName from a JSON string"""
        return cls(json.loads(json_str))

