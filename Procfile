release: python manage.py makemigrations --no-input
release: python manage.py migrate

web: gunicorn main.wsgi