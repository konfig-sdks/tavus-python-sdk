# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from tavus_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_REPLICAS = "/v2/replicas"
    V2_REPLICAS_REPLICA_ID = "/v2/replicas/{replica_id}"
    V2_REPLICAS_REPLICA_ID_NAME = "/v2/replicas/{replica_id}/name"
    V2_VIDEOS = "/v2/videos"
    V2_VIDEOS_VIDEO_ID = "/v2/videos/{video_id}"
    V2_VIDEOS_VIDEO_ID_NAME = "/v2/videos/{video_id}/name"
