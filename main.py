from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI, HTTPException , status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from uuid import uuid4 as UIDI

app = FastAPI(title="CrudBasico", description="Crud Bbasico creado con fastApi")

class publicacion(BaseModel):
    id: str
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
    """
    Root endpoint to test if the API is running.
    """
    return {"message": "Hola Mundo"}

@app.get("/posts")
async def get_post():
    """
    Get all posts.

    Returns:
        List[publicacion]: List of all posts.

    Raises:
        HTTPException: 404 status code if there are no posts to show.
    """
    if lits_posts:
        return lits_posts
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="No hay publicaciones que mostrar" )

@app.get("/post/{id}")
async def get_post(id: str):
    """
    Get a specific post by ID.

    Args:
        id (str): ID of the post to retrieve.

    Returns:
        publicacion: Post information.

    Raises:
        HTTPException: 404 status code if the post with the specified ID is not found.
    """
    for post in lits_posts:
        if post["id"] == id:
            post_dict = dict(post)  # Convert the dictionary view to a dictionary
            return publicacion(**post_dict)  # Create a new instance of the publicacion class with the dictionary values
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Publicación con ID: {id} no encontrada")

@app.post("/posts")
async def save_post(post_id: publicacionID):
    """
    Save a new post.

    Args:
        post_id (publicacionID): Post information without an ID.

    Returns:
        publicacion: Newly created post.

    Raises:
        HTTPException: 400 status code if the post cannot be created.
    """
    post = publicacion(**dict(post_id), id=str(UIDI()), published_at=datetime.now())
    if post:
        lits_posts.append(post.dict())
        return lits_posts[-1]
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se ha podido crear la publicacion")

@app.delete("/posts")
async def delete_posts (id:str):
    """
        Delete a post by ID.

        Args:
            id (str): ID of the post to delete.

        Raises:
            HTTPException:
                - 404 status code if the post with the specified ID is not found.
                - 302 status code if the post is successfully deleted.
    """
    for post in lits_posts:
        if post.get("id") == id:
            lits_posts.remove(post)
            raise HTTPException(status_code= status.HTTP_302_FOUND, detail=f"Publicacion con ID: {id} eliminado")
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Publicacion con ID: {id} no encontrada")

@app.put("/posts")
async def add_Post(post : publicacionID, id:str):
    """
    Update a post by ID.

    Args:
        post (publicacionID): Updated post information without an ID.
        id (str): ID of the post to update.

    Returns:
        JSONResponse: Success message.

    Raises:
        HTTPException: 404 status code if the post with the specified ID is not found.
    """
    for i, public  in enumerate(lits_posts):
        if public.get("id") == id:
            lits_posts[i] = dict(publicacion(**dict(post), id=str(id), published_at=datetime.now()))
            return JSONResponse(content={"message": "producto actualizado correctamente"})
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Publicacion con ID: {id} no encontrada")
