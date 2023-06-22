"""Inserting into table"""
from models import User, Post
from sqlalchemy.orm import Session
from connection import engine

session = Session(bind=engine)

derek = User(
    username="Derek",
    email_addr="derek@gmail.com",
    post=[Post(title="Learning python", content="About python learning")],
)

bimbam = User(
    username="bimbom",
    email_addr="tuktuk@gmail.com",
    post=[Post(title="Learning python", content="About python learning")],
)

vlada = User(
    username="Vlada",
    email_addr="vlada@gmail.com",
    post=[Post(title="All about love", content="About love")],
)

igor = User(
    username="Igor",
    email_addr="igrik@gmail.com",
    post=[Post(title="Live in ocean", content="About ocean")],
)

alena = User(
    username="Alena",
    email_addr="alena@gmail.com",
    post=[Post(title="Fairy tale", content="About fairy")],
)

boom = User(
    username="boom",
    email_addr="boom@gmail.com",
    post=[
        Post(
            title="About boom",
            content="fdsfaklj jkldsfg kjdfsklajsd kljasdflkj kljasdf",
        ),
        Post(
            title="Secont About boom",
            content="Second fdsfaklj jkldsfg kjdfsklajsd kljasdflkj kljasdf",
        ),
    ],
)

bam = User(
    username="Bam",
    email_addr="asdfasdf@gmail.com",
    post=[Post(title="fasdfas", content="dsfasa")],
)

tram = User(
    username="Tram",
    email_addr="tram@gmail.com",
    post=[Post(title="tram pam pam", content="boomm tram bam bam")],
)

session.add_all([derek, igor, alena, vlada, boom, bam, tram])
session.commit()
