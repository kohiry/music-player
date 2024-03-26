from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.player.schemas import AudioSchema
from app.player.service import get_audios, parse_audio

player = APIRouter(prefix='/player')

templates = Jinja2Templates(directory="templates")


@player.get('/api/next')
def get_next() -> AudioSchema:
    path_audio = next(get_audios())
    answer = parse_audio(path_audio)
    return answer


@player.get('/')
def get_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
