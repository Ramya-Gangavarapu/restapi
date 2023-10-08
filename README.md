# Assignment Title: Advanced Django REST API Development

## Introduction

In this assignment, we have developed a Django REST API project following advanced practices and standards. The project aims to demonstrate our proficiency in Django, RESTful API design, code quality, testing, and documentation.

## Project Structure

project-root/
│
├── restapi/                 # Django project folder

│   ├── restapi/             # Main Django app

│   ├── restapiapp/          # Additional app within the project

│   ├── manage.py            # Django management script

│   └── ...                  # Other Django project files

│

├── requirements.txt         # Python package dependencies

│

├── README.md                # Comprehensive project documentation

│

└── ...                      # Other project files


Please check out in the files section

## API Documentation

API provides the following endpoints:

/api/resource/ (GET, POST, PUT, DELETE): Endpoint for managing resources.

/api/auth/ (POST): Authentication endpoint for obtaining a JWT token.

## Resource Endpoints

GET /api/resource/: Retrieve a list of resources.
POST /api/resource/: Create a new resource.
GET /api/resource/{id}/: Retrieve a specific resource by ID.
PUT /api/resource/{id}/: Update a specific resource by ID.
DELETE /api/resource/{id}/: Delete a specific resource by ID.


## Authentication Endpoint

POST /api/auth/: Obtain a JWT token for authentication.


## Testing Approach

We have implemented a comprehensive testing approach to ensure the reliability and correctness of our API. The testing stack includes:

Django's built-in unittest framework

pytest for more advanced testing scenarios

Test cases covering each API endpoint, authentication, and error handling

Mocking for external dependencies

Continuous integration testing with GitHub Actions


## Testing Results

Our testing approach has resulted in the following outcomes:

Test coverage of over 70%

Successful validation of API endpoints and authentication

Proper error handling and validation checks

No security vulnerabilities detected


