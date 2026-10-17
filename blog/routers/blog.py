from fastapi import APIRouter,HTTPException,status,Depends
from .. import models,schemas
from .. database import get_db
from sqlalchemy.orm import Session
from typing import List
from .. repository import blog


router = APIRouter(
    prefix = '/blog',
    tags = ['BLOGS']

)



@router.get('' , response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
   return blog.show_all(db)

@router.get('/{id}',status_code=200 , response_model=schemas.ShowBlog)#default status code would not be executed if there is custom status code.
def show (id : int,  db : Session = Depends(get_db) ):
    return blog.show_byid(id, db)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id:int, request : schemas.Blog, db : Session = Depends(get_db)):
     return blog.update(id,request, db )


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db) 

@router.delete('/{id}',status_code=204)
def destroy(id, db : Session = Depends(get_db)):
   return blog.destroy(id, db)
