from enum import unique
from xmlrpc.client import Boolean
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text
from sqlalchemy.orm import relationship
# Posttables
#Table creation code It created these tables Post, Users
class Post(Base):
    __tablename__= "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default ='TRUE',nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    owner = relationship("User") 

#UsersTable
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String,nullable=False,)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
