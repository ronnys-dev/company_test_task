Локальный запуск с docker-compose:

- Создаем .env.dev. в корневой папке, пример:

```
DEBUG=1

SECRET_KEY=django-secret-key

DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1'

SQL_ENGINE=django.db.backends.postgresql

SQL_DATABASE=django_db

SQL_USER=postgres

SQL_PASSWORD=password

SQL_HOST=db

SQL_PORT=5432

DATABASE=postgres
```

- Запускаем из корня

`docker-compose up --build`

- Пересобираем без кэша при необходимости docker-compose build --no-cache

http://localhost:8000/