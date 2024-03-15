import typing_extensions

from tavus_python_sdk.apis.tags import TagValues
from tavus_python_sdk.apis.tags.videos_api import VideosApi
from tavus_python_sdk.apis.tags.replicas_api import ReplicasApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VIDEOS: VideosApi,
        TagValues.REPLICAS: ReplicasApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VIDEOS: VideosApi,
        TagValues.REPLICAS: ReplicasApi,
    }
)
