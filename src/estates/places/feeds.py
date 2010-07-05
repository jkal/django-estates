from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _
from places.models import Place

class LatestPlacesFeed(Feed):
    title = _('Latest Places')
    link = '/places/'
    description = _('The 10 most recently added places.')
    
    def items(self):
        return Place.objects.filter(published=True).order_by('-pub_date')[:10] 
    
    def item_description(self, item):
        action = 'Sale' if item.action == 'S' else 'Rent'
        
        itemdata = "%s, %sm, %sE" % (action, item.area, item.price)
        return itemdata