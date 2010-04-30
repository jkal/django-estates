from django.conf.urls.defaults import *
from django.contrib import admin

from places.views import index as index_view

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^$', index_view),
)
