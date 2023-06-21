'''Connection to Database'''
from sqlalchemy import create_engine
# from sqlalchemy import create_engine, text


engine = create_engine(
    'postgresql+psycopg://fastapi:123456@192.168.88.226/posts')

# with engine.connect() as conn:
#     result = conn.execute(text('select * from posts'))
#     print(result.all())
