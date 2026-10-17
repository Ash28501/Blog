from fastapi import APIRouter,status,HTTPException,Depends
from .. import schemas,models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix = '/users',
    tags = ['USERS'] 
)

@router.post('',response_model= schemas.ShowUser, status_code = status.HTTP_201_CREATED)
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show(id:int, db : Session = Depends(get_db)):
    return user.get_alluser(id, db)