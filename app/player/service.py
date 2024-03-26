from itertools import cycle
from typing import Iterable
import os


def get_audios() -> Iterable:
    directory = 'static/audio'

    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return cycle(file_paths)
