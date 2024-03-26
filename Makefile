up:
	docker-compose up
upb:
	docker-compose up --build
tests:
	docker-compose exec python -m pytest tests -s
