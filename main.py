from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as UIDI

app = FastAPI(title="CrudBasico", description="Crud Bbasico creado con fastApi")

class publicacion(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


class publicacionID(BaseModel):
    title: str
    author: str
    content: Text
    published: bool = False

lits_posts = []

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}
