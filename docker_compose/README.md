# Проектное задание: Docker-compose

### При первом запуске необходимо выполнить команду (<docker-compose up -d --build>)
Нужные миграции выполнятся сами при сборке контейнера с приложением.

Функционал:
- Админ-панель Django
- Миграции Django
- Синхронное веб приложение Django
- БД - Postgresql
- Линтер - flake8
- docker
- docker-compose

# Структура файла .env.example:
- POSTGRES_NAME - Имя БД
- POSTGRES_USER - Пользователь БД
- POSTGRES_PASSWORD - Пароль от пользователя БД
- SECRET_KEY - Секретный ключ django
- DEBUG - Переменная отвечает за режим отладки (True/False)
- DB_PORT - Порт БД
- DB_HOST - Хост БД (Должен соответствовать имени внутри сети docker-compose, в данном случае db)