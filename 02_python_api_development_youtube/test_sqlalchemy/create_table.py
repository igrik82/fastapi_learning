"""Create table"""

from models import Base
from connection import engine

print("Creating table...")
Base.metadata.create_all(bind=engine)
print("Done!")
