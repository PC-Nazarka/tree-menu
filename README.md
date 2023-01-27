# tree-menu

[Built with Cookiecutter DjangoRestFramework](https://github.com/PC-Nazarka/cookiecutter-django-rest-framework/)

## Для запуска проекта

Создайте ```.env``` файл в корневой папке проекта со следующими переменными:
- DJANGO_SECRET_KEY
- DJANGO_DEBUG
- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD

После создания файла запустите проект с помощью этих команд

```bash
docker-compose up --build -d
docker-compose run django python manage.py migrate
```

### Для создания супер пользователя

```bash
docker-compose exec django python manage.py createsuperuser
```

### Для удобства был написан скрипт для генерации данных

```bash
docker-compose run django python manage.py runscript fill_sample_data
```

### Для выбора отображенных меню в параметрах запроса использовать параметр ```menu```, после которого прописать имена меню

```http://0.0.0.0:8000/?menu=Меню1```

### Для выбора активного пункта меню в параметрах запроса использовать параметр ```menuitem```, после которого прописать id активных пунктов

Пример:

```http://0.0.0.0:8000/1/?menuitem=1```
