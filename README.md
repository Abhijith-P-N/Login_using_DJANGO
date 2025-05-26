# Django Security Project

A simple Django web application with:
- User registration and login
- Admin interface
- Change password functionality
- PostgreSQL database integration
- Environment variables for secrets

---

## Features

- User registration and authentication
- Secure password storage and change password functionality
- Admin interface for managing users
- PostgreSQL as the primary database
- Environment variable support via `.env` file

---

## Requirements

- Python 3.8 or later (tested with Python 3.13)
- Django 4.x or 5.x
- PostgreSQL
- pip
- [django-environ](https://github.com/joke2k/django-environ) for environment variable loading

---

## Setup Instructions

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2. Set up a virtual environment

```sh
python -m venv venv
source venv/bin/activate          # On Linux/Mac
venv\Scripts\activate             # On Windows
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

1. Ensure PostgreSQL is installed and running.
2. Create a database (e.g., `login`) and a user with access:

```sql
-- In psql or PgAdmin
CREATE DATABASE login;
CREATE USER postgres WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE login TO postgres;
```

### 5. Create a `.env` file

Create a file named `.env` in your project root (same directory as `manage.py`):

```env
SECRET_KEY=your-very-secret-key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 6. Apply migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser (admin)

```sh
python manage.py createsuperuser
```

### 8. Run the development server

```sh
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your web browser.

---

## Usage

- Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) with your superuser credentials.
- Register a new user or log in at [http://localhost:8000/login/](http://localhost:8000/login/).
- Change password at [http://localhost:8000/password_change/](http://localhost:8000/password_change/).

---

## Project Structure

```
yourrepo/
├── accounts/                   # User authentication app
├── secureapp/                  # Main project settings
├── templates/
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       ├── password_change.html
│       └── password_change_done.html
├── manage.py
├── requirements.txt
└── .env
```

---

## Notes

- Always keep your `SECRET_KEY` and database credentials safe (never commit your `.env` to public repos).
- For production, set `DEBUG=False` and use secure values for your secrets.
- For custom features, extend the `accounts` app as needed.

---

## Troubleshooting

- **CSRF errors:** Ensure `{% csrf_token %}` is in all forms and cookies are enabled in your browser.
- **Template errors:** Make sure your template files exist in the proper directories.
- **Database errors:** Double-check your `.env` variables and PostgreSQL setup.

---

## License

MIT (or your chosen license)
