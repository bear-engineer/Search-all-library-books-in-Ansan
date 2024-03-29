from .base import *

DEBUG = False

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.production.application'

INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}