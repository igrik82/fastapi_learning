'''First project'''
from random import randint
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Poster(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# Storing data in lists
my_posts = [{'title': 'title of post1', 'content': 'content post 1', 'id': 1},
            {'title': 'title of post2', 'content': 'content post 2', 'id': 2},
            {'title': 'title of post3', 'content': 'content post 3', 'id': 3}]


def find_post(post_id):
    for post in my_posts:
        print(post['id'])
        if post['id'] == post_id:
            return post
    return None


@app.get('/')
def root():
    return {'message': 'Hello world!'}


@app.post('/posts')
def create_post(user_post: Poster):
    post = user_post.dict()
    if not post['id']:
        post['id'] = randint(1, 1_000_000)
    my_posts.append(post)
    return {'Post': post}


@app.get('/posts')
def show_posts():
    return {'Posts': my_posts}


@app.get('/posts/latest')
def show_lat_post():
    post = my_posts[len(my_posts) - 1]
    return {'Post': post}


@app.get('/posts/{post_id}')
def show_post(post_id: int):
    post = find_post(post_id)
    return {'Post': post}
