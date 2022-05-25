run:
	docker compose up -d

down:
	docker compose down

build:
	docker compose up build

buildup:
	docker compose up -d --build

restart:
	docker compose restart

migrate:
	docker compose exec web python3 manage.py migrate

test:
	docker compose exec web python3 -m pytest -v

verbose:
	docker compose exec web python3 -m pytest -vv --durations=0

logs:
	docker compose logs -ft

show_urls:
	docker compose exec web python3 manage.py show_urls
