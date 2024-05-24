compose:
	docker compose up --build -d

lint:
	pylint $(git ls-files '*.py')