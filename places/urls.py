from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from places.views import all_places, new_place, view_place

urlpatterns = patterns('',
    (r'^all/$', all_places),
    (r'^new/$', new_place),
    (r'^new/thanks/$', direct_to_template, {'template':'thanks.html'}),
    (r'^(?P<place_id>\d{0,10})/$', view_place),
)
