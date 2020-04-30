Paste
=====
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
