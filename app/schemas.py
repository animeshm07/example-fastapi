from datetime import datetime
import email
from tokenize import String
from typing import Optional
from click import password_option
from pydantic import BaseModel, EmailStr
from sqlalchemy import true


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass 

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode= True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode= True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    # class Config:
    #     orm_mode= True

class Token(BaseModel):
    access_token: str
    token_type: str 

class TokenData(BaseModel):
    id: Optional[str] = None
