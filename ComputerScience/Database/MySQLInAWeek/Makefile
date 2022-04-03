run:
	docker compose up -d

build:
	docker compose build

down:
	docker compose down

remove:
	docker volume rm mysqlinaweek_mysql-db

.PHONY: logs
logs:
	docker compose logs -ft

.PHONY: login
login:
	docker exec -it mysql_container bash
