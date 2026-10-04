from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str 
    published: Optional[bool] 

@app.post('/blog')
def create_blog(blog: Blog):  # or also can write request: Blog  
    
    return {'data' : f'Blog is created with title as {blog.title}'}


@app.get('/blog')
def index(limit = 10, published:bool =True, sort:Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data' : f'{limit} published blog list'}
    else:
        return {'data' : f'{limit} blog list'}
        
 
@app.get('/blog/unpublished')
def show():
    return {'data' : 'list of unpublished blog'} 

@app.get('/blog/{id}')
def show(id : int):
    # fetch blog with id = id
    return{'data' : id}


# Learned about the query parameter in path and the bydefault value in function parameter
# @app.get('/blog')
# def index(limit = 10, published:bool =True, sort:Optional[str] = None):
#     # only get 10 published blogs
#     if published:
#         return {'data' : f'{limit} published blog list'}
#     else:
#         return {'data' : f'{limit} blog list'}

# # so here keep in mind order of path operator decorator as dynamic will come after if previous similar path name. 
# @app.get('/blog/unpublished')
# def show():
#     return {'data' : 'list of unpublished blog'} 

# @app.get('/blog/{id}')
# def show(id : int):
#     # fetch blog with id = id
#     return{'data' : id}






# First learning
# @app.get('/')
# def index():
#     return {'data' : { 'name' : 'Ash' }}


# @app.get('/about')
# def about():
#     return {'data':{'data about '}}