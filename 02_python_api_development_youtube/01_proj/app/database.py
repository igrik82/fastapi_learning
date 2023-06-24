from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


DATABASE = "blog"
engine = create_engine(
    f"postgresql+psycopg://fastapi:123456@192.168.88.226/{DATABASE}", echo=True
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
