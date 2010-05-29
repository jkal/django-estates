from django.contrib.syndication.views import Feed
from places.models import Place

class LatestPlacesFeed(Feed):
    title = 'Latest Places'
    link = '/places/'
    description = 'The 10 most recently added places.'
    
    def items(self):
        return Place.objects.filter(published=True).order_by('-pub_date')[:10]
    
    # def item_title(self, item):
    #     return item.title
    # 
    
    def item_description(self, item):
        return item.description