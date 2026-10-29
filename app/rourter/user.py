from fastapi import Depends, FastAPI, Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session, session
from .. import models,schemas,utils
from ..database import engine,get_db
 
router = APIRouter(
   prefix="/users",
   tags=["users"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.userout)
def creat_user(user: schemas.usercreate, db: Session = Depends(get_db)):
  print(user.password)
  print(len(user.password))
  hash_password= utils.hash(user.password)
  user.password = hash_password
  new_user=models.user(**user.model_dump())
  
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user 

@router.get('/{id}',response_model=schemas.userout)
def get_user(id: int,db: Session = Depends(get_db),):
   user = db.query(models.user).filter(models.user.id == id).first()
   
   if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id:{id} does not exist")
   return user
 
        
 