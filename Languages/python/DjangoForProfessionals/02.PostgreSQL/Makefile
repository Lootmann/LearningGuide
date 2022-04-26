run:
	docker compose up -d

build:
	docker compose build

buildup:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -ft

# django commands
migrate:
	docker compose exec web python3 manage.py migrate

create-superuser:
	docker compose exec web python3 manage.py createsuperuser
