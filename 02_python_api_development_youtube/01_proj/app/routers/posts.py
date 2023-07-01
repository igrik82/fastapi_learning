import sys
import os
from database import get_db
from schema import CreateUpdatePostPydan, ResponsePydan
import models
from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from oauth2 import get_current_user

# importing from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=ResponsePydan
)
def create_post(
    user_post: CreateUpdatePostPydan,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    print(current_user.id)
    new_post = models.Poster(user_id=current_user.id, **user_post.dict())

    db.add(new_post)
    db.commit()
    # return back post
    db.refresh(new_post)

    return new_post


@router.get("/", response_model=list[ResponsePydan])
def show_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Poster).all()
    return posts


@router.get("/latest")
def show_last_post(db: Session = Depends(get_db)):
    post_query = db.query(models.Poster)
    index: int = post_query.count()
    post = post_query.where(models.Poster.id == index).first()
    return post


@router.get("/{post_id}")
def show_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Poster).filter(models.Poster.id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Post": f"Post with id: {post_id} not found"},
        )
    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Poster).filter(models.Poster.id == post_id)
    if post_query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put(
    "/{post_id}",
    response_model=ResponsePydan,
    status_code=status.HTTP_202_ACCEPTED,
)
def udate_post(
    post_id: int,
    user_post: CreateUpdatePostPydan,
    db: Session = Depends(get_db),
):
    post_query = db.query(models.Poster).filter(models.Poster.id == post_id)
    old_post = post_query.first()

    if old_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    post_query.update(user_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
