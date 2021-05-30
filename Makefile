SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )

docker_up:
	docker-compose up -d

docker_up_single:
	docker-compose up -d backend 

docker_stop:
	docker-compose stop

docker_update_dependencies:
	docker-compose down
	docker-compose up -d --build

docker_test:
	docker-compose run backend python manage.py test $(ARG) --parallel --keepdb

docker_create_admin_user:
	docker-compose exec backend python manage.py createsuperuser
	# docker exec -it container_id python manage.py createsuperuser

build_front:
	cd frontend/ && npm run build
	cp -r frontend/build/ backend/web_interface/

test:
	python3 backend/manage.py test backend/ $(ARG) --parallel --keepdb
