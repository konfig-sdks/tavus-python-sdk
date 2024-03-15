import typing_extensions

from tavus_python_sdk.paths import PathValues
from tavus_python_sdk.apis.paths.v2_replicas import V2Replicas
from tavus_python_sdk.apis.paths.v2_replicas_replica_id import V2ReplicasReplicaId
from tavus_python_sdk.apis.paths.v2_replicas_replica_id_name import V2ReplicasReplicaIdName
from tavus_python_sdk.apis.paths.v2_videos import V2Videos
from tavus_python_sdk.apis.paths.v2_videos_video_id import V2VideosVideoId
from tavus_python_sdk.apis.paths.v2_videos_video_id_name import V2VideosVideoIdName

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_REPLICAS: V2Replicas,
        PathValues.V2_REPLICAS_REPLICA_ID: V2ReplicasReplicaId,
        PathValues.V2_REPLICAS_REPLICA_ID_NAME: V2ReplicasReplicaIdName,
        PathValues.V2_VIDEOS: V2Videos,
        PathValues.V2_VIDEOS_VIDEO_ID: V2VideosVideoId,
        PathValues.V2_VIDEOS_VIDEO_ID_NAME: V2VideosVideoIdName,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_REPLICAS: V2Replicas,
        PathValues.V2_REPLICAS_REPLICA_ID: V2ReplicasReplicaId,
        PathValues.V2_REPLICAS_REPLICA_ID_NAME: V2ReplicasReplicaIdName,
        PathValues.V2_VIDEOS: V2Videos,
        PathValues.V2_VIDEOS_VIDEO_ID: V2VideosVideoId,
        PathValues.V2_VIDEOS_VIDEO_ID_NAME: V2VideosVideoIdName,
    }
)
