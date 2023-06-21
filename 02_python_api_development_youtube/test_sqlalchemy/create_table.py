'''Create table'''

from models import Base, Post, User
from connection import engine

print('Creating table...')
Base.metadata.create_all(bind=engine)
print('Done!')
