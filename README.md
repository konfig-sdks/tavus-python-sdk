<div align="left">

[![Visit Tavus](./header.png)](https://www.tavus.io&#x2F;)

# Tavus<a id="tavus"></a>

We're an AI video research company making personalized video possible at scale. Generate videos of yourself, and never record again! Available via web app & developer APIs.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`tavus.replicas.create_new_replica`](#tavusreplicascreate_new_replica)
  * [`tavus.replicas.delete_by_replica_id`](#tavusreplicasdelete_by_replica_id)
  * [`tavus.replicas.get_replica_by_id`](#tavusreplicasget_replica_by_id)
  * [`tavus.replicas.list`](#tavusreplicaslist)
  * [`tavus.replicas.rename_replica_by_id`](#tavusreplicasrename_replica_by_id)
  * [`tavus.videos.create_video_from_replica_and_script`](#tavusvideoscreate_video_from_replica_and_script)
  * [`tavus.videos.delete_by_video_id`](#tavusvideosdelete_by_video_id)
  * [`tavus.videos.get_all`](#tavusvideosget_all)
  * [`tavus.videos.get_by_video_id`](#tavusvideosget_by_video_id)
  * [`tavus.videos.update_name`](#tavusvideosupdate_name)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Tavus&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from tavus_python_sdk import Tavus, ApiException

tavus = Tavus(
    api_key="YOUR_API_KEY",
)

try:
    # Create Replica
    create_new_replica_response = tavus.replicas.create_new_replica(
        train_video_url="string_example",
        callback_url="string_example",
        replica_name="string_example",
    )
    print(create_new_replica_response)
except ApiException as e:
    print("Exception when calling ReplicasApi.create_new_replica: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from tavus_python_sdk import Tavus, ApiException

tavus = Tavus(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Create Replica
        create_new_replica_response = await tavus.replicas.acreate_new_replica(
            train_video_url="string_example",
            callback_url="string_example",
            replica_name="string_example",
        )
        print(create_new_replica_response)
    except ApiException as e:
        print("Exception when calling ReplicasApi.create_new_replica: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from tavus_python_sdk import Tavus, ApiException

tavus = Tavus(
    api_key="YOUR_API_KEY",
)

try:
    # Create Replica
    create_new_replica_response = tavus.replicas.raw.create_new_replica(
        train_video_url="string_example",
        callback_url="string_example",
        replica_name="string_example",
    )
    pprint(create_new_replica_response.body)
    pprint(create_new_replica_response.body["replica_id"])
    pprint(create_new_replica_response.body["status"])
    pprint(create_new_replica_response.headers)
    pprint(create_new_replica_response.status)
    pprint(create_new_replica_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ReplicasApi.create_new_replica: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `tavus.replicas.create_new_replica`<a id="tavusreplicascreate_new_replica"></a>

This endpoint creates a new Replica that can be used to generate personalized videos. 

The only required body parameter is `train_video_url`. This url must be a download link such as a presigned S3 url. Please ensure you pass in a video that meets the [requirements](https://docs.tavusapi.com/api-reference) for training.

Replica training will fail without the following consent statement being present at the beginning of the video:
> I, [FULL NAME], am currently speaking and consent Tavus to create an AI clone of me by using the audio and video samples I provide. I understand that this AI clone can be used to create videos that look and sound like me.

Learn more about the consent statement [here](https://docs.tavusapi.com/api-reference).

Learn more about training a personal Replica [here](https://docs.tavusapi.com/api-reference).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_replica_response = tavus.replicas.create_new_replica(
    train_video_url="string_example",
    callback_url="string_example",
    replica_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### train_video_url: `str`<a id="train_video_url-str"></a>

A direct link to a publicly accessible storage location such as an S3 bucket. This video will be used for replica training.

##### callback_url: `str`<a id="callback_url-str"></a>

A url that will receive a callback on completion of replica training or on error.

##### replica_name: `str`<a id="replica_name-str"></a>

A name for the replica.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReplicasCreateNewReplicaRequest`](./tavus_python_sdk/type/replicas_create_new_replica_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReplicasCreateNewReplicaResponse`](./tavus_python_sdk/pydantic/replicas_create_new_replica_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/replicas` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.replicas.delete_by_replica_id`<a id="tavusreplicasdelete_by_replica_id"></a>

This endpoint deletes a single Replica by its unique identifier. Once deleted, this Replica can not be used to generate videos.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tavus.replicas.delete_by_replica_id(
    replica_id="replica_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### replica_id: `str`<a id="replica_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/replicas/{replica_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.replicas.get_replica_by_id`<a id="tavusreplicasget_replica_by_id"></a>

This endpoint returns a single Replica by its unique identifier. 

Included in the response body is a `training_progress` string that represents the progress of the Replica training. If there are any errors during training, the `status` will be `error` and the `error_message` will be populated.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_replica_by_id_response = tavus.replicas.get_replica_by_id(
    replica_id="replica_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### replica_id: `str`<a id="replica_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReplicasGetReplicaByIdResponse`](./tavus_python_sdk/pydantic/replicas_get_replica_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/replicas/{replica_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.replicas.list`<a id="tavusreplicaslist"></a>

This endpoint returns a list of all replicas that have been created by the API Key in use. In the response, a root level `data` key will contain the list of Replicas.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = tavus.replicas.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ReplicasListResponse`](./tavus_python_sdk/pydantic/replicas_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/replicas` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.replicas.rename_replica_by_id`<a id="tavusreplicasrename_replica_by_id"></a>

This endpoint renames a single Replica by its unique identifier. 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tavus.replicas.rename_replica_by_id(
    replica_name="string_example",
    replica_id="replica_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### replica_name: `str`<a id="replica_name-str"></a>

##### replica_id: `str`<a id="replica_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReplicasRenameReplicaByIdRequest`](./tavus_python_sdk/type/replicas_rename_replica_by_id_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/replicas/{replica_id}/name` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.videos.create_video_from_replica_and_script`<a id="tavusvideoscreate_video_from_replica_and_script"></a>

This endpoint generates a new video using a Replica and a script. 

The only required body parameters are `replica_id` and `script`. The `replica_id` is a unique identifier for the Replica that will be used to generate the video. The `script` is the text that will be spoken by the Replica in the video.

If a `background_url` is provided, Tavus will record a video of the website and use it as the background for the video. If a `background_source_url` is provided, where the URL points to a download link such as a presigned S3 URL, Tavus will use the video as the background for the video. If neither are provided, the video will consist of a full screen Replica.

To learn more about generating videos with Replicas, see [here](https://docs.tavusapi.com/api-reference).

To learn more about writing an effective script for your video, see [Scripting prompting](https://docs.tavusapi.com/api-reference).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_video_from_replica_and_script_response = (
    tavus.videos.create_video_from_replica_and_script(
        replica_id="r783537ef5",
        script="Hello from Tavus! Enjoy your new replica",
        background_source_url="string_example",
        background_url="string_example",
        video_name="My First Video",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### replica_id: `str`<a id="replica_id-str"></a>

A unique identifier for the replica that will be used to generate the video.

##### script: `str`<a id="script-str"></a>

A script to be used for the video.

##### background_source_url: `str`<a id="background_source_url-str"></a>

A direct link to a video that is publicly accessible via a storage location such as an S3 bucket. This will be used as the background for the video. The video must be publicly accessible.

##### background_url: `str`<a id="background_url-str"></a>

A link to a website. This will be used as the background for the video. The website must be publicly accessible and properly formed.

##### video_name: `str`<a id="video_name-str"></a>

A name for the video.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideosCreateVideoFromReplicaAndScriptRequest`](./tavus_python_sdk/type/videos_create_video_from_replica_and_script_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VideosCreateVideoFromReplicaAndScriptResponse`](./tavus_python_sdk/pydantic/videos_create_video_from_replica_and_script_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.videos.delete_by_video_id`<a id="tavusvideosdelete_by_video_id"></a>

This endpoint deletes a single video by its unique identifier.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tavus.videos.delete_by_video_id(
    video_id="video_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/{video_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.videos.get_all`<a id="tavusvideosget_all"></a>

This endpoint returns a list of all videos that have been generated by the API Key in use. 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = tavus.videos.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`VideosGetAllResponse`](./tavus_python_sdk/pydantic/videos_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.videos.get_by_video_id`<a id="tavusvideosget_by_video_id"></a>

This endpoint returns a single video by its unique identifier. 

The response body will contain a `status` string that represents the status of the video. If the video is ready, the response body will also contain a `download_url`, `stream_url`, and `hosted_url` that can be used to download, stream, and view the video respectively.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_video_id_response = tavus.videos.get_by_video_id(
    video_id="video_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VideosGetByVideoIdResponse`](./tavus_python_sdk/pydantic/videos_get_by_video_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/{video_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `tavus.videos.update_name`<a id="tavusvideosupdate_name"></a>

This endpoint renames a single video by its unique identifier.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tavus.videos.update_name(
    video_name="string_example",
    video_id="video_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_name: `str`<a id="video_name-str"></a>

##### video_id: `str`<a id="video_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideosUpdateNameRequest`](./tavus_python_sdk/type/videos_update_name_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/videos/{video_id}/name` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
