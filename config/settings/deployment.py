import os
import environ
from datetime import timedelta
from config.settings.base import *

# env settings
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env.dev"))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = str(env("ALLOWED_HOSTS")).split(",")
WEATHER_API = env("WEATHER_API")

LOCAL_APPS = ["src.core"]
EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework_simplejwt', 'debug_toolbar',
    'drf_yasg', 'corsheaders', "django_celery_beat",
]

INSTALLED_APPS += LOCAL_APPS + EXTERNAL_APPS
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
]

DOCKER = int(env("DOCKER"))

host = 'db' if DOCKER else 'localhost'

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "HOST": host,
        "PORT": 5432,
        "PASSWORD": env("POSTGRES_PASSWORD")
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',  # Anonim foydalanuvchilar uchun limit
        'user': '1000/day',  # Tizimga kirgan foydalanuvchilar uchun limit
    },
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': True
}

# cors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT'
]
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ['*']

CSRF_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://\localhost:8000\$",
    r"^http://\127.0.0.1:8000\$",
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=21),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# django debug toolbar settings
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
import socket

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = 'assets/'
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Celery sozlamalari
if not DOCKER:
    CELERY_BROKER_URL = "redis://localhost:6379/0"  # Redis broker
else:
    CELERY_BROKER_URL = "redis://redis:6379/0"  # docker Redis broker
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
