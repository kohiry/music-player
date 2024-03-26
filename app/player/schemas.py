from pydantic import BaseModel


class AudioSchema(BaseModel):
    path: str
    img: bytes | None
    name: str
    artist: str

