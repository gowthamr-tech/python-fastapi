from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)

class Product(Base):
    __tablename__ = "products"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(100), nullable=False, index=True)
    price=Column(Integer, nullable=False)

class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String(100), nullable=False, index=True)
    email=Column(String(100), nullable=False, index=True)