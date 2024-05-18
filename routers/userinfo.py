from fastapi import APIRouter, Depends
from ..database import SessionLocal
from sqlalchemy import select
from sqlalchemy.orm import Session 
from starlette import status
from typing import Annotated, Optional
from pydantic import Field, BaseModel



router = APIRouter(prefix="/user", tags=["UserInfo"])

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class newdata(BaseModel):
    name: Optional[str] = Field(None, min_length=3)
    about: Optional[str] = Field(None, min_length=3, max_length=100)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Job",
                "about": "I am a test user"
            }
        }

@router.get("/user", status_code=status.HTTP_200_OK)
def get_user():
    return

@router.post("/user", status_code=status.HTTP_201_CREATED)
def welcome_msg():
    return {"Greet": "Welcome! This is your Social Media app."}