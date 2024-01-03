from config.settings.base_settings import *  # NOQA

SECRET_KEY = "django-insecure-idv$okbx1eu)g+f#_v@_)m=m+g=s49jt=+hq)bvf2etspmkg$5"
DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
