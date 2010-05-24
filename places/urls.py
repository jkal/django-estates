from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from feeds import *

from places.views import all_places, fav_places, new_place, view_place, delete_place, fav_place

site_feeds = {
    'place': LatestPlaces,
}

urlpatterns = patterns('',
    (r'^$', all_places),
    (r'^favs/$', fav_places),
    (r'^new/$', new_place),
    (r'^new/thanks/$', direct_to_template, {'template':'places/thanks.html'}),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict' : site_feeds}), 
    (r'^(?P<place_id>\d{0,10})/$', view_place),
    (r'^(?P<place_id>\d{0,10})/delete/$', delete_place),
    (r'^(?P<place_id>\d{0,10})/fave/$', fav_place),
)
