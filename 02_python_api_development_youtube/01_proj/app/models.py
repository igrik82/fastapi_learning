"""SqlAlchemy models"""
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
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
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )


class User(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
