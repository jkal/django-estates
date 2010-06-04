from django.conf.urls.defaults import *
from django.contrib import admin
from places.views import index as index_view, check_username, custom_login
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # static content
    (r'%s(?P<path>.*)/$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, }),

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/', custom_login),
    
    # login right after registration
    (r'^accounts/', include('registration.backends.simple.urls')),
    
    # uncomment to enable mail verification
    # (r'^accounts/', include('registration.backends.default.urls')),

    (r'^places/', include('places.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^usercheck/$', check_username),
    (r'^$', index_view),
)
