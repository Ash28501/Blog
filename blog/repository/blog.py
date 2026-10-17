from fastapi import HTTPException,status
from .. import models






def show_all(db):
     blog = db.query(models.Blog).all()
     return blog

def show_byid(id : int,db ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details':f'blog with id {id} not available.'}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , 
            detail= f'blog with id {id} not available.'
            )
    return blog

def update(id : int, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id{id} not found.'
        )
    blog.update(request.model_dump())
    db.commit()
    return f'update blog with id {id}'



def create(request,db):
    new_blog = models.Blog(title = request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id{id} not found.'
        )
    
    blog.delete(synchronize_session=False)
    db.commit()
    return  f'deleted blog with id {id}'