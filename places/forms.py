from django.forms import Form, ModelForm
from places.models import Place

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        exclude = ['latitude', 'longitude', 'submitter', 'pub_date', 'published', 'hits',]
