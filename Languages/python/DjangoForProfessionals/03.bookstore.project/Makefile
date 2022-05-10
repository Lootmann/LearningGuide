run:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: restart
restart:
	docker compose restart

.PHONY: test
test:
	docker compose exec web python3 -m pytest -v

.PHONY: logs
logs:
	docker compose logs -ft

.PHONY: build
build:
	docker compose up -d --build

.PHONY: show_urls
show_urls:
	docker compose exec web python3 manage.py show_urls
