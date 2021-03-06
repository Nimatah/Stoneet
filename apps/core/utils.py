import base64
import os
import uuid
from datetime import datetime


def get_file_path(directory: str, filename: str) -> str:
    now = datetime.now()
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(f'{directory}/{now.year}/{now.month}', filename)


def from_base64(b64):
    return base64.b64decode(b64)
