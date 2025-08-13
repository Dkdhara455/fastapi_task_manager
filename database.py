from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from fastapi_task_manager.database import Base

DATABASE_URL = "sqlite:///./tasks.db"
#SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://<user-name>:<password@loclhost>:port number/<database-name"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
