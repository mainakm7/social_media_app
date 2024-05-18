from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class UserInfo(Base):
    __tablename__ = "userinfo"
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(200))
    about = Column(String(200))
    

class UserBlog(Base):
    __tablename__ = "userblog"
    
    id = Column(Integer, primary_key = True, index = True)
    blog = Column(String(200))
    # owner_id = Column(Integer, ForeignKey("userinfo.id"))