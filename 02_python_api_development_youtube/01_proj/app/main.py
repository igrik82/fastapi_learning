"""First project"""
from fastapi import FastAPI
import models
from database import engine
from routers import posts, users, auth, votes
from config import settings

# Create table
models.Poster.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {"message": "Hello world!"}
