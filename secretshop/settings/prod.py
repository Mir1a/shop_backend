# region				-----External Imports-----
import os
# endregion

# region				-----Internal Imports-----
from .django import *
from .project import *
from .third_party import *
# endregion

SECRET_KEY = 'django-insecure-f3b^5-n1zgj1z&(6vl=uykrs6kppw1k)xov8)y^**!d0a-zp!l^'

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE'),
        'ATOMIC_REQUESTS': True
    }
}

# CACHE

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{os.environ.get("REDIS_HOST","127.0.0.1")}:{os.environ.get("REDIS_PORT",6379)}/1',
    }
}

MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware'] + \
             MIDDLEWARE + \
             ['django.middleware.cache.FetchFromCacheMiddleware']

# CORS
INSTALLED_APPS += ['corsheaders']

MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.common.CommonMiddleware') - 1,
    'corsheaders.middleware.CorsMiddleware'
)

MIDDLEWARE.insert(
    # MIDDLEWARE.index('secretshop.middleware.Process4XXError') - 1,
    'secretshop.middleware.Process500Error'
)

CORS_ALLOWED_ORIGINS = [
    f'http://{os.environ.get("FRONTEND_DOMAIN")}',
    f'https://{os.environ.get("FRONTEND_DOMAIN")}',
    'http://127.0.0.1:3000',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://localhost'
]

# 500 middleware


print(">>> START PROJECT WITH PROD SETTINGS <<<")

