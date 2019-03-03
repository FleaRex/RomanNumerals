test:
	pipenv run pytest

fix:
	pipenv run black .

lint:
	pipenv run black --check .
