"""SqlAlchemy models"""
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.schema import Sequence, UniqueConstraint
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    type_annotation_map = {datetime: TIMESTAMP(timezone=True)}
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))


class Poster(Base):
    __tablename__ = "posts"

    # For default colomn is not null
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    published: Mapped[bool] = mapped_column(
        server_default="True", nullable=True
    )
    rating: Mapped[int] = mapped_column(nullable=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    owner = relationship("User")
    # votes_rating: Mapped[int] = mapped_column(ForeignKey("votes.id"))
    # make_vote = relationship("Vote")


class User(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)


class Vote(Base):
    __tablename__ = "votes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    vote: Mapped[int] = mapped_column(nullable=True)
    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id", ondelete="CASCADE"),  # primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),  # primary_key=True
    )

    __table_args__ = (UniqueConstraint("post_id", "user_id"),)
