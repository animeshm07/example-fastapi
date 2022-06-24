from fastapi import Body, FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List

from app import oauth2
from ..database import get_db
from .. import models,schemas, oauth2
#===================Postspath=========================
router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

#This api is returing the data which is genSrated by create_posts api
@router.get("/",response_model=List[schemas.Post]) # these all are the entry points basically
def get_posts(db: Session = Depends(get_db), user_id: int = Depends
(oauth2.get_current_user)):
    posts = db.query(models.Post).all() #This is retriving db data using python code
    return posts

#This api is genrating the data
@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Post) 
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = 
Depends(oauth2.get_current_user)):
    
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
  
    return new_post

#THis api returns the data on the basis of id  
@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int , db: Session = Depends(get_db), current_user: int = Depends
(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id  == id ).first() 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id: {id} was not found")
    return post 


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends
(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id  == id )
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id: {id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail = "Not authrized to perform this action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends
(oauth2.get_current_user)):
    post_qury = db.query(models.Post).filter(models.Post.id  == id )
    post = post_qury.first()
    if post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with the id: {id} was not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail = "Not authrized to perform this action")
    post_qury.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_qury.first()


