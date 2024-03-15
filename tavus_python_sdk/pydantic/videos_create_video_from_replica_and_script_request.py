# coding: utf-8

"""
    Tavus Developer API Collection

    We're an AI video research company making personalized video possible at scale. Generate videos of yourself, and never record again! Available via web app & developer APIs.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class VideosCreateVideoFromReplicaAndScriptRequest(BaseModel):
    # A unique identifier for the replica that will be used to generate the video.
    replica_id: str = Field(alias='replica_id')

    # A script to be used for the video.
    script: str = Field(alias='script')

    # A direct link to a video that is publicly accessible via a storage location such as an S3 bucket. This will be used as the background for the video. The video must be publicly accessible.
    background_source_url: typing.Optional[str] = Field(None, alias='background_source_url')

    # A link to a website. This will be used as the background for the video. The website must be publicly accessible and properly formed.
    background_url: typing.Optional[str] = Field(None, alias='background_url')

    # A name for the video.
    video_name: typing.Optional[str] = Field(None, alias='video_name')
    class Config:
        arbitrary_types_allowed = True
