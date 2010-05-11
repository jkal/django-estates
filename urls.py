from django.conf.urls.defaults import *
from django.contrib import admin
from places.views import index as index_view
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # static content
    (r'%s(?P<path>.*)/$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, }),

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^places/', include('places.urls')),
    (r'^$', index_view),
)
