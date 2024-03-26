from itertools import cycle
import eyed3
from typing import Iterable
import os

from app.player.schemas import AudioSchema


def get_audios() -> Iterable:
    directory = 'static/audio'

    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return cycle(file_paths)


def parse_audio(path: str) -> AudioSchema:
    audio_file = eyed3.load(path)
    artist_name = str(audio_file.tag.artist)
    name = str(audio_file.tag.title)

    if audio_file.tag.images:
        image_data = audio_file.tag.images[0].image_data
    else:
        image_data = None

    return AudioSchema(
        name=name,
        artist=artist_name,
        img=image_data,
        path=path
    )