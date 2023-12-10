.env:
	@cp .env.example .env

dev-start: .env
	@docker-compose up -d

dev-stop:
	@docker-compose down

dev-logs:
	@docker-compose logs -f

exec:
	@docker exec -it $$(echo "$$(docker ps --filter "name=django")" | awk 'NR > 1 {print $$1}') sh

start :
	@docker-compose up -d