release: python manage.py migrate
web: waitress-serve --port=$PORT database.wsgi:application
