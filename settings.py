import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('John Kalantzis', 'ikalantzis@ceid.upatras.gr'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',            # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',              # Or path to database file if using sqlite3.
        'USER': '',                     # Not used with sqlite3.
        'PASSWORD': '',                 # Not used with sqlite3.
        'HOST': '',                     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                     # Set to empty string for default. Not used with sqlite3.
    },
}

TIME_ZONE = 'Europe/Athens'

# 'el' for Greek version, 'en' for English
LANGUAGE_CODE = 'el'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'lhg8#wkiz58qc-$&-1f690o6nane*23oc9cz!^a6pqkuq%!n_o'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'realty.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname('__file__'), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'registration',
    'profiles',
    'places',
    'easy_thumbnails',
    #'south',
)

AUTH_PROFILE_MODULE = 'places.UserProfile'

LOGIN_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7 

EMAIL_HOST = 'mail.ceid.upatras.gr'
#EMAIL_PORT = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = ''
DEFAULT_FROM_EMAIL = 'ikalantzis@ceid.upatras.gr'

# easy_thumbnails app settings
THUMBNAIL_DEBUG = True
