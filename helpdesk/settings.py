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
    'ticketsystem',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
     'django.middleware.locale.LocaleMiddleware',
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

LOCALE_PATHS = (
    os.path.join(BASE_DIR, './locale'),

)

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

import ldap
from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
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
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=ab2015prod,dc=com",
ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="uid")
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=groups,dc=ab2015prod,dc=com"

AUTH_LDAP_USER_ATTR_MAP = {
"first_name": "cn","last_name": "sn",
"user_name": "uid","email":"mail"
}

AUTH_LDAP_PROFILE_ATTR_MAP = {
"uid": "uid"
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
"is_depadmin": "cn=depadmins,ou=groups,dc=ab2015prod,dc=com",
"is_sysadmin": "cn=sysadmins,ou=groups,dc=ab2015prod,dc=com",
"is_developer": "cn=developers,ou=groups,dc=ab2015prod,dc=com",
"is_netadmin": "cn=netadmins,ou=groups,dc=ab2015prod,dc=com",
"is_general": "cn=general,ou=groups,dc=ab2015prod,dc=com",
}
#This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True
#Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True
#Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'./helpdesk.log'),
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'helpdesk': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'userprofile': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'ticketsystem': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
