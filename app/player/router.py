from fastapi import APIRouter
from fastapi import Request

from app.player.constants import templates, gen
from app.player.schemas import AudioSchema
from app.player.service import parse_audio

player = APIRouter(prefix='/player')


@player.get('/api/next')
def get_next() -> AudioSchema:
    path_audio: str = next(gen)
    answer = parse_audio(path_audio)
    return answer


@player.get('/')
def get_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
