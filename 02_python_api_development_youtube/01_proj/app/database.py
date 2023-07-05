from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from config import settings


engine = create_engine(
    f"postgresql+psycopg://{settings.database_username}:\
{settings.database_password}@{settings.database_host}:\
{settings.database_port}/{settings.database_name}",
    echo=False,
)

if not database_exists(engine.url):
    create_database(engine.url)


SessionLocal = sessionmaker(autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
