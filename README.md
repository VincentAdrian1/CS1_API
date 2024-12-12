# Flask REST API
This project is a Flask Rest Api application 

## Introduction
Rest API is  set of rules and conventions for building and interacting with web services. It uses standard HTTP methods (such as GET, POST, PUT, DELETE) to allow communication between client and server systems, often over the internet.

Key principles of REST APIs:

- Stateless: Each request contains all the information needed, and the server doesn't store session data.
- Client-Server: The client and server are separate, enhancing scalability.
- Uniform Interface: It uses standardized HTTP methods, status codes, and data formats (e.g., JSON, XML).
- Resource-Based: Resources (data or services) are identified by unique URLs.
- Representation: Resources are represented in formats like JSON or XML.
- Cacheable: Responses can be cached to improve performance.

#### Common HTTP Methods in REST

- GET: Retrieve data from the server.
- POST: Send data to the server to create a new resource.
- PUT: Update an existing resource on the server.
- DELETE: Remove a resource from the server.

#### Example use of HTTP Methods in REST

- GET `/users`: Get a list of all users
- GET `/users/1`: Get the details of user with ID 1
- POST `/users`: Create a new user
- PUT `/users/1`: Update the details of user with ID 1
- DELETE `/users/1`: Delete the user with ID 1


## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Installation
  Create a virtual environment in you project folder.
```bash
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```
Activate the virtual environment | To ensure that the correct package/library versions are consistently used every time the software runs.
```bash
.venv/Scripts/Activate
```
Then install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
Import `Flask` and `Flask-MySQLdb` for MySQL integration

The database is provided in the repository
`skill_gap_db.sql`.

## Usage
After the installation of dependencies and the database.

Clone the project into local repository.

The project is capable of CRUD functions, both for employees and skill table.

To run the Flask App, type `python <app_name>.py` in the terminal

### Employees Table Route (Note: the output is in JSON format)

*App route is typed in the url given that is is running in localhost `http://127.0.0.1:5000`*

- `/employees` To view or display the contents of Employee table
- `/employees/1` is for searching, employees can be searched by their ID
- ADD, UPDATE, and DELETE can be used inside the `test.py` and validated in the database or view funtion that the action is executed.
- ADD function is within the `test.py`.
- UPDATE function is within the `test.py`.
- DELETE function is within the `test.py`.


### Skills Table Route (Note: the output is in JSON format)

- `/skills` To view or display the contents of Skills table
- `/skillstbl` To display the number of employees that has a specific skill within the department
- `/skills_dept` To display the specific department details (skills within the department and the number of employees that has it in the department). *To search for the depaartment or use the route, `/skills_dept?department=finance`.* Type "?department=<department name> in the url to search for a specific department.
-  





