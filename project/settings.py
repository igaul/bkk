"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from os import getenv, path
from pathlib import Path

ENVFILE = getenv("ENV_FILE", ".env")

print("ENVFILE", ENVFILE)
if ENVFILE in ["0", "False", "false", "FALSE"]:
    print("skipping env load")
else:
    from dotenv import load_dotenv

    load_dotenv(ENVFILE)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print("BASE_DIR", BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

FLY_APP_NAME = getenv("FLY_APP_NAME")
FLY_HOST = f"{FLY_APP_NAME}.fly.dev"
ADD_FLY_HOST = FLY_APP_NAME and getenv("ADD_FLY_HOST", "False") == "True"


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")
if not SECRET_KEY:
    print("SECRET_KEY not set, generating one")
    from django.core.management.utils import get_random_secret_key

    SECRET_KEY = get_random_secret_key()

DEBUG = getenv("DEBUG", "False") == "True"


ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "").split(",")
if ADD_FLY_HOST and FLY_HOST and FLY_HOST not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(FLY_HOST)

if DEBUG and "localhost" not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append("localhost")

CSRF_TRUSTED_ORIGINS = [f"https://{ah}" for ah in ALLOWED_HOSTS]

if DEBUG:
    print("DEBUG", DEBUG, getenv("DEBUG"))
    print("ALLOWED_HOSTS", ALLOWED_HOSTS)
    print("CSRF_TRUSTED_ORIGINS", CSRF_TRUSTED_ORIGINS)


# Application definition

INSTALLED_APPS = [
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    #
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #
    "django_browser_reload",  # DEBUG only
    #
    "users",
    "website",
    "washingtonsite",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]
if DEBUG:
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "CONN_MAX_AGE": None,  # this is already default
        # TODO: add health check setting if psql
        "ENGINE": getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": getenv("DB_USER", "user"),
        "PASSWORD": getenv("DB_PASSWORD", "password"),
        "HOST": getenv("DB_HOST", "localhost"),
        "PORT": getenv("DB_PORT", "5432"),
        "OPTIONS": {},
    }
}
if getenv("DB_SSL"):
    DATABASES["default"]["OPTIONS"]["sslmode"] = "require"
if MAX_AGE := getenv("DB_CONN_MAX_AGE"):
    try:
        MAX_AGE = int(MAX_AGE)
        DATABASES["default"]["CONN_MAX_AGE"] = MAX_AGE
    except Exception:
        pass


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# TODO: use whitenoise (or s3)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
# TODO: use S3 or nginx container
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG" if DEBUG else "INFO")
if LOG_LEVEL not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    LOG_LEVEL = "INFO"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },
    "requests": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },
}
APP_LOGFILE = getenv("APP_LOG_FILE")
IS_IN_PRERELEASE = getenv("RELEASE_COMMAND") == "1"
if APP_LOGFILE and not IS_IN_PRERELEASE:
    try:
        # this will fail in staging container (no disk access)
        LOGGING["handlers"]["file"] = {
            "level": LOG_LEVEL,
            "class": "logging.FileHandler",  # TODO: RotatingFileHandler
            "filename": APP_LOGFILE,
        }
        LOGGING["root"]["handlers"].append("file")
        print("APP_LOGFILE", APP_LOGFILE)
    except Exception as e:
        print("failed to set file logger", e)
else:
    print("no APP_LOG_FILE")

# USER
AUTH_USER_MODEL = "users.CustomUser"


# WAGTAIL
WAGTAIL_SITE_NAME = "Baby Ketten"
WAGTAILADMIN_BASE_URL = "http://192.168.1.233:4455"
""" unused ... TODO: set to bkk if we use wt """
