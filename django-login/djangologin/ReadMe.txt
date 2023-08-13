
DJAGNO

PATH error with django => python -m django startproject django

migrate the database schema
python manage.py migrate

start the server
python manage.py runserver      ** if you want you can add 8080 at the end to run at a specific port 



Create admin user
python manage.py createsuperuser



After setting up static
run
python manage.py collectstatic


DJANGO caching problem:
run without saving cach:
python manage.py runserver --nothreading --noreload
