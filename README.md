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
The database is provided in the repository
`skill_gap_db.sql`.

## Usage
After the installation of dependencies and the database.

Clone the project into local repository.

The project is capable of CRUD functions, both for employees and skill table.

