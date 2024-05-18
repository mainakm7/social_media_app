from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from typing import Optional, Annotated
from pydantic import Field, BaseModel

from ..database import SessionLocal
from ..models import UserBlog

router = APIRouter(prefix="/blog", tags=["UserBlog"])

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class NewBlog(BaseModel):
    blog: str = Field(min_length=3, max_length=200)
    
    class Config:
        schema_extra = {
            "example": {
                "blog": "example"
            }
        }


@router.get("/latest", status_code=status.HTTP_200_OK)
async def get_latest_blog(db: db_dependency):
    return db.query(UserBlog).order_by(UserBlog.id.desc()).first()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_blog(blog: NewBlog, db: db_dependency):
    new_blog = UserBlog(**blog.model_dump())
    db.add(new_blog)
    db.commit()
