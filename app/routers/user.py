from .. import models,schemas,utils
from fastapi import Body, FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

#===================Userspaths=========================
router = APIRouter(
    prefix="/users",
    tags=['users']
)

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    #Hashing the password for users table
    hashed_password = utils.hash(user.password)
    #Storing the hashed password into users.password colom
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = f"users with the id: {id} has not found")
    return user