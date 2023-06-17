'''First project'''
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello world!'}


if __name__ == "__main__":
    uvicorn.run(app='main:app', host='0.0.0.0', port=8888, reload=True)
