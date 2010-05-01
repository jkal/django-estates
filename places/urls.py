from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from places.views import all_view, new_view

urlpatterns = patterns('',
    (r'^all/$', all_view),
    (r'^new/$', new_view),
    (r'^new/thanks/$', direct_to_template, {'template':'thanks.html'}),
)
