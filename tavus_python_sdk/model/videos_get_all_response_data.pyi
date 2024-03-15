# coding: utf-8

"""
    Tavus Developer API Collection

    We're an AI video research company making personalized video possible at scale. Generate videos of yourself, and never record again! Available via web app & developer APIs.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from tavus_python_sdk import schemas  # noqa: F401


class VideosGetAllResponseData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['VideosGetAllResponseDataItem']:
            return VideosGetAllResponseDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['VideosGetAllResponseDataItem'], typing.List['VideosGetAllResponseDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VideosGetAllResponseData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'VideosGetAllResponseDataItem':
        return super().__getitem__(i)

from tavus_python_sdk.model.videos_get_all_response_data_item import VideosGetAllResponseDataItem