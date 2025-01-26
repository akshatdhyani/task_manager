# Task Management 

Task management system using "Python" , "Django" and "Django REST FRAMEWORK"
This API let's a user to manage tasks based on Roll Based Access Control. It lets user registration, assign tasks and manage them according to the role.

# Features
• User System : Registration and login functionality with role based access control according to roles(Admin, Manager or Employee)
• Task Management : Can perform CRUD operations for tasks
• Role Based Access Control : *Admins can manage users and tasks.
    * Managers can create, assign, and update tasks.
    * Employees can view and update their own tasks. 
    
# Technical Requirements
1. Backend Framework :-
Use Django, FastAPI or any other framework of Python
** Required API Endpoints:
Authentication & User Management:
● POST /auth/register - Register new user
● POST /auth/login - User login
● GET /users - List all users (Admin only)
● PUT /users/<id>/role - Update user role (Admin only)

** Task Management:
● GET /tasks - List tasks (filtered by role)
● POST /tasks - Create new task (Manager+)
● GET /tasks/<id> - Get single task
● PUT /tasks/<id> - Update task
● DELETE /tasks/<id> - Delete task (Manager+)
● POST /tasks/<id>/assign - Assign task to employee (Manager+)

** Role-Based Access Control
Access rules:
● Admin:
○ Full access to all endpoints
○ Can manage user roles
○ Can view all tasks and users
● Manager:
○ Can create tasks
○ Can assign tasks to employees
○ Can view all tasks
○ Can update task status
● Employee:
○ Can view assigned tasks
○ Can update task status
○ Cannot create or assign tasks

# Set-up instructions
1.Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/akshatdhyani/task_manager.git
cd task_manager
```
2. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

3. Apply Migrations
   ```
   python manage.py migrate
   ```
4. Create Superuser
   ```
   python manage.py createsuperuser
   ```
   You can use by default created superuser with the following credentials:-
   ```
   username: akshat
   password: superuser
   ```
5. Run the development server
   ```
   python manage.py runserver
   ```

### Example API Requests and Response
# 1. User registration
   # Request:
   POST /auth/register/
   {
   "username" : "Robert_Jr",
   "email" : "robert@gmail.com",
   "password" : "ironman3000",
   "role" : "admin"
   }

   # Response:
   {
    "message": "User has been registered. Thank you for registering."
    }
# 2. User Login
   # Request:
   POST /auth/login/
  {
    "username": "Robert_Jr",
    "password": "ironMan3000"

  }
  # Response:
  {
    "access": "acess_token",
    "refresh": "access_token"
  }
# 3. Create a task (done by manager):
  # Request:
  POST /tasks/
  {
      "title": "Next round of the interview",
      "description": "Appear for the next round of the interview",
      "due_date": "2025-01-31",
      "status": "pending",
      "level": "high"
  }

  # Response: 
  {
    "id": 2,
    "title": "CNext round of the interview",
    "description": "Appear for the next round of the interview",
    "due_date": "2025-01-31",
    "status": "pending",
    "level": "high",
    "created_on": "2025-01-24T14:00:00Z",
    "assigned_to": null,
    "assigned_by": null
}

# 4. Delete a task (done by manager)
  # Request:
  DELETE /tasks/<taskID>/

  # Response:
  {
    "message": "Task deleted."
  }
