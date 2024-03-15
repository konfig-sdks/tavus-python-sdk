operation_parameter_map = {
    '/v2/replicas-POST': {
        'parameters': [
            {
                'name': 'train_video_url'
            },
            {
                'name': 'callback_url'
            },
            {
                'name': 'replica_name'
            },
        ]
    },
    '/v2/replicas/{replica_id}-DELETE': {
        'parameters': [
            {
                'name': 'replica_id'
            },
        ]
    },
    '/v2/replicas/{replica_id}-GET': {
        'parameters': [
            {
                'name': 'replica_id'
            },
        ]
    },
    '/v2/replicas-GET': {
        'parameters': [
        ]
    },
    '/v2/replicas/{replica_id}/name-PATCH': {
        'parameters': [
            {
                'name': 'replica_name'
            },
            {
                'name': 'replica_id'
            },
        ]
    },
    '/v2/videos-POST': {
        'parameters': [
            {
                'name': 'replica_id'
            },
            {
                'name': 'script'
            },
            {
                'name': 'background_source_url'
            },
            {
                'name': 'background_url'
            },
            {
                'name': 'video_name'
            },
        ]
    },
    '/v2/videos/{video_id}-DELETE': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/v2/videos-GET': {
        'parameters': [
        ]
    },
    '/v2/videos/{video_id}-GET': {
        'parameters': [
            {
                'name': 'video_id'
            },
        ]
    },
    '/v2/videos/{video_id}/name-PATCH': {
        'parameters': [
            {
                'name': 'video_name'
            },
            {
                'name': 'video_id'
            },
        ]
    },
};