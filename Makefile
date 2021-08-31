venv:
	C:/Python/Python36/python.exe -m venv venv

init:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

serve:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

super:
	python manage.py createsuperuser --user=admin --email=admin@project.dev

gen-key:
	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

test:
	python manage.py test