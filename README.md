E-Commerce REST API
A RESTful API built with Django REST Framework for managing products in an e-commerce platform.

Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (Development)
- Postman (API Testing)

Features
- Full CRUD operations for Products
- Field level and Object level validations
- DRF Browsable API
- JWT Authentication ready

API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/products/ | Get all products |
| POST | /api/products/ | Create a product |
| GET | /api/products/{id}/ | Get single product |
| PUT | /api/products/{id}/ | Update a product |
| DELETE | /api/products/{id}/ | Delete a product |

Setup Instructions
1. Clone the repository
2. Create virtual environment:
   python -m venv ecommerce_env
3. Activate virtual environment:
   ecommerce_env\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Run migrations:
   python manage.py migrate
6. Start server:
   python manage.py runserver

