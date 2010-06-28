from django.conf.urls.defaults import *
from django.contrib import admin
from places.views import index as index_view 
from views import check_username, custom_login
import settings

admin.autodiscover()

js_info_dict = {
    'packages': ('estates',),
}

urlpatterns = patterns('',
    # static content
    url(r'%s(?P<path>.*)/$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, }),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^accounts/login/', custom_login),

    # login right after registration
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # uncomment to enable mail verification
    # url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^places/', include('places.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^usercheck/$', check_username, name='check-username'),
    url(r'^$', index_view, name='index-page'),
)
