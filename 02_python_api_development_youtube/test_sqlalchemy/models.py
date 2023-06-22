"""Base model"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    email_addr: Mapped[str]
    post: Mapped[list["Post"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User username={self.username}"


class Post(Base):
    __tablename__ = "user_post"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    published: Mapped[bool] = mapped_column(default=True, nullable=False)
    user: Mapped["User"] = relationship(back_populates="post")

    def __repr__(self) -> str:
        return f"<Post title={self.title} content={self.content}"
