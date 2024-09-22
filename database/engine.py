from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

from database.config import conf

Base: DeclarativeBase = declarative_base()
engine = create_engine(conf.get_url)
session = sessionmaker(engine, expire_on_commit=False)
