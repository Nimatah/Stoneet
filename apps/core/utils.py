import os
import uuid


def get_file_path(directory: str, filename: str) -> str:
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(directory, filename)
