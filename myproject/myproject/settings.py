"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qy%yqfqt@#*iz59jyhuu99p73)g-r%5-umq7+xhyz43ycxn^c-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','loginbg.bc-pl.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'logindb',                      
        'USER': 'bariflolabs',
        'PASSWORD': 'bariflo2024',
        'HOST': '20.244.37.91',
        'PORT': '5432', 
    }
}

################## Admin IOT Database ########################################################
ADMIN_DASH_DB_NAME = 'admindb'
ADMIN_DASH_DB_USER = 'Bariflolabs'
ADMIN_DASH_DB_PASS = 'Bfl@2024'
ADMIN_DASH_DB_HOST = 'aqua-postgres.postgres.database.azure.com'
ADMIN_DASH_DB_PORT = '5432'

################## Aqua farming Database ########################################################
AQUA_FARM_DB_NAME = 'aquadb'
AQUA_FARM_DB_USER = 'Bariflolabs'
AQUA_FARM_DB_PASS = 'Bfl@2024'
AQUA_FARM_DB_HOST = 'aqua-postgres.postgres.database.azure.com'
AQUA_FARM_DB_PORT = '5432'

################## Waterbody Database ########################################################
WATERBODY_DB_NAME = 'waterdb'
WATERBODY_DB_USER = 'Bariflolabs'
WATERBODY_DB_PASS = 'Bfl@2024'
WATERBODY_DB_HOST = 'aqua-postgres.postgres.database.azure.com'
WATERBODY_DB_PORT = '5432'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    'https://loginbg.bc-pl.com',
]

CORS_ORIGIN_ALLOW_ALL = True


