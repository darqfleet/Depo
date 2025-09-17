import pathlib
from exceptions import *

def exist_path(path: str):
    message = f'{path}, not exist'
    if not pathlib.Path(path).exists():
        raise Missing(message)
    return True