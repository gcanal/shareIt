#-*- coding: utf-8 -*-
"""
Django settings for shareit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#nh7w*_3=*8zr6ojm=ksr=*$+%@)&3pyc2+8+9-k@)grsl+cza'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True  #for developpement 

ALLOWED_HOSTS = []

ADMINS = (
  ('Guillaume CANAL', 'guillaume.canal@telecom-bretagne.eu'),
  ('Frédéric GRESSET', 'frederic.gresset@telecom-bretagne.eu'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'south',
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n", # for i18n ; important for the set_language redirect view
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
#"shareit.context_processors.view_name_context_processor",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#The order in MIDDLEWARE_CLASSES matters because a middleware can depend on other middleware. For instance,
#AuthenticationMiddleware stores the authenticated user in the session; therefore, it must run after SessionMiddleware.
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', #for i18n
    #'website.middleware.ViewNameMiddleware',#to have access to the view name
)

ROOT_URLCONF = 'shareit.urls'

WSGI_APPLICATION = 'shareit.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'database.sql', 
    'USER': '', 
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
  }
}

TEMPLATE_DIRS = (
  "./templates/"
)
################## Internationalization ##################
# https://docs.djangoproject.com/en/1.6/topics/i18n/
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (#path of the translation files
    "./locale/",
)
gettext = lambda x: x # we create a false gettext function in order to avoid importing django.utils.translation
#for this might cause an infinite import loop
LANGUAGES = (
   ('fr', gettext('French')),
   ('en', gettext('English')),
)
###################### Static Files  #######################

APPEND_SLASH = True  # Ajoute un slash en fin d'URL
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
"./static/", # directory name to put static files : JS CSS Imgs
)

# en developpement 
MEDIA_ROOT="./media/" #MEDIA_ROOT is the path on the filesystem to the directory containing our static media.
MEDIA_URL="/media/" # is the URL that makes the static media accessible over HTTP.
