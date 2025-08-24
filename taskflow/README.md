# TaskFlow API

A Django REST Framework API for a collaborative task management system.

## Features

*   User registration and authentication
*   Project creation and management
*   Task tracking within projects
*   Commenting system on tasks
*   User permissions and project membership

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/taskflow-api.git
    cd taskflow-api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://localhost:8000/`.

## API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/auth/register/` | POST | User registration |
| `/api/auth/login/` | POST | User login |
| `/api/projects/` | GET, POST | List and create projects |
| *(More endpoints to be documented as they are built)* | | |

## Technology Stack

*   Django
*   Django REST Framework
*   SQLite (Development)
