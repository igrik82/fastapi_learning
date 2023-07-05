from enum import Enum
from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schema import Votes
from oauth2 import get_current_user
from models import Vote, Poster

router = APIRouter(prefix="/votes", tags=["Votes"])


def like_or_dislike(user_vote: int, exception: bool = False):
    # Liked or disliked
    class LikeDislike(Enum):
        liked = 1
        disliked = 0

    def choise(vote: int):
        if LikeDislike.liked.value == vote:
            return LikeDislike.liked.name
        return LikeDislike.disliked.name

    if exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"You already {choise(user_vote)} this post.",
        )
    return {"details": f"Yoy successfully {choise(user_vote)} this post."}


@router.post("/", status_code=status.HTTP_201_CREATED)
def make_vote(
    body_data: Votes,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    print(body_data.post_id)
    # if post exist
    post_exist = (
        db.query(Poster).filter(body_data.post_id == Poster.id).first()
    )

    if not post_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found."
        )

    vote_query = db.query(Vote).filter(
        body_data.post_id == Vote.post_id, current_user.id == Vote.user_id
    )
    found_vote = vote_query.first()

    if found_vote:
        if found_vote.vote == body_data.vote:
            like_or_dislike(body_data.vote, True)

        new_vote = Vote(
            # post_id=body_data.post_id,
            # user_id=current_user.id,
            vote=body_data.vote,
        )
        vote_query.update({"vote": new_vote.vote}, synchronize_session=False)
        db.commit()
        return {"details": f"{like_or_dislike(body_data.vote)}"}
    else:
        new_vote = Vote(
            post_id=body_data.post_id,
            user_id=current_user.id,
            vote=body_data.vote,
        )
        db.add(new_vote)
        db.commit()
        return {"details": f"{like_or_dislike(body_data.vote)}"}
