# Makefile

run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

populate:
	python manage.py populate_fake_data

test:
	python manage.py test

lint:
	black . --exclude venv
