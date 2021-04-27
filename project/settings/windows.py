from .base import *


HUEY = {
    'huey_class': 'huey.MemoryHuey',
    'name': "plantask",
    'results': True,
    'store_none': False,
    'immediate': False,
    'utc': False,
    'blocking': True,
    'consumer': {
        'workers': 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,
        'backoff': 1.15,
        'max_delay': 10.0,
        'scheduler_interval': 1,
        'periodic': True,
        'check_worker_health': True,
        'health_check_interval': 1,
    },
}
