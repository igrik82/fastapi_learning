'''First project'''
# import uvicorn
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Poster(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get('/')
def root():
    return {'message': 'Hello world!'}


@app.post('/createpost')
def create_post(user_post: Poster):
    print(user_post.published)
    return {'Post': user_post}


# if __name__ == "__main__":
# uvicorn.run(app='main:app', host='0.0.0.0', port=8888, reload=True)
