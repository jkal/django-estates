#
# Django WSGI handler. Used by uWSGI.
#
import os, sys
import django.core.handlers.wsgi

sys.path.append('/sites/webprog2010')
sys.path.append('/sites/webprog2010/estates')

os.environ['DJANGO_SETTINGS_MODULE'] = 'estates.settings'

application = django.core.handlers.wsgi.WSGIHandler()
