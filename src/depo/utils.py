import pathlib
from exceptions import *
from pathlib import Path

def exist_path(path: Path):
    message = f'{path}, not exist'
    if not path.exists():
        raise Missing(message)
    return True