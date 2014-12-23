"""
Django settings for helpdesk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
COMMON_CONFIG_FILE='/opt/helpdesk.conf'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from readconf import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DJANGOSETTINGS=DjangoSettings()
SECRET_KEY = DJANGOSETTINGS.getsecretkey()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.views',
    'django_auth_ldap',
    'helpdesk',
    'userprofile',
    
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#  'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'helpdesk.urls'

WSGI_APPLICATION = 'helpdesk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DBCONF=DBconfig()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DBCONF.getdatabase(),
        'USER': DBCONF.getdbuser(),
	'PASSWORD': DBCONF.getdbpass(),
        'HOST': DBCONF.getdbhost(),
        'PORT': DBCONF.getdbport()
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'helpdesk/static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'helpdesk/templates/'),
)

import ldap
from django_auth_ldap.config import LDAPSearch
LDAPCONF=LDAPconfig()
AUTHENTICATION_BACKENDS = ('django_auth_ldap.backend.LDAPBackend','django.contrib.auth.backends.ModelBackend')
AUTH_LDAP_SERVER_URI = "ldap://"+LDAPCONF.getldaphost()+":"+LDAPCONF.getldapport()
AUTH_LDAP_BIND_DN = LDAPCONF.getbasedn()
AUTH_LDAP_BIND_PASSWORD = LDAPCONF.getldappass()
AUTH_LDAP_USER_SEARCH = LDAPSearch(LDAPCONF.getsearchdn(),
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}
