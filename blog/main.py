from fastapi import FastAPI
from . import schemas,models
from .database import engine


app = FastAPI()
models.Base.metadata.create_all(engine)  #main line for connecting to the db 


@app.post('/blog')
def create(request : schemas.Blog):
    return request

