Django Machine Test.

Creating users, managing clients and projects

#Django REST API for Client and Project Management

#Overview

This project provides a RESTful API built with Django to manage clients, users, and projects efficiently. It allows for the registration of clients,projects, along with retrieval,updation and deletion of clients and projects.

#Features

Client Management: Register, update, and delete clients. Project Management: Create projects for clients and assign users. User-Specific Projects: Retrieve projects assigned to the logged-in user.

#Endpoints

GET /clients/: List all clients. POST /clients/: Create a new client. GET /clients/:id: Retrieve client details with projects. PUT /clients/:id: Update client information. DELETE /clients/:id: Delete a client. POST /clients/:id/projects/: Create a new project for a client. GET /projects/: List projects assigned to the logged-in user.

#Usage

Access the API endpoints via your preferred API client or browser.
