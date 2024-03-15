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


class RequiredVideosCreateVideoFromReplicaAndScriptResponse(TypedDict):
    pass

class OptionalVideosCreateVideoFromReplicaAndScriptResponse(TypedDict, total=False):
    # The date and time the video was created.
    created_at: str

    # A direct link to view your video once generation has completed, hosted by Tavus.
    hosted_url: str

    # The status of the video.
    status: str

    # A unique identifier for the video.
    video_id: str

    # The name of the video.
    video_name: str

class VideosCreateVideoFromReplicaAndScriptResponse(RequiredVideosCreateVideoFromReplicaAndScriptResponse, OptionalVideosCreateVideoFromReplicaAndScriptResponse):
    pass