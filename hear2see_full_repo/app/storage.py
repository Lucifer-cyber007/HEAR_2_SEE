
import os, shutil, uuid, datetime

def save_audio(path):
    os.makedirs("data/input_audio", exist_ok=True)
    ext = os.path.splitext(path)[1]
    name = f"audio_{uuid.uuid4().hex}{ext}"
    dest = f"data/input_audio/{name}"
    shutil.copy2(path,dest)
    return dest
