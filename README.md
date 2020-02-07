# django_docker

Make Migrations

```bash
docker-compose run app sh -c "python manage.py makemigrations core"
```

Create a project
```bash
docker-compose run app sh -c "django-admin.py startproject app ."
```


Build & rebuild after adding new dependencies
```bash
docker-compose run app sh -c "django-admin.py startproject app ."
```

Run UnitTests and flake8
```bash
docker-compose run app sh -c "python manage.py test && flake8"
```

-------------------------------------------------------------------------------------------------------------

Docker


Build image from Dockerfile
```bash
docker build .
```

List running Images
```bash
docker ps
```
List all images
```bash
docker Ps -a
```







