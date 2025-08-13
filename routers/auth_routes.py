from fastapi import APIRouter, Depends, HTTPException, dependencies,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from models import *
from jose import JWTError,jwt
from auth import ALGORITHM,SECRET_KEY
# from database import get_db
import models

import models as models, schemas as schemas
from database import SessionLocal
from auth import verify_password, get_password_hash, create_access_token, decode_access_token, blacklist

router = APIRouter(tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/logout")
def logout(token: str = Depends(oauth2_scheme)):
    blacklist.add(token)
    return {"message": "Logged out successfully"}

def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # This will be a dict with "sub"
    except JWTError:
        return None

# def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

@router.get("/auth/profile", response_model=schemas.UserResponse)
def read_current_user(current_user: dict = Depends(get_current_user),db:Session=Depends(get_db)):
    user_name=current_user.get("sub")
    user=db.query(models.User).filter(models.User.username==user_name).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user


@router.delete("/auth/delete-account")
def delete_own_account(db: Session = Depends(get_db),current_user: dict = Depends(get_current_user)):
    # Delete current authenticated user
    username = current_user.get("sub")
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "Account deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")