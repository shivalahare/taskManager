
# Task Management Application

A **Task Management** system built using the **Django** web framework. This project allows users to register, log in, and manage their tasks with full CRUD (Create, Read, Update, Delete) functionality. The app is ideal for learning or practicing how to work with Django's authentication system, forms, models, and templates.

## Features

- User authentication (Login/Signup/Logout).
- Task creation, viewing, updating, and deletion.
- Simple and clean Bootstrap-based UI.
- Responsive design (mobile-friendly).
- CSRF protection for secure forms.
- Uses Django class-based views and the built-in authentication system.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Features and Functionality](#features-and-functionality)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

Make sure you have the following installed:

- **Python 3.8+**: [Download here](https://www.python.org/downloads/)
- **Django 4.0+**: The web framework used to develop this application.
- **Git**: For version control and cloning the repository.
- **pip**: To install the required Python dependencies.

### Installation

1. **Clone the repository**:
   
   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/task-manager.git
   ```

2. **Navigate to the project directory**:
   
   ```bash
   cd taskManager
   ```

3. **Create a virtual environment** (recommended):
   
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:

   - For **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - For **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install the project dependencies**:

   Install all the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations**:

   Apply the necessary database migrations to set up the models:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser** (optional):

   You can create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:

   Finally, run the application using:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000`.

### Project Structure

Here's an overview of the project's directory structure:

```
task-manager/
├── tasks/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── task_manager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

- **tasks/**: Contains the app-specific logic like models, views, templates, and static files.
- **taskManager/**: The main Django project directory that holds settings, URLs, and configuration files.
- **db.sqlite3**: The SQLite database file (created after running migrations).
- **manage.py**: Django's command-line utility for administrative tasks.

### Features and Functionality

#### 1. **User Authentication**
   - **Login**: Users can log in using their credentials.
   - **Signup**: New users can create an account.
   - **Logout**: Authenticated users can log out securely.

#### 2. **Task Management**
   - **Create Tasks**: Users can create new tasks using the task form.
   - **View Tasks**: Tasks are listed on the dashboard.
   - **Update Tasks**: Users can update the details of existing tasks.
   - **Delete Tasks**: Tasks can be removed permanently.

#### 3. **Django Admin Panel**
   - Admins can manage tasks and users through the built-in Django admin interface.

### Usage Guide

1. **Homepage (Task List)**:
   - Shows all tasks associated with the logged-in user.
   - Tasks can be created, updated, and deleted from this page.

2. **Task Creation**:
   - Navigate to `/create/` to add new tasks.
   - Requires a title and description.

3. **Task Update/Delete**:
   - Use the edit or delete buttons next to each task on the task list page.

4. **Login/Signup**:
   - Navigate to `/accounts/login/` to log in.
   - Sign up at `/accounts/signup/` if you don’t have an account.

### Screenshots (Optional)
<picture> <img align="right" src="https://github.com/shivalahare/taskManager/blob/main/screenshots/Tm1.png?raw=true"></picture>

### Contributing

If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your branch.
5. Create a new pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
