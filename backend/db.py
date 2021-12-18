import os
from dotenv import load_dotenv
from os.path import join, dirname
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
print('PATH ', dotenv_path)
load_dotenv(dotenv_path)
USER_NAME = os.environ.get("MYSQL_USER", 'user')
PASSWORD = os.environ.get("MYSQL_PASSWORD", 'password')
HOST = os.environ.get("MYSQL_HOST_NAME", 'db')
DATABASE_NAME = os.environ.get("MYSQL_DATABASE", 'sample_db')

H = os.environ.get("MYSQL_HOST_NAME")
print('H ', H) 

user_name = USER_NAME
password = PASSWORD
host = HOST
database_name = DATABASE_NAME

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()