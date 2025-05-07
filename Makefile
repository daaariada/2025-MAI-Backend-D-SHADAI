.PHONY: migrate up down

migrate:
	docker-compose run web python manage.py migrate

up:
	docker-compose up -d

down:
	docker-compose down