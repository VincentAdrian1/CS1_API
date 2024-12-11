# Flask REST API
This project is a Flask Rest Api application 

## Introduction
Rest API is  set of rules and conventions for building and interacting with web services. It uses standard HTTP methods (such as GET, POST, PUT, DELETE) to allow communication between client and server systems, often over the internet.

Key principles of REST APIs:

Stateless: Each request contains all the information needed, and the server doesn't store session data.
Client-Server: The client and server are separate, enhancing scalability.
Uniform Interface: It uses standardized HTTP methods, status codes, and data formats (e.g., JSON, XML).
Resource-Based: Resources (data or services) are identified by unique URLs.
Representation: Resources are represented in formats like JSON or XML.
Cacheable: Responses can be cached to improve performance.



## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Installation
  Create a virtual environment in you project folder
```bash
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```
Activate the virtual environment | To ensure that the correct package/library versions are consistently used every time the software runs
```bash
.venv/Scripts/Activate
```
Then install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
  
