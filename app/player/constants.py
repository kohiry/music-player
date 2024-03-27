from starlette.templating import Jinja2Templates

from app.player.service import get_audios, gen_path_audio

templates = Jinja2Templates(directory="templates")
audios = get_audios()
gen = gen_path_audio(audios)
