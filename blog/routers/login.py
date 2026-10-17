from fastapi import APIRouter,Depends,HTTPException,status
from .. import models,schemas,hashing
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = '/login',
    tags = ['login']

)


@router.post('', status_code = status.HTTP_200_OK )
def login(request : schemas.Login,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"User with username {request.username} not found"

        )
    
    if not hashing.Hash.verify(request.password,user.password):
         raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = f"Invalid password."

        )

    return 'login'
