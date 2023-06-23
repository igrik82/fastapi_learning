"""First project"""
from random import randint
from typing import Optional
from psycopg.rows import dict_row
from pydantic import BaseModel
import psycopg
from fastapi import FastAPI, Response, status, HTTPException

app = FastAPI()


class Poster(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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
def create_post(
    user_post: Poster,
):
    post = user_post.dict()
    if not post["id"]:
        post["id"] = randint(1, 1_000_000)
    my_posts.append(post)
    return {"Post": post}


@app.get("/posts")
def show_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"Posts": posts}


@app.get("/posts/latest")
def show_last_post():
    post = my_posts[len(my_posts) - 1]
    return {"Post": post}


@app.get("/posts/{post_id}")
def show_post(post_id: int):
    post = find_post(post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Post": f'Post with id: "{post_id}" not found'},
        )
    return {"Post": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    index = find_index_by_id(post_id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}", status_code=status.HTTP_202_ACCEPTED)
def udate_post(post_id: int, user_post: Poster):
    index = find_index_by_id(post_id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    post = user_post.dict()
    my_posts[index]["title"] = post["title"]
    my_posts[index]["content"] = post["content"]
    return {"message": my_posts[index]}
