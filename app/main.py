from fastapi import FastAPI, Depends
from requests import post
from . import models
from . database import engine, get_db
from sqlalchemy.orm import Session
from .routers import auth, post,user


app = FastAPI() # Creating an instance of fast API

#title str , content str restricting the api data
#FastApI db connection string copied from fastapi documents
models.Base.metadata.create_all(bind=engine) #this create the table

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

#POC methods
@app.get("/") # Path operation copied from FASTAPI also its for getting the request from api
def root():
    return{"message": "Welcome to my api"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return {"data":post}

    