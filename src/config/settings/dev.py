from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure"
DEBUG = True

INSTALLED_APPS += [  # NOQ
    "django_extensions",
]

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQ
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
