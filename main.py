from fastapi import FastAPI
import models
from database import engine
from routers import auth_routes, task_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Task Manager API")

# Include routers
app.include_router(auth_routes.router)
app.include_router(task_routes.router)
