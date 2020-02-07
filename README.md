# django_docker

Make Migrations

```bash
docker-compose run app sh -c "python manage.py makemigrations core"
```

Create a project
docker-compose run app sh -c "django-admin.py startproject app ."



Build & rebuild after adding new dependencies

docker-compose run app sh -c "django-admin.py startproject app ."


Run UnitTests and flake8
docker-compose run app sh -c "python manage.py test && flake8"


-------------------------------------------------------------------------------------------------------------

Docker


Build image from Dockerfile

docker build .


List running Images
docker ps

List all images
docker Ps -a








