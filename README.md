# FastAPI Tasks API with JWT Authentication

This is a simple RESTful API built with FastAPI that allows users to manage tasks.  
Authentication is handled using **JWT (JSON Web Tokens)**, so only logged-in users with a valid token can view tasks.

## Features
- User registration and login
- JWT token authentication
- Create, read, update, and delete tasks
- Secure password hashing with bcrypt
- SQLite database with SQLAlchemy

1. **Clone the repository**  
git clone <your-repo-url>
cd <your-project-folder>

## installation 
pip install -r requirements.txt

## run the application
uvicorn main:app --reload
