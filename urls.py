from django.conf.urls.defaults import *
from django.contrib import admin
from places.views import index as index_view, check_username, custom_login
from registration.views import register 
from places.forms import RegistrationFormUserProfile
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # static content
    (r'%s(?P<path>.*)/$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, }),

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/', custom_login),
    (r'^accounts/register/$', register, {'backend': 'registration.backends.default.DefaultBackend', 'form_class' : RegistrationFormUserProfile}),
    (r'^accounts/', include('registration.backends.default.urls')),
    # login right after registration
    # (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^places/', include('places.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^usercheck/$', check_username),
    (r'^$', index_view),
)
