from .base import *

DEBUG = False

ALLOWED_HOSTS = ["ip-address", "www.myhost.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": "",
    }
}

STATIC_ROOT = BASE_DIR / "static"
