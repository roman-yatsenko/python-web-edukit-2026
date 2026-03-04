# Платформа електронного навчання на Django (2026)

Ця платформа електронного навчання була розроблена з використанням фреймворку Django у 2026 році. Вона надає можливості для створення та управління онлайн-курсами, а також забезпечує інтерактивні функції для студентів та викладачів.

## 1. Створення проєкту

```shell
pip install pipenv --upgrade
pipenv install
pipenv install Django
pipenv install Pillow
```

Перезапуск терміналу

```shell
pipenv shell
django-admin startproject core .
django-admin startapp courses
```

#### 📝 /core/settings.py

```py=33
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',
]
```

```py=106
LANGUAGE_CODE = 'uk-UA'

TIME_ZONE = 'Europe/Kyiv'
```

### Роздавання медіафайлів

#### 📝 /core/settings.py

```py=125
# Media files

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'
```

#### 📝 core\urls.py

```py=17
from django.conf import settings
from django.conf.urls.static import static
```

```py=26
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
