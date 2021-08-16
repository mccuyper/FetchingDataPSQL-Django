# testing SQLAlchemy connecting to DB

from sqlalchemy import create_engine
from  sqlalchemy import MetaData, Table


DB_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'
ENGINE = create_engine(DB_URL)

conn = ENGINE.connect()
metadata = MetaData()
user = Table('cdr', metadata, Column('id'))
try:
    print('success')
except:
    print('failed')