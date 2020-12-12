# Quero Listar
Listing, API-like, universities and theirs courses

## Project decisions

* Using DJANGO with Django Rest Framework for better management of users, easy store objects and read/store them
* Django Rest Framework gives Serializers, wich is a great tool to query objects on API
* Docker and docker-compose to provide isolation of environment and easy deploy
* For the docker-compose, using architecture from Cookie-Cutter (check `compose` folder)
* For requirements, splitted in base and local libs, for them create for more environments
* Postgres as the database, because of schemas and views cached for scalabilty

## Running the project

With this command with essentials flags, docker will generate images with all the libs and run the server!

```bash
docker-compose up --build
```

## Developing

Docker-compose is configured to share the volume between container and the developer computer, so no re-building the image.


### Creating migrations

Modified the models, huh, generate new migration files

```bash
docker-compose run --rm django python manage.py makemigrations
```

Then, to apply it

```bash
docker-compose run --rm django python manage.py migrate
```

### First data

```bash
docker-compose run --rm django python manage.py shell < scripts/import_db_json.py
```

### Creating an admin user:

```bash
docker-compose run --rm django python manage.py createsuperuser --email admin@example.com --username admin
```

### Debugging

Need to run some script or command, step into the container then run whatelse you like:

```bash
docker-compose run --rm django bash
```
