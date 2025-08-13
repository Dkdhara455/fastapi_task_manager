import uvicorn
import fastapi_task_manager.models as models


if __name__ == "__main__":
    uvicorn.run("fastapi_task_manager.main:app", host="127.0.0.1", port=8000, reload=True)
