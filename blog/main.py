from fastapi import FastAPI,Depends,status,HTTPException
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
from .routers import blog,user

app = FastAPI()
models.Base.metadata.create_all(engine)  #main line for connecting to the db 

app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try :
#         yield db
#     finally:
#         db.close()


# @app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update(id, request : schemas.Blog, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND,
#             detail=f'Blog with id{id} not found.'
#         )
#     blog.update(request.model_dump())
#     db.commit()
#     return 'update'

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request : schemas.Blog, db : Session = Depends(get_db)):
#     new_blog = models.Blog(title = request.title, body = request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog' , response_model=List[schemas.ShowBlog],tags=['blogs'])
# def all(db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).all()
#     return blog





# @app.get('/blog/{id}',status_code=200 , response_model=schemas.ShowBlog, tags=['blogs'])#default status code would not be executed if there is custom status code.
# def show (id, response : Response, db : Session = Depends(get_db) ):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'details':f'blog with id {id} not available.'}

#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND , 
#             detail= f'blog with id {id} not available.'
#             )
#     return blog


# @app.delete('/blog/{id}',status_code=204, tags=['blogs'])
# def destroy(id, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:

#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f'Blog with id{id} not found.'
#         )
    
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.post('/user',response_model= schemas.ShowUser, status_code = status.HTTP_201_CREATED,tags=['Users'])
# def create_user(request : schemas.User, db : Session = Depends(get_db)):
   
#     new_user = models.User(name = request.name, email = request.email, password =Hash.bcrypt(request.password) )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/users/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK, tags=['Users'])
# def show(id:int, db : Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND,
#             detail= f'User with id {id} not found.'
#         )
#     return user

    
