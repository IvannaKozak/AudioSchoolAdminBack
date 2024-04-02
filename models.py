from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=True)
    email = Column(String(200), nullable=True)
    hashed_password = Column(String(200), nullable=True)
    role = Column(String(45), nullable=True)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(200), nullable=True)


class Audiobook(Base):
    __tablename__ = 'audiobook'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=True)
    description = Column(String(2000), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)

