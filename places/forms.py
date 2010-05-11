from django.forms import Form, ModelForm
from places.models import Place

class PlaceForm(ModelForm):
    class Meta:
        model = Place

        # fields to show on the form, with this order
        fields = ['address', 'city', 'country', 'category', 'price', 'area',
                  'year', 'description']
