# Python_Django
#codemonk_project

**Overview**
Codemonk project is a Django-based web application that offers user management, paragraph storage, and search functionality. The backend is built with Django REST Framework, enabling the creation, management, and retrieval of paragraphs and users via RESTful APIs.

**Features**
User Management: Users can register, log in, and manage their accounts.
Paragraph Management: Users can save paragraphs and associate them with individual words.
Search Functionality: Users can search for paragraphs containing specific words.
API Documentation: Automatically generated API documentation using Swagger and ReDoc.
Project Structure

**Installation
Prerequisites**

•	Python 3.x
•	PostgreSQL
•	pip (Python package installer)

Steps

1.Clone the Repository:
git clone <repository_url>
cd codemonk

2.Create and Activate Virtual Environment:
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3.Install Dependencies:
pip install -r requirements.txt

4.Configure Database:
Modify DATABASES settings in codemonk/settings.py to match your PostgreSQL configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5.Apply Migrations:
python manage.py migrate

6.Create a Superuser:
python manage.py createsuperuser

7.Run the Development Server:
python manage.py runserver
The server will be available at http://localhost:8000/.

**Usage**
API Endpoints
User Management
•	Register a User:
POST /api/users/
json
Copy code
{
    "email": "user@example.com",
    "name": "User Name",
    "dob": "1990-01-01",
    "password": "password123"
}
•	Retrieve, Update, or Delete a User:
GET, PUT, DELETE /api/users/{id}/

**Authentication**
•	Login: POST /api/token/
{
    "email": "user@example.com",
    "password": "password123"
}
This returns a JWT token pair (access and refresh tokens).

•	Refresh Token: POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}
Paragraph Management
•	Save a Paragraph:  POST /api/save-paragraph/
{
    "text": "This is a sample paragraph."
}
•	Search Paragraphs: GET /api/search/?word=sample
{
    "search_results": [
        "This is a sample paragraph."
    ]
}
-------------------------------------------------------##---------------------------------------------------------------------------
**Frontend**
The frontend is a simple HTML page with forms for submitting and searching paragraphs. To use the frontend:
1.	Open test.html in your browser:  The page contains forms to submit paragraphs and search for words within paragraphs.

2.	Submit Paragraph: 
•	 Enter a paragraph in the textarea and click "Submit".
•	The paragraph will be saved to the backend.

3.	Search Paragraphs:
•	Enter a word in the search input and click "Search".
•	The results will display paragraphs containing the word.

**API Documentation**
API documentation is available via Swagger and ReDoc.

•	Swagger UI: http://localhost:8000/api/docs/
•	ReDoc: http://localhost:8000/api/redoc/
These endpoints provide detailed information on all available APIs, including request and response formats.

**Conclusion:**
Codemonk is now set up and ready to use. You can interact with the backend APIs via the frontend forms or through API clients like Postman. The provided API documentation will help you understand and use the available endpoints effectively.
