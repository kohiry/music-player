from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from app.player.router import player

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(player)


@app.get('/')
def redir():
    return RedirectResponse('/player/')
