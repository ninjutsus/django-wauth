"""Django settings for example project."""


import os
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

print BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'example', 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.realpath(os.path.join(BASE_DIR, 'example/static')),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'example/templates'),
)

LOGIN_URL = reverse_lazy('auth_login_external')