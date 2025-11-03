# alx_travel_app

This is a minimal Django project scaffold prepared for Milestone 1: Setup and Database Configuration.

## What's included
- Django project `alx_travel_app`
- App `listings`
- `requirements.txt`
- `.env` with default DB values (change before production)
- Swagger (drf-yasg) configured at `/swagger/`
- Basic REST endpoint at `/api/listings/`

## Quick start (after download)
1. Create a virtualenv and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Update `.env` with your real `SECRET_KEY` and database credentials.
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser and run server:
   ```bash
   python manage.py createsuperuser
   python manage.py runserver
   ```
5. Visit:
   - `http://127.0.0.1:8000/swagger/` for Swagger UI
   - `http://127.0.0.1:8000/api/listings/` for listings API

## GitHub remote
You provided `https://github.com` — please replace the remote URL with your repository:
```bash
git remote add origin https://github.com/<your-username>/alx_travel_app.git
```
