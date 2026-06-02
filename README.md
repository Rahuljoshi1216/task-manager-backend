# 🚀 Team Task Manager

A full-stack Team Task Manager application built with **FastAPI**, **React**, **PostgreSQL/SQLite**, and **JWT Authentication**. The application enables teams to create projects, manage members, assign tasks, track progress, and monitor project activity through a dashboard.

## 🌟 Features

### 🔐 Authentication & Authorization

* User Signup & Login
* JWT-based Authentication
* Protected Routes
* Role-Based Access Control (Admin / Member)

### 📁 Project Management

* Create Projects
* View User Projects
* Add Team Members to Projects
* Project Membership Validation

### ✅ Task Management

* Create Tasks
* Assign Tasks to Team Members
* Update Task Status
* Track Task Progress
* Project-specific Task Views

### 📊 Dashboard

* Total Tasks Overview
* Pending Tasks Count
* Completed Tasks Count
* Overdue Tasks Tracking
* Priority-Based Statistics

### 🔒 Security

* JWT Token Authentication
* Project-Level Authorization
* Member Access Validation
* Admin-Only Operations

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication

### Database

* SQLite (Development)
* PostgreSQL (Production Ready)


---

## 📂 Project Structure

```text
Task-Manager
│
├── python-backend
│   ├── app
│   │   ├── routes
│   │   ├── services
│   │   ├── models
│   │   ├── schemas
│   │   ├── core
│   │   └── db
│   │
│   ├── requirements.txt
│   └── Procfile
│
└── README.md
```

---

## ⚙️ Installation

### Backend Setup

```bash
cd python-backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

## 🔑 Environment Variables

Create a `.env` file in the backend root directory:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint     | Description   |
| ------ | ------------ | ------------- |
| POST   | /auth/signup | Register User |
| POST   | /auth/login  | Login User    |

### Projects

| Method | Endpoint                          |
| ------ | --------------------------------- |
| GET    | /projects/                        |
| POST   | /projects/                        |
| GET    | /projects/{project_id}            |
| GET    | /projects/{project_id}/members    |
| POST   | /projects/{project_id}/add-member |

### Tasks

| Method | Endpoint            |
| ------ | ------------------- |
| GET    | /tasks/             |
| GET    | /tasks/{project_id} |
| POST   | /tasks/             |
| PUT    | /tasks/{task_id}    |

### Dashboard

| Method | Endpoint    |
| ------ | ----------- |
| GET    | /dashboard/ |

---

## 🎯 Future Improvements

* Email Notifications
* File Attachments
* Comments on Tasks
* Activity Logs
* Real-Time Updates using WebSockets
* Advanced Analytics Dashboard
* Kanban Board View

---

## 👨‍💻 Author

**Rahul Joshi**

AI/ML • GenAI • Deep Learning Enthusiast

GitHub: https://github.com/Rahuljoshi1216

LinkedIn: https://linkedin.com/in/rahullJoshi
