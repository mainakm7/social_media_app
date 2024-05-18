from fastapi import FastAPI
from .models import Base
from .database import engine
from starlette import status
from .routers import userinfo,blog,auth, admin

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(userinfo.router)
app.include_router(blog.router)
app.include_router(auth.router)
app.include_router(admin.router)




@app.get("/healthy")
def health_check():
    return {"status":"healthy"}


@app.get("/", status_code=status.HTTP_200_OK)
def welcome_msg():
    return {"Greet": "Welcome! This is your Social Media app."}

