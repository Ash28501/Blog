from fastapi import FastAPI,Depends,status,Response
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(engine)  #main line for connecting to the db 

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db : Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

@app.get('/blog/{id}',status_code=200)#default status code would not be executed if there is custom status code.
def show (id, response : Response, db : Session = Depends(get_db) ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details':f'blog with id {id} not available.'}
    return blog