import base64
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


def gen_path_audio(audios: Iterable) -> str:
    for audio in audios:
        yield audio


def parse_audio(path: str) -> AudioSchema:
    audio_file = eyed3.load(path)
    print(audio_file, '\n\n')
    artist_name = str(audio_file.tag.artist)
    name = str(audio_file.tag.title)

    image_data = None
    if audio_file.tag.images:
        image_data = base64.b64encode(audio_file.tag.images[0].image_data).decode('utf-8')

    return AudioSchema(
        name=name,
        artist=artist_name,
        img=image_data,
        path=path
    )

