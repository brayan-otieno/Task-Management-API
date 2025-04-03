# Task Management API

This is a Task Management API built with Django and Django Rest Framework (DRF). It provides a RESTful interface for managing tasks, user authentication, and task assignments.

## Features

- User authentication (with registration and login)
- Task management (CRUD operations)
- Task assignment to users
- Task status management (e.g., pending, in-progress, completed)
- Task filtering and sorting by due date, status, and more.

## Requirements

- Python 3.6+
- Django 3.x or higher
- Django Rest Framework (DRF)
- A virtual environment (recommended)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api

### 2. Register a user

```bash
POST /api/auth/register/

{
  "email": "user@example.com",
  "username": "testuser",
  "password": "testpass123"
}

### 3. Login to Get Tokens

```bash
POST /api/auth/login/
{
  "email": "user@example.com",
  "username": "testuser",
  "password": "testpass123"
}

Response will include:
```bash
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}

Use the access token in the Authorization header for subsequent requests:
```bash
Authorization: Bearer your-access-token

### Projects Endpoints

### 1. Create Project
```bash
POST /api/projects/

{
  "name": "New Project",
  "description": "Project description"
  "members": [id]
}

###  Get Project Details
```bash
GET /api/projects/{id}/

### Update Project
```bash
PUT /api/projects/{id}/

{
  "name": "Updated Project Name",
  "description": "Updated description"
  "memebers": [id]
}

### Delete Project
```bash
DELETE /api/projects/{id}/

### Tasks Endpoints

### 1. List All Tasks (with filters)
```bash
GET /api/tasks/
GET /api/tasks/?status=completed
GET /api/tasks/?priority=high
GET /api/tasks/?project={project_id}

### 2. Create Task
```bash
POST /api/tasks/

{
  "title": "New Task",
  "description": "Task description",
  "priority": "high",
  "status": "todo",
  "due_date": "2023-12-31T23:59:59Z",
  "project": 1,
  "assigned_to": [1, 2]
}

### Get Task Details
```bash
GET /api/tasks/{id}/

### Update Task
```bash
PUT /api/tasks/{id}/

{
  "title": "Updated Task Title",
  "status": "in_progress"
}

### Delete Task
```bash
DELETE /api/tasks/{id}/


### Comments Endpoints

### 1. List Comments for Task
```bash
GET /api/comments/?task_id={task_id}

### 2. Create Comment
```bash
POST /api/comments/
Content-Type: application/json

{
  "task": 1,
  "content": "This is a comment",
  "mentions": [2, 3]
}

### 3. Get Comment Details
```bash
GET /api/comments/{id}/

### 4. Update Comment
```bash
PUT /api/comments/{id}/
{
  "content": "Updated comment content"
}

### Task History Endpoints

### 1. View Task History
```bash
GET /api/task-history/?task_id={task_id}