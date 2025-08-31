TaskFlow API
A Django REST Framework API for a collaborative task management system.

Features
User registration and authentication with token-based auth

Project creation and management with team collaboration

Task tracking within projects with status and priority levels

Commenting system on tasks for team discussion

Dashboard with project statistics and analytics

User permissions and project membership management

Installation & Setup
Clone the repository:

bash
git clone https://github.com/benjamin-w-pixel/taskflow-api.git
cd taskflow-api
Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py migrate
Create a superuser (optional for admin access):

bash
python manage.py createsuperuser
Start the development server:

bash
python manage.py runserver
The API will be available at http://localhost:8000/.

API Endpoints
Endpoint	Method	Description	Authentication
/api/auth/register/	POST	User registration	None
/api/auth/login/	POST	User login (returns token)	None
/api/projects/	GET	List user's projects	Token Required
/api/projects/	POST	Create new project	Token Required
/api/tasks/	POST	Create new task	Token Required
/api/comments/	POST	Add comment to task	Token Required
/api/dashboard/overview/	GET	Project statistics	Token Required
Example Usage
User Registration
bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'
User Login
bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
Create Project (with authentication)
bash
curl -X POST http://127.0.0.1:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{"title":"My Project","description":"Project description"}'
Technology Stack
Django 5.2.5

Django REST Framework

SQLite (Development)

Token Authentication

PostgreSQL (Ready for production)

Project Structure
text
taskflow-api/
├── users/          # User authentication app
├── projects/       # Project management app
├── tasks/          # Task management app
├── comments/       # Comment system app
├── dashboard/      # Analytics and reporting
└── taskflow/       # Main project configuration
Complete API Testing Guide
1. User Registration
POST http://127.0.0.1:8000/api/auth/register/

json
{
    "username": "alxstudent",
    "email": "student@alx.com",
    "password": "alxpassword123"
}
2. User Login
POST http://127.0.0.1:8000/api/auth/login/

json
{
    "username": "alxstudent",
    "password": "alxpassword123"
}
Save the token returned in the response

3. Get Projects
GET http://127.0.0.1:8000/api/projects/
Headers:

Authorization: Token YOUR_TOKEN_HERE

4. Create Project
POST http://127.0.0.1:8000/api/projects/
Headers:

Content-Type: application/json

Authorization: Token YOUR_TOKEN_HERE

json
{
    "title": "ALX Capstone Project",
    "description": "Building TaskFlow API for ALX",
    "deadline": "2024-12-31T23:59:59Z"
}
5. Create Task
POST http://127.0.0.1:8000/api/tasks/
Headers:

Content-Type: application/json

Authorization: Token YOUR_TOKEN_HERE

json
{
    "title": "Test API Endpoints",
    "description": "Test all endpoints with Postman",
    "project": 1,
    "status": "IN_PROGRESS",
    "priority": "HIGH"
}
6. Create Comment
POST http://127.0.0.1:8000/api/comments/
Headers:

Content-Type: application/json

Authorization: Token YOUR_TOKEN_HERE

json
{
    "content": "Great progress on the API implementation!",
    "task": 1
}
7. Get Dashboard
GET http://127.0.0.1:8000/api/dashboard/overview/
Headers:

Authorization: Token YOUR_TOKEN_HERE

Expected Responses
Successful Registration (201)
json
{
    "token": "abc123def456ghi789jkl012mno345pqr678",
    "user_id": 1,
    "username": "alxstudent"
}
Successful Login (200)
json
{
    "token": "abc123def456ghi789jkl012mno345pqr678",
    "user_id": 1,
    "username": "alxstudent"
}
Projects List (200)
json
[
    {
        "id": 1,
        "title": "ALX Capstone Project",
        "description": "Building TaskFlow API for ALX",
        "owner": 1,
        "members": [1],
        "deadline": "2024-12-31T23:59:59Z",
        "created_at": "2024-08-31T11:30:00.123456Z"
    }
]
Dashboard Overview (200)
json
{
    "total_projects": 1,
    "total_tasks": 3,
    "completed_tasks": 1,
    "completion_rate": 33.33,
    "user": "alxstudent"
}
Error Handling
401 Unauthorized
json
{
    "detail": "Authentication credentials were not provided."
}
400 Bad Request (Validation Error)
json
{
    "error": "Invalid input data",
    "details": {
        "username": ["This field is required."]
    }
}
