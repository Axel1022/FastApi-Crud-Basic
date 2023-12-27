from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI, HTTPException , status
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

@app.get("/posts")
def get_post():
    if lits_posts:
        return lits_posts
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="No hay publicaciones que mostrar" )

@app.get("/post/{id}")
def get_post(id:str):
    for post in lits_posts:
        if post.get("id") == id:
            return post
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)

@app.post("/posts")
def save_post(post_id: publicacionID):
    post = publicacion(**dict(post_id), id=str(UIDI()), published_at=datetime.now())
    if post:
        lits_posts.append(post.dict())
        return lits_posts[-1]
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se ha podido crear la publicacion")

@app.delete("/posts")
def delete_posts (id:str):
    for post in lits_posts:
        if post.get("id") == id:
            publicacion = post
            lits_posts.remove(publicacion)
            raise HTTPException(status_code= status.HTTP_302_FOUND, detail=f"Publicacion con ID: {id} eliminado")
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Publicacion con ID: {id} no encontrada")
