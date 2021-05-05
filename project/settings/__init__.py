import os
import sys

DJANGO_ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT", 'dev')

if DJANGO_ENVIRONMENT == 'dev':
    from .base import *
elif DJANGO_ENVIRONMENT == 'staging':
    from .staging import *
elif DJANGO_ENVIRONMENT == 'prod':
    from .production import *
else:
    from .base import *

if sys.platform != 'linux':
    from .windows import *
