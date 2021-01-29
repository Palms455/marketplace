import os
import uuid

# куда загружать файл, каждый раз гарантированно новое место
def get_upload_dir(_, filename):
    return os.path.join("images", "board", str(uuid.uuid4()), filename)