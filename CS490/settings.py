"""
Django settings for CS490 project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent #Location of the Project
TEMPLATES_DIR = BASE_DIR.joinpath('templates') #Location of the HTML templates
STATIC_DIR = BASE_DIR.joinpath('static') #Location of the Static (CSS,JS,Vendor)
MEDIA_DIR= BASE_DIR.joinpath('media') #Location of Images and User served Files


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2a-z11-%&u005h4_h_&=!=4f7olmalkn4#_qb4512u6_n8&&*a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #Till beta production it will be true

ALLOWED_HOSTS = ['cs-490.herokuapp.com','127.0.0.1'] # Hosted sites ,local site


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', #importing app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # compression for images
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CS490.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'CS490.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# sqlite3 DB local storage
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': BASE_DIR / 'db.sqlite3',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dagvc1pmm2qhlh',
        'HOST': 'ec2-52-86-116-94.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'spgvpoxswhnjhq',
        'PASSWORD': '2b93a0d932dd8284d64fcf954151e6f980d86223ec18b5d6d29ce405722842c9',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York' #Local Time

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = BASE_DIR.joinpath('static/files')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

#Media files(User uploaded files)

MEDIA_URL= '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'