from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : 'blog list'}

# so here keep in mind order of path operator decorator as dynamic will come after if previous similar path name. 
@app.get('/blog/unpublished')
def show():
    return {'data' : 'list of unpublished blog'} 

@app.get('/blog/{id}')
def show(id : int):
    # fetch blog with id = id
    return{'data' : id}






# First learning
# @app.get('/')
# def index():
#     return {'data' : { 'name' : 'Ash' }}


# @app.get('/about')
# def about():
#     return {'data':{'data about '}}