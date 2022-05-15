run:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: build
build:
	docker compose up -d --build

.PHONY: restart
restart:
	docker compose restart

.PHONY: migrate
migrate:
	docker compose exec web python3 manage.py migrate

.PHONY: test
test:
	docker compose exec web python3 -m pytest -v

.PHONY: verbose
verbose:
	docker compose exec web python3 -m pytest -vv --durations=0

.PHONY: logs
logs:
	docker compose logs -ft

.PHONY: show_urls
show_urls:
	docker compose exec web python3 manage.py show_urls
