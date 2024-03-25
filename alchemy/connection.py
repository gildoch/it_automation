from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column