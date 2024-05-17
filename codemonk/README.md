Paragraph Management API
This project implements a REST API using Django and PostgreSQL to manage paragraphs of text. The API allows you to submit multiple paragraphs, stores each paragraph along with word-to-paragraph mappings, and provides an endpoint to search for paragraphs containing a specific word.

Features
Submit multiple paragraphs of text via a POST request.
Store each paragraph in a PostgreSQL database.
Store mappings of each word to its corresponding paragraph.
Retrieve paragraphs that contain a specific word via a GET request.
Prerequisites
Python 3.10 or higher
PostgreSQL 13 or higher
Django 5.0.4
Django REST Framework
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/paragraph-management-api.git
cd paragraph-management-api
Set up a virtual environment:

sh
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
Configure PostgreSQL:

Create a PostgreSQL database and user. Replace your_database_name, your_database_user, and your_database_password with your actual database credentials.

sh
Copy code
sudo -u postgres psql
Inside the PostgreSQL shell:

sql
Copy code
CREATE DATABASE your_database_name;
CREATE USER your_database_user WITH PASSWORD 'your_database_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
\q
Update the Django settings:

Edit the settings.py file to include your PostgreSQL database configuration.

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply database migrations:

sh
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

sh
Copy code
python manage.py runserver
API Endpoints
Save Paragraphs
URL: /api/save-paragraph/

Method: POST

Description: Save multiple paragraphs and their word mappings.

Request Body:

json
Copy code
{
    "paragraphs": [
        "This is the first paragraph.",
        "This is the second paragraph."
    ]
}
Response:

json
Copy code
{
    "saved_paragraphs": [
        {
            "id": 1,
            "text": "This is the first paragraph.",
            "created_at": "2024-05-17T14:05:07Z",
            "modified_at": "2024-05-17T14:05:07Z"
        },
        {
            "id": 2,
            "text": "This is the second paragraph.",
            "created_at": "2024-05-17T14:05:07Z",
            "modified_at": "2024-05-17T14:05:07Z"
        }
    ]
}
Search Paragraphs
URL: /api/search-paragraph/

Method: GET

Description: Search for paragraphs containing a specific word.

Query Parameter:

word: The word to search for.
Example Request:

sql
Copy code
/api/search-paragraph/?word=first
Response:

json
Copy code
{
    "paragraphs": [
        {
            "id": 1,
            "text": "This is the first paragraph.",
            "created_at": "2024-05-17T14:05:07Z",
            "modified_at": "2024-05-17T14:05:07Z"
        }
    ]
}
Project Structure
codemonk/: Django project directory.
rest/: Django app directory containing the main application.
migrations/: Database migrations.
__init__.py: App initialization.
admin.py: Django admin configuration.
apps.py: App configuration.
models.py: Database models.
serializers.py: DRF serializers.
views.py: API views.
urls.py: URL configurations for the app.
manage.py: Django management script.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions, feel free to reach out to the project maintainer at your.email@example.com.

