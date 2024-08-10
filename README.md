You can now test the APIs using tools like Postman.

Summary of Available Endpoints
POST /api/register/: Register a new user.
POST /api/login/: Login a user and return a token.
GET /api/tasks/: List all tasks.
POST /api/tasks/: Create a new task.
GET /api/tasks/{id}/: Retrieve a specific task.
PUT/PATCH /api/tasks/{id}/: Update a task.
DELETE /api/tasks/{id}/: Delete a task.
POST /api/tasks/{id}/add_member/: Add a member to a task.
POST /api/tasks/{id}/remove_member/: Remove a member from a task.
GET /api/tasks/{id}/members/: List all members of a task.
POST /api/tasks/{id}/add_comment/: Add a comment to a task.
GET /api/tasks/{id}/comments/: List all comments of a task.
PATCH /api/tasks/{id}/update_status/: Update the status of a task.
