from django.contrib.syndication.feeds import Feed
from places.models import Place

class LatestPlaces(Feed):
    title = 'Latest Places'
    description = 'Latest Places'
    
    def items(self):
        return Place.objects.order_by('-pub_date')[:15]
    
    def item_pubdate(self, item):
        return item.pub_date
