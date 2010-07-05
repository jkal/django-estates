from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from places.feeds import LatestPlacesFeed
from places.views import json, new_place, view_place, delete_place, fav_place, search_places

urlpatterns = patterns('',
    url(r'^$', search_places, name='all-places'),
    url(r'^json/$', json, name='places-json'),
    url(r'^new/$', new_place, name='new-place'),
    url(r'^new/thanks/$', direct_to_template, {'template':'places/thanks.html'}, name='new-place-thanks'),
    url(r'^feed/$', LatestPlacesFeed(), name='places-feed'), 
    url(r'^(?P<place_id>\d{0,10})/$', view_place, name='view-place'),
    url(r'^(?P<place_id>\d{0,10})/delete/$', delete_place, name='delete-place'),
    url(r'^(?P<place_id>\d{0,10})/fave/$', fav_place, name='fave-place'),
)
