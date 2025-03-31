from sqlalchemy import Column, Integer, String
from database import Base , engine


def create_table():
    Base.metadata.create_all(engine)
    print("Table created")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)