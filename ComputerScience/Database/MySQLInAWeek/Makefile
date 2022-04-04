run:
	docker compose up -d

.PHONY: build
build:
	docker compose build

.PHONY: down
down:
	docker compose down

.PHONY: remove
remove:
	docker volume rm mysqlinaweek_mysql-db

.PHONY: logs
logs:
	docker compose logs -ft

.PHONY: login
login:
	docker exec -it mysql_container mysql -u root -p -h 127.0.0.1
