Paste
=====
![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/dessolo/paste)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/dessolo/paste)
![Docker Pulls](https://img.shields.io/docker/pulls/dessolo/paste)
![Docker Image Version (latest by date)](https://img.shields.io/docker/v/dessolo/paste)
![GitHub](https://img.shields.io/github/license/dessolo/Paste)

*Simple implementation* https://pastebin.com
### Run server
```shell script
podman-compode up -d
podman exec -it paste_paste_1 bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### Environ
|Key|Default|Description|
|------|-------|------|
|SECRET_KEY|random generated|django secret key|
|TIME_ZONE|Europe/Moscow|timezone|
|DEBUG|False|debug mode|
|POSTGRES_DB|postgres| postgres database|
|POSTGRES_USER|postgres|postgres user|
|POSTGRES_PASSWORD|postgres|postgres password|
|POSTGRES_HOST|127.0.0.1|postgres host|
|POSTGRES_PORT|5432|postgres port|
