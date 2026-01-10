Flask REST Users API

A simple REST API built with Flask demonstrating full CRUD operations on a User resource.

Tech Stack

Python

Flask

API Endpoints

POST /users → Create user

GET /users → Get all users

GET /users/<id> → Get user by ID

PUT /users/<id> → Update user

DELETE /users/<id> → Delete user

All requests and responses use JSON.

Run Locally
pip install flask
python app.py


Server runs at:

http://127.0.0.1:5000

Notes

Uses in-memory storage

Data resets on server restart

Tested using Postman

Author

Dhanush
