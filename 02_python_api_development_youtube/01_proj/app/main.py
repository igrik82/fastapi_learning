"""First project"""
from typing import Optional
from psycopg.rows import dict_row
from pydantic import BaseModel
import psycopg
from fastapi import Depends, FastAPI, Response, status, HTTPException
import models
from database import engine, get_db
from sqlalchemy.orm import Session

# Create table
models.Poster.metadata.create_all(bind=engine)

app = FastAPI()


class Poster_pydantic(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = 2


try:
    conn = psycopg.connect(
        host="192.168.88.226",
        dbname="posts",
        user="fastapi",
        password="123456",
        row_factory=dict_row,
    )
    cursor = conn.cursor()
    print("Database connection was succesfull!")

except Exception as er:
    print("Connection failed...")
    print("Error: ", er)


# Storing data in lists
my_posts = [
    {"title": "title of post1", "content": "content post 1", "id": 1},
    {"title": "title of post2", "content": "content post 2", "id": 2},
    {"title": "title of post3", "content": "content post 3", "id": 3},
]


def find_post(post_id):
    for post in my_posts:
        print(post["id"])
        if post["id"] == post_id:
            return post
    return None


def find_index_by_id(post_id):
    for index, post in enumerate(my_posts):
        if post["id"] == post_id:
            return index
    return None


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(user_post: Poster_pydantic, db: Session = Depends(get_db)):
    new_post = models.Poster(**user_post.dict())

    db.add(new_post)
    db.commit()
    # return back post
    db.refresh(new_post)

    return {"Post": new_post}


@app.get("/posts")
def show_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Poster).all()
    return {"Posts": posts}


@app.get("/posts/latest")
def show_last_post(db: Session = Depends(get_db)):
    post_query = db.query(models.Poster)
    index: int = post_query.count()
    post = post_query.where(models.Poster.id == index).first()
    return {"Post": post}


@app.get("/posts/{post_id}")
def show_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Poster).filter(models.Poster.id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Post": f"Post with id: {post_id} not found"},
        )
    return {"Post": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Poster).filter(models.Poster.id == post_id)
    if post_query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}", status_code=status.HTTP_202_ACCEPTED)
def udate_post(
    post_id: int, user_post: Poster_pydantic, db: Session = Depends(get_db)
):
    post_query = db.query(models.Poster).filter(models.Poster.id == post_id)
    old_post = post_query.first()

    if old_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    post_query.update(user_post.dict(), synchronize_session=False)
    db.commit()

    return {"message": post_query.first()}
