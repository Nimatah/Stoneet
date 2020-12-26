import os
import sys

_local: str = os.getenv("DJANGO_LOCAL", True)
_debug: str = os.getenv("DJANGO_DEBUG", True)

if _local:
    from .base import *
elif _debug:
    from .staging import *
else:
    from .production import *

if sys.platform != 'linux':
    from .windows import *
