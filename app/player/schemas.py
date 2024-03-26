from pydantic import BaseModel


class AudioSchema(BaseModel):
    path: str

