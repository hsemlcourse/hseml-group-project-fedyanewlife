.PHONY: lint up down

lint:
	flake8 src/

up:
	docker-compose up -d --build

down:
	docker-compose down