# Book-Store-API
A simple Book Store API built with Django REST Framework, featuring basic CRUD operations.

Table of Contents

Overview

Features

Installation

Usage

API Endpoints

Contributing

License

Overview

Book-Store-API is a RESTful API for managing a book store. Users can create, read, update, and delete books. The API is built with Django and Django REST Framework, demonstrating basic backend practices including viewsets, pagination, and SQLite database integration.

Features

CRUD operations for books

SQLite database integration

Pagination for book lists

Viewsets for clean API structure

Usage

Use an API client (like Postman) to interact with the endpoints. Example endpoints:

GET /books/router/ — list all books

POST /books/router/ — add a new book

GET /books/router/<id>/ — retrieve a book by ID

PUT /books/router/<id>/ — update a book by ID

DELETE /books/router/<id>/ — delete a book by ID

API Endpoints
Method	  Endpoint	            Description
GET	    /books/router/	      List all books #implemented cursor pagination for the GET request
POST	  /books/router/	      Add a new book
GET	    /books/router/<id>/	  Retrieve book by ID
PUT	    /books/router/<id>/	  Update book by ID
DELETE	/books/router/<id>/	  Delete book by ID
