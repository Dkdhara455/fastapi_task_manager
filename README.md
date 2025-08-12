# FastAPI Tasks API with JWT Authentication

This is a simple RESTful API built with FastAPI that allows users to manage tasks.  
Authentication is handled using **JWT (JSON Web Tokens)**, so only logged-in users with a valid token can view tasks.

## Features
->User Registration with:

    ->Password hashing (using passlib)

    ->Password validation (must have at least one number, one special symbol, and be ≥ 5 characters)

->JWT Authentication for login-protected endpoints

->Create, Read, Update, Delete Tasks

->Delete Own Account (removes user from DB andinvalidates token)

->Automatic Logout on account deletion

->Swagger UI for API exploration

**Clone the repository**  
git clone <your-repo-url>
cd <your-project-folder>

## installation 
pip install -r requirements.txt
## in requirements.txt file available all dependencies

## run the application
uvicorn main:app --reload

| Method | Endpoint          | Description                    | Auth Required  |
| ------ | ----------------- | ------------------------------ | -------------  |
| POST   | `/register`       | Register a new user            | ❌            |
| POST   | `/login`          | Login and get JWT token        | ❌            |
| GET    | `/tasks`          | Get all tasks                  | ✅            |
| POST   | `/tasks`          | Create new task                | ✅            |
| PUT    | `/tasks/{id}`     | Update task                    | ✅            |
| DELETE | `/tasks/{id}`     | Delete task                    | ✅            |
| DELETE | `/delete_account` | Delete your account and logout | ✅            |
