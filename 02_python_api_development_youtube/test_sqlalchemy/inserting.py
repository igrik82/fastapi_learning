'''Inserting into table'''
from models import User, Post
from sqlalchemy.orm import Session
from connection import engine

session = Session(bind=engine)


derek = User(
    username='Derek',
    email_addr='derek@gmail.com',
    post=[
        Post(
            title='Learning python',
            content='About python learning'
        )
    ]

)

igor = User(
    username='Igor',
    email_addr='igrik@gmail.com',
    post=[
        Post(
            title='Live in ocean',
            content='About ocean'
        )
    ]

)

alena = User(
    username='Alena',
    email_addr='alena@gmail.com',
    post=[
        Post(
            title='Fairy tale',
            content='About fairy'
        )
    ]

)

session.add_all([derek, igor, alena])
session.commit()
