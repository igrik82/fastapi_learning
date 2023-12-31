"""Connection to Database"""

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DATABASE = "blog_posts"
engine = create_engine(
    f"postgresql+psycopg://fastapi:123456@192.168.88.226/{DATABASE}", echo=True
)

if not database_exists(engine.url):
    create_database(engine.url)
