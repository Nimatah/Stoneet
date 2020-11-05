import os
import sys

_debug: str = os.getenv("DJANGO_DEBUG", True)

if _debug:
    from .base import *
else:
    from .production import *

if sys.platform != 'linux':
    from .windows import *
