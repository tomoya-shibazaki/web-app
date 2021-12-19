"""db"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
USER_NAME = os.environ.get("MYSQL_USER", "user")
PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
HOST = os.environ.get("MYSQL_HOST_NAME", "db")
DATABASE_NAME = os.environ.get("MYSQL_DATABASE", "sample_db")


user_name = USER_NAME
password = PASSWORD
host = HOST
database_name = DATABASE_NAME

DATABASE = f"mysql://{user_name}:{password}@{host}/{database_name}?charset=utf8"

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()
