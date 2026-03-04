# python-web-edukit-2026

Платформа електронного навчання на Django (2026)

## Структура моделей курсів

```
Subject 1
  Course 1
    Module 1
      Content 1 (image)
      Content 2 (text)
    Module 2
      Content 3 (text)
      Content 4 (file)
      Content 5 (video)
      Content 6 (url)
      ...
```

## Використання фікстур для БД

```shell
py manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
# delete all subjects from DB
py manage.py loaddata subjects.json
```
