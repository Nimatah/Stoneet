import os
import sys

_debug: bool = os.getenv("DJANGO_DEBUG", True)
_staging: bool = os.getenv("DJANGO_STAGING", False)

if _staging:
    from .staging import *
elif _debug:
    from .base import *
else:
    from .production import *

if sys.platform != 'linux':
    from .windows import *
