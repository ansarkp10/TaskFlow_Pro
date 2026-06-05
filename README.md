# TaskFlow Pro

## Login Page

![Login](./screenshots/login.png)

---

## Dashboard Page

![Dashboard](./screenshots/dashboard.png)

---

## Projects Page

![Projects](./screenshots/projects.png)

---

## Tasks Page

![Tasks](./screenshots/tasks.png)


TaskFlow Pro is a full-stack task management application built using:

- FastAPI (Backend)
- Next.js (Frontend)
- PostgreSQL (Database)
- JWT Authentication

The system supports multi-user project and task management where each user can only access their own data.

---

# Features

## Authentication
- User Registration
- User Login
- JWT Token Authentication

## Users
- Create User
- List Users

## Projects
- Create Project
- List Projects
- Update Project
- Delete Project

## Tasks
- Create Task
- Assign Task
- Update Task Status
- List Tasks
- Filter Tasks
  - By Project
  - By Status
  - By Assigned User

---

# Architecture

Frontend:
- Next.js
- Axios
- Tailwind CSS

Backend:
- FastAPI
- SQLAlchemy
- JWT Authentication
- PostgreSQL

Database:
- PostgreSQL relational database

---

# ER Diagram

Users
│
├── Projects
│     └── created_by → users.id
│
└── Tasks
      └── assigned_to → users.id

Projects
│
└── Tasks
      └── project_id → projects.id

---

# Database Design

## Users

| Column | Type |
|--------|------|
| id | Integer |
| name | String |
| email | String |
| password | String |
| role | String |

---

## Projects

| Column | Type |
|--------|------|
| id | Integer |
| name | String |
| description | String |
| created_by | Integer |

---

## Tasks

| Column | Type |
|--------|------|
| id | Integer |
| title | String |
| description | String |
| status | String |
| project_id | Integer |
| assigned_to | Integer |
| due_date | Date |

---

# Setup Instructions

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
````

Backend runs on:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```bash
http://127.0.0.1:3000
```

---

# Environment Variables

## Backend `.env`

```env
DATABASE_URL=postgresql://postgres:password@localhost/taskflow_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

## Frontend `.env.local`

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

# API Documentation

# Authentication APIs

## Register User

POST `/auth/register`

```json
{
  "name": "Ansar",
  "email": "ansar@gmail.com",
  "password": "123456",
  "role": "developer"
}
```

---

## Login

POST `/auth/login`

```json
{
  "email": "ansar@gmail.com",
  "password": "123456"
}
```

---

# User APIs

## Create User

POST `/users/`

---

## List Users

GET `/users/`

---

# Project APIs

## Create Project

POST `/projects/`

```json
{
  "name": "Ecommerce App",
  "description": "Online shopping platform"
}
```

---

## List Projects

GET `/projects/`

---

## Update Project

PUT `/projects/{project_id}`

---

## Delete Project

DELETE `/projects/{project_id}`

---

# Task APIs

## Create Task

POST `/tasks/`

```json
{
  "title": "Build Login API",
  "description": "Implement JWT auth",
  "status": "pending",
  "project_id": 1,
  "assigned_to": 1,
  "due_date": "2026-06-10"
}
```

---

## Assign Task

PUT `/tasks/{task_id}/assign/{user_id}`

---

## Update Task Status

PUT `/tasks/{task_id}/status?status=completed`

---

## List Tasks

GET `/tasks/`

---

## Filter Tasks By Project

GET `/tasks/?project_id=1`

---

## Filter Tasks By Status

GET `/tasks/?status=pending`

---

## Filter Tasks By Assigned User

GET `/tasks/?assigned_to=1`

---

# Security

* JWT Authentication
* Protected APIs
* User-specific data isolation
* Password hashing using bcrypt

---

# Tech Stack

Frontend:

* Next.js
* Axios
* Tailwind CSS

Backend:

* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT

---

# Author

K ANSAR


