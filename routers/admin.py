from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from pydantic import Field, BaseModel
from ..models import UserBlog, Users
from ..database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated, Optional
from .auth import get_current_user


router = APIRouter(prefix="/admin", tags=["Admin"])


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
        
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/blog", status_code=status.HTTP_200_OK)
async def read_all_blogs(user: user_dependency, db: db_dependency):
    if not user or user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Admin authentication failed")
    return db.query(UserBlog).all()

@router.get("/users", status_code=status.HTTP_200_OK)
async def all_user_data(user: user_dependency, db: db_dependency):
    if not user or user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Admin authentication failed")
    return db.query(Users).all()

@router.delete("/delete/{blogid}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_byid(user: user_dependency, db: db_dependency, blogid: int = Path(gt=0)):
    
    if not user or user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Admin authentication failed")
    
    data_model = db.query(UserBlog).filter(UserBlog.id == blogid).first()
    if not data_model:
        raise HTTPException(status_code=404, detail="Data not Found")
    
    db.query(UserBlog).filter(UserBlog.id == blogid).delete()
    db.commit()
    