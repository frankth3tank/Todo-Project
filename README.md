# Todos Project with FastAPI
Todos-Project is a simple web application that allows users to manage their todo lists. It's built using FastAPI, SQLite3, and SQLAlchemy.

## Prerequisites
Before you can use this application, you will need to have the following installed on your machine:

- Python 3.7 or higher
- pip

## Installation
1. Clone this repository to your local machine.
```
git clone https://github.com/frankth3tank/Todos-Project.git
```
2. Change into the project directory.
```
cd Todos-Project
```
3. Create a virtual environment and activate it.
```
python -m venv env
source env/bin/activate
```
4. Install the dependencies.
```
pip install -r requirements.txt
```

## Usage
1. Start the API server.
```
uvicorn main:app --reload
```
2. Navigate to http://localhost:8000/docs in your web browser to access the Swagger UI. Here, you can test the different endpoints available in the API.

## Endpoints
### Todos Endpoints
- `GET /` Returns a list of all the todos.
- `GET /todos/{id}` Returns a single todo by its ID.
- `POST /todo` Creates a new todo.
- `PUT /{todo_id}` Updates an existing todo.
- `DELETE /{todo_id}` Deletes a todo by its ID.
### User Endpoints
- `GET /` Returns a list of all the users.
- `PUT /password` Update password of the user.
### Auth Endpoints
- `POST /` Creates a new user.
- `POST /token` Creates a JWT Token.
### Admin Endpoints
- `GET /todos` Returns all todos from every user.
- `DELETE /todo/{todo_id}` Delete a todo from todo id of any user.

## Database
Todos-Project uses a SQLite3 database to store the todos and users. The database file (todosapp.db) is created automatically when you run the application for the first time.

## Models
Todos-Project defines two models: Todo and User.
### Todo
- id: Integer primary key.
- title: String.
- description: String.
- priority: Integer.
- completed: Boolean, default False.
- owner_id: Integer foreign key user id
### User
- id: Integer primary key.
- email: String.
- username: String.
- first_name: String.
- last_name: String.
- hashed_password: String.
- is_active: Boolean, default True.
- role: String.


## Contributing
If you would like to contribute to this project, please open a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License
This project is licensed under the MIT License.