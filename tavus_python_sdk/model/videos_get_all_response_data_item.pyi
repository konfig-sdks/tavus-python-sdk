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


class VideosGetAllResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            background_source_url = schemas.StrSchema
            background_url = schemas.StrSchema
            replica_id = schemas.StrSchema
            script = schemas.StrSchema
            video_name = schemas.StrSchema
            __annotations__ = {
                "background_source_url": background_source_url,
                "background_url": background_url,
                "replica_id": replica_id,
                "script": script,
                "video_name": video_name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["background_source_url"]) -> MetaOapg.properties.background_source_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["background_url"]) -> MetaOapg.properties.background_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replica_id"]) -> MetaOapg.properties.replica_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["video_name"]) -> MetaOapg.properties.video_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["background_source_url", "background_url", "replica_id", "script", "video_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["background_source_url"]) -> typing.Union[MetaOapg.properties.background_source_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["background_url"]) -> typing.Union[MetaOapg.properties.background_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replica_id"]) -> typing.Union[MetaOapg.properties.replica_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["script"]) -> typing.Union[MetaOapg.properties.script, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["video_name"]) -> typing.Union[MetaOapg.properties.video_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["background_source_url", "background_url", "replica_id", "script", "video_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        background_source_url: typing.Union[MetaOapg.properties.background_source_url, str, schemas.Unset] = schemas.unset,
        background_url: typing.Union[MetaOapg.properties.background_url, str, schemas.Unset] = schemas.unset,
        replica_id: typing.Union[MetaOapg.properties.replica_id, str, schemas.Unset] = schemas.unset,
        script: typing.Union[MetaOapg.properties.script, str, schemas.Unset] = schemas.unset,
        video_name: typing.Union[MetaOapg.properties.video_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideosGetAllResponseDataItem':
        return super().__new__(
            cls,
            *args,
            background_source_url=background_source_url,
            background_url=background_url,
            replica_id=replica_id,
            script=script,
            video_name=video_name,
            _configuration=_configuration,
            **kwargs,
        )