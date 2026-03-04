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

#### 📝 courses\models.py

```py
from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Спеціалізація"
        verbose_name_plural = "Спеціалізації"
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE, verbose_name="Викладач")
    subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE, verbose_name="Спеціалізація")
    title = models.CharField(max_length=500, verbose_name="Назва")
    slug = models.SlugField(max_length=500, unique=True)
    overview = models.TextField(verbose_name="Опис")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        ordering = ['-created']
    
    def __str__(self):
        return self.title
```

```shell
py manage.py makemigrations
py manage.py migrate
```
