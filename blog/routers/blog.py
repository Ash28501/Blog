from fastapi import APIRouter,HTTPException,status,Depends
from .. import models,schemas
from .. database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()



@router.get('/blog' , response_model=List[schemas.ShowBlog],tags=['blogs'])
def all(db : Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

@router.get('/blog/{id}',status_code=200 , response_model=schemas.ShowBlog, tags=['blogs'])#default status code would not be executed if there is custom status code.
def show (id,  db : Session = Depends(get_db) ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details':f'blog with id {id} not available.'}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , 
            detail= f'blog with id {id} not available.'
            )
    return blog


@router.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id, request : schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id{id} not found.'
        )
    blog.update(request.model_dump())
    db.commit()
    return 'update'


@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}',status_code=204, tags=['blogs'])
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id{id} not found.'
        )
    
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
