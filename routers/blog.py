from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import Optional, Annotated
from pydantic import Field, BaseModel
from .auth import get_current_user
from ..database import SessionLocal
from ..models import UserBlog, Users

router = APIRouter(prefix="/blog", tags=["UserBlog"])

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]

class NewBlog(BaseModel):
    blog: str = Field(min_length=3, max_length=200)
    
    class Config:
        json_schema_extra = {
            "example": {
                "blog": "example"
            }
        }


@router.get("/", status_code=status.HTTP_200_OK)
async def get_latest_blog(user: user_dependency, db: db_dependency):
    return db.query(UserBlog).filter(UserBlog.owner_id==user.get("id")).order_by(UserBlog.id.desc()).first()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_blog(user: user_dependency, db: db_dependency, blog: NewBlog):
    new_blog = UserBlog(**blog.model_dump(), owner_id = user.get("id"))
    db.add(new_blog)
    db.commit()

@router.get("/own", status_code=status.HTTP_200_OK)
async def get_all_userblog(user: user_dependency, db: db_dependency):
    return db.query(UserBlog).filter(UserBlog.owner_id==user.get("id")).all()

@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_blog(user: user_dependency, db: db_dependency):
    return db.query(UserBlog).all()


@router.get("/{blogid}", status_code=status.HTTP_200_OK)
async def get_blog_byid(user: user_dependency, db: db_dependency, blogid: int = Path(ge=1)):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")
    
    blogdata =  db.query(UserBlog).filter(UserBlog.owner_id == user.get("id"), UserBlog.id == blogid).first()
    if blogdata:
        return blogdata
    else:
        raise HTTPException(status_code=404, detail="Data not Found")


@router.delete("/delete/{blogid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(user: user_dependency, db: db_dependency, blogid: int = Path(ge=1)):
    blog_data = db.query(UserBlog).filter(UserBlog.owner_id == user.get("id"), UserBlog.id == blogid).first()
    if not blog_data:
        raise HTTPException(status_code=404, detail="Data not Found")
    
    db.query(UserBlog).filter(UserBlog.owner_id == user.get("id"), UserBlog.id == blogid).delete()
    db.commit()
