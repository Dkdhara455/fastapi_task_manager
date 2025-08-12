from pydantic import BaseModel,validator
import re
from fastapi import HTTPException

# TASK 
class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class TaskResponse(TaskBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True

#  USER 
class UserCreate(BaseModel):
    username: str
    password: str
    @validator("password")
    def validate_password(cls, v):
        if len(v) < 5:
            raise ValueError("Password must be at least 5 characters long.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character.")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit.")
        return v

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

#  TOKEN 
class Token(BaseModel):
    access_token: str
    token_type: str
