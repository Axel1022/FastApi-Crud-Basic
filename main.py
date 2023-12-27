from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI, HTTPException , status
from fastapi.responses import JSONResponse
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
async def read_root():
    return {"message": "Hola Mundo"}

@app.get("/posts")
async def get_post():
    if lits_posts:
        return lits_posts
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="No hay publicaciones que mostrar" )

@app.get("/post/{id}")
async def get_post(id:str):
    for post in lits_posts:
        if post.get("id") == id:
            return post
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)

@app.post("/posts")
async def save_post(post_id: publicacionID):
    post = publicacion(**dict(post_id), id=str(UIDI()), published_at=datetime.now())
    if post:
        lits_posts.append(post.dict())
        return lits_posts[-1]
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se ha podido crear la publicacion")

@app.delete("/posts")
async def delete_posts (id:str):
    for post in lits_posts:
        if post.get("id") == id:
            lits_posts.remove(post)
            raise HTTPException(status_code= status.HTTP_302_FOUND, detail=f"Publicacion con ID: {id} eliminado")
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Publicacion con ID: {id} no encontrada")

@app.put("/posts")
async def add_Post(post : publicacionID, id:str):
    for i, public  in enumerate(lits_posts):
        if public.get("id") == id:
            lits_posts[i] = publicacion(**dict(post), id=str(id), published_at=datetime.now())
            return JSONResponse(content={"message": "producto actualizado correctamente"})
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Publicacion con ID: {id} no encontrada")
