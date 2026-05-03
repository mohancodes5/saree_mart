"""
Django settings for Saree Store (monolithic, templates + Bootstrap 5).
"""

import os
import dj_database_url
from pathlib import Path

from django.contrib.messages import constants as msg_constants

BASE_DIR = Path(__file__).resolve().parent.parent

MESSAGE_TAGS = {
    msg_constants.DEBUG: "secondary",
    msg_constants.INFO: "info",
    msg_constants.SUCCESS: "success",
    msg_constants.WARNING: "warning",
    msg_constants.ERROR: "danger",
}

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-uvs)rc^q_zn0%r&i#-ibltub&)9nm4c)4d(l7%z7gqh1q1@5t!')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ["localhost", "127.0.0.1","*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "shop",
    "dashboard",
    "staff_admin",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "shop.context_processors.cart_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL", "postgresql://store_0ocg_user:NmPhLZ80wIBNbsSfFMYGK1Xnm67Pqoun@dpg-d7ri4qt7vvec738obk9g-a.oregon-postgres.render.com/store_0ocg")
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Leading slashes so browser resolves /media/... from any page (fixes broken product images).
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
