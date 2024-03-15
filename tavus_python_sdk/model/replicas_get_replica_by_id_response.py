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


class ReplicasGetReplicaByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            created_at = schemas.StrSchema
            
            
            class error_message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            replica_id = schemas.StrSchema
            replica_name = schemas.StrSchema
            status = schemas.StrSchema
            thumbnail_video_url = schemas.StrSchema
            training_progress = schemas.StrSchema
            updated_at = schemas.StrSchema
            __annotations__ = {
                "created_at": created_at,
                "error_message": error_message,
                "replica_id": replica_id,
                "replica_name": replica_name,
                "status": status,
                "thumbnail_video_url": thumbnail_video_url,
                "training_progress": training_progress,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_message"]) -> MetaOapg.properties.error_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replica_id"]) -> MetaOapg.properties.replica_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replica_name"]) -> MetaOapg.properties.replica_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail_video_url"]) -> MetaOapg.properties.thumbnail_video_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["training_progress"]) -> MetaOapg.properties.training_progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "error_message", "replica_id", "replica_name", "status", "thumbnail_video_url", "training_progress", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_message"]) -> typing.Union[MetaOapg.properties.error_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replica_id"]) -> typing.Union[MetaOapg.properties.replica_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replica_name"]) -> typing.Union[MetaOapg.properties.replica_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail_video_url"]) -> typing.Union[MetaOapg.properties.thumbnail_video_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["training_progress"]) -> typing.Union[MetaOapg.properties.training_progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "error_message", "replica_id", "replica_name", "status", "thumbnail_video_url", "training_progress", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        error_message: typing.Union[MetaOapg.properties.error_message, None, str, schemas.Unset] = schemas.unset,
        replica_id: typing.Union[MetaOapg.properties.replica_id, str, schemas.Unset] = schemas.unset,
        replica_name: typing.Union[MetaOapg.properties.replica_name, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        thumbnail_video_url: typing.Union[MetaOapg.properties.thumbnail_video_url, str, schemas.Unset] = schemas.unset,
        training_progress: typing.Union[MetaOapg.properties.training_progress, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReplicasGetReplicaByIdResponse':
        return super().__new__(
            cls,
            *args,
            created_at=created_at,
            error_message=error_message,
            replica_id=replica_id,
            replica_name=replica_name,
            status=status,
            thumbnail_video_url=thumbnail_video_url,
            training_progress=training_progress,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )