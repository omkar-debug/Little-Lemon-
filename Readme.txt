LITTLE LEMON RESTAURANT API
===========================

PROJECT
This is a Django and Django REST Framework restaurant API. Django serves a styled home page at /. The project includes public menu browsing, authenticated menu management, guest-owned table bookings, user registration, token login, the Django admin, and API tests. MySQL is supported and configured with environment variables. SQLite is used by default for a quick development run.

REQUIREMENTS
- Python 3.10 or newer
- MySQL Server 8 (for MySQL mode); create a database named littlelemon with utf8mb4, and have a MySQL user with permission to use it
- Git (for committing and pushing the project)

SETUP (PowerShell)
1. Create and activate a virtual environment:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
2. Install dependencies:
   py -m pip install -r requirements.txt
3. For MySQL mode, copy .env.example to .env and set DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, and DJANGO_SECRET_KEY. The project loads these values from .env. Quick SQLite mode needs no database configuration.
   Quick SQLite mode needs no database configuration.
4. Create database tables and an admin account:
   py manage.py migrate
   py manage.py createsuperuser
5. Start the server:
   py manage.py runserver
6. Visit http://127.0.0.1:8000/ . Manage menu items in /admin/ or with an authenticated API request.

API PATHS FOR PEER REVIEW
Base URL: http://127.0.0.1:8000

GET     /                         Styled Django home page (HTML)
GET     /api/menu-items/          List menu items (public)
POST    /api/menu-items/          Add a menu item (authentication required)
GET     /api/menu-items/{id}/     Retrieve a menu item (public)
PUT     /api/menu-items/{id}/     Replace a menu item (authentication required)
PATCH   /api/menu-items/{id}/     Update a menu item (authentication required)
DELETE  /api/menu-items/{id}/     Delete a menu item (authentication required)
POST    /api/auth/register/       Register a user; response includes an API token
POST    /api/auth/token/login/    Get an API token using username and password
GET     /api/bookings/            List your bookings (authentication required)
POST    /api/bookings/            Create a booking for the signed-in user
GET     /api/bookings/{id}/       Retrieve one of your bookings
PUT/PATCH/DELETE /api/bookings/{id}/  Change or delete one of your bookings
GET     /admin/                   Django admin login

AUTHENTICATION
Register with JSON {"username":"reviewer","email":"reviewer@example.com","password":"StrongPass123!"}. The response returns a token. Alternatively POST {"username":"reviewer","password":"StrongPass123!"} to /api/auth/token/login/. For protected requests set the header:
Authorization: Token YOUR_TOKEN_HERE

MENU EXAMPLE
POST /api/menu-items/ JSON: {"title":"Lemon cake","price":"6.50","inventory":8}

BOOKING EXAMPLE
POST /api/bookings/ JSON: {"name":"Avery","no_of_guests":2,"booking_date":"2026-12-20T19:00:00Z"}
The booking is associated with the authenticated user automatically. Each user can access only their own reservations.

INSOMNIA
Create a request collection with base URL http://127.0.0.1:8000. Register or log in first, copy the returned token, then set Authorization to Bearer/Token authentication with the value YOUR_TOKEN_HERE (or add the exact header Authorization: Token YOUR_TOKEN_HERE). Set JSON request bodies to application/json. Try public GET /api/menu-items/, authenticated menu POST, registration/login, then authenticated booking GET/POST/PUT/DELETE.

TESTS
Run: py manage.py test restaurant

GIT AND COURSE SUBMISSION
Initialize or use your Git repository, commit all project files including this Readme.txt, and push it to GitHub. Then paste that GitHub repository URL into the course My submission form, preview, and submit. The repository URL and course submission require your GitHub account and course-site actions; this workspace does not know your repository URL or credentials.
