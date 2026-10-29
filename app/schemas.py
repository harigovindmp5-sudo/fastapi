from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict,conint
class PostBase(BaseModel):
    title: str
    content: str
    published : bool = True

class Postcreate(PostBase):
    pass
class userout(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)   

class Post(BaseModel):
    id:int
    title:str
    content:str
    published: bool 
    created_at: datetime
    owner_id:int
    owner:userout

    model_config = ConfigDict(from_attributes=True)

class Postout(BaseModel):
    Post: Post
    votes: int
    model_config = ConfigDict(from_attributes=True)
     
class usercreate(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str
class token(BaseModel):
    access_token:str
    token_type:str
class tokendata(BaseModel):
      id: Optional[int] = None
class vote(BaseModel):
    post_id:int
    dir:conint(le=1)
