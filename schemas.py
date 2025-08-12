from pydantic import BaseModel

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

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

#  TOKEN 
class Token(BaseModel):
    access_token: str
    token_type: str
