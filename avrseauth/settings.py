"""
Django settings for avrseauth project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '../..'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["192.168.0.18"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'eveauth'
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

AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.eveonline.EVEOnlineOAuth2',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    'eveauth.pipeline.update_user',
)

ROOT_URLCONF = 'avrseauth.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'avrseauth.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/services/'
SOCIAL_AUTH_CLEAN_USERNAMES = True
SOCIAL_AUTH_EVEONLINE_SCOPE = [
  "publicData"
]


# Celery
CELERY_IGNORE_RESULT = False
CELERY_TASK_RESULT_EXPIRES = 1200

CELERY_DISABLE_RATE_LIMITS = True
CELERYD_TASK_SOFT_TIME_LIMIT = 300
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(_PATH, 'static')

# How many hours between rechecking user groups via API
USER_UPDATE_DELAY = 1

# Celery
CELERY_APP_NAME = "avrseauth"
BROKER_URL = "redis://127.0.0.1:6379/"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/"
CELERY_IGNORE_RESULT = False
CELERY_TASK_RESULT_EXPIRES = 1200

CELERY_DISABLE_RATE_LIMITS = True
CELERYD_TASK_SOFT_TIME_LIMIT = 300
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True

from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    # Update user groups once an hour
    'spawn_groupupdates': {
        'task': 'spawn_groupupdates',
        #'schedule': timedelta(hours=USER_UPDATE_DELAY)
        'schedule': timedelta(seconds=30)
    },
    'purge_expired_templinks': {
        'task': 'purge_expired_templinks',
        'schedule': timedelta(seconds=5)
    }
}


from local_settings import *
