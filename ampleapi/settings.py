"""
Django settings for ampleapi project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#path to store media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL ='/media/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*i#h34=b#$q3*1w&)5gzmjnvzv8q$x)trt5(j$6lkg1(8fzi=+'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['aempleapp.herokuapp.com']
#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restapi',
    'core',
    'authentication',
    'rest_framework',
    'django_filters',
    'django_extensions',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ampleapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ampleapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#DATABASES = ('host=postgres://bibjvpeqexgdou:ccd93e4b9b37053b8b1ab7708ec52133326407d91475d7aa1134c38776775560@ec2-54-83-37-223.compute-1.amazonaws.com:5432/d2lahmntq0kksb:sslmode=require')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ddr3s102ja8fbv',
#         'USERNAME': 'elessnxxodqasd',
#         'PASSWORD' : '9f7ba44e313743fe8226aed8b3234bfea66948ade13797d1a428bcbdff6dec48',
#         'HOST' : 'ec2-54-204-46-236.compute-1.amazonaws.com',
#         'PORT' : '5432',
#      }
# }

# DATABASES = {
#     'default': {
#
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ampledb',
        'USERNAME': 'Samuel',
        'PASSWORD' : 'rekoll',
        'HOST' : 'localhost',
        'PORT' : '5433',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#STATIC_URL = '/static/'

import dj_database_url
#DATABASES['default'] = dj_database_url.config()

db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)

STATIC_URL = '/static/'
# STATICFILES_DIRS=[
#     os.path.join(BASE_DIR, "static"),
# ]
#
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'


#new code added for heroku deployment
# LOGOUT_REDIRECT_URL = '/login/'
# LOGIN_REDIRECT_URL = '/'
#
# CORS_REPLACE_HTTPS_REFERER = True
# #HOST_SECURE = "https://"
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTE_INCLUDE_SUBDOMAINS = True
# SECURE_HSTE_SECONDS = 1000000
# SECURE_FRAME_DENY = True


#second test codes for media
#STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


##newly added for user authentication
# Tell Django about the custom `User` model we created. The string
# `authentication.User` tells Django we are referring to the `User` model in
# the `authentication` module. This module is registered above in a setting
# called `INSTALLED_APPS`.
AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'core.exceptions.core_exception_handler',
#     'NON_FIELD_ERRORS_KEY': 'error',
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'authentication.backends.JWTAuthentication',
#     ),
#
#     'DEFAULT_PERMISSION_CLASSES': (
#              'rest_framework.permissions.IsAuthenticated',
#     #         #'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#          ),
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 20,
# }


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#         #'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ),
#     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
#     # 'DEFAULT_AUTHENTICATION_CLASSES': (
#     #     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     #     'rest_framework.authentication.SessionAuthentication',
#     #     'rest_framework.authentication.BasicAuthentication',
#     # ),
# }

WT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    #'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=60),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#         #'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ),
#     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
#     # 'DEFAULT_AUTHENTICATION_CLASSES': (
#     #     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     #     'rest_framework.authentication.SessionAuthentication',
#     #     'rest_framework.authentication.BasicAuthentication',
#     # ),
# }

#django_heroku.settings(locals())
