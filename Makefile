all:
	docker build -t xscriber:0.1 . --network=host && docker compose down && docker compose  --env-file .env up -d
