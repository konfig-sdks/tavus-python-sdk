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


class ReplicasCreateNewReplicaRequest(BaseModel):
    # A direct link to a publicly accessible storage location such as an S3 bucket. This video will be used for replica training.
    train_video_url: str = Field(alias='train_video_url')

    # A url that will receive a callback on completion of replica training or on error.
    callback_url: typing.Optional[str] = Field(None, alias='callback_url')

    # A name for the replica.
    replica_name: typing.Optional[str] = Field(None, alias='replica_name')
    class Config:
        arbitrary_types_allowed = True