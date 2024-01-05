Django Project
==============

This is a Docker (with docker-compose) environment for Django Project development.

# Installation

1. First, clone this repository:

```bash
$ git clone 
```

2. Init project
```bash
$ make
```

3. Show containers:
```bash
$ make ps
```
This results in the following running containers:

```bash
> $ docker-compose ps
   Name                  Command                 State                          Ports
----------------------------------------------------------------------------------------------------------
adminer       entrypoint.sh docker-php-e ...   Up           0.0.0.0:9000->8080/tcp
celery        celery -A core worker -l i ...   Up
celery-beat   celery -A core beat -l inf ...   Up
core          python manage.py runserver ...   Up           0.0.0.0:8000->8000/tcp
mailhog       MailHog                          Up           0.0.0.0:1025->1025/tcp, 0.0.0.0:8025->8025/tcp
postgres      docker-entrypoint.sh postgres    Up           0.0.0.0:5432->5432/tcp
redis         docker-entrypoint.sh redis ...   Up           0.0.0.0:6379->6379/tcp
```

