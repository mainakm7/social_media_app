from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String(200), unique=True)
    username = Column(String(45), unique=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    hashed_password = Column(String(200))
    role = Column(String(45))
    phone_number = Column(String(20), unique=True)
    

class UserBlog(Base):
    __tablename__ = "userblog"
    
    id = Column(Integer, primary_key = True, index = True)
    blog = Column(String(200))
    owner_id = Column(Integer, ForeignKey("users.id"))
    
class UserPhotos(Base):
    __tablename__ = "userphotos"
    
    id = Column(Integer, primary_key = True, index = True)
    picurl = Column(String(200))
    owner_id = Column(Integer, ForeignKey("users.id"))