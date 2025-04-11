.PHONY: check_docker_installed check_mypy check_pyright local_typing docker_build docker_check typing

check_docker_installed:
	@command -v docker >/dev/null || (echo "Error: Docker not found. Install Docker first." && exit 1)

check_mypy:
	poetry run mypy src/otus_03/

check_pyright:
	poetry run pyright src/otus_03/

local_typing: check_mypy check_pyright

docker_build: check_docker_installed
	docker build -t app .

docker_check: check_docker_installed
	docker run --rm app

typing: docker_build docker_check

