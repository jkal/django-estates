from django import forms
from django.forms import Form, ModelForm, HiddenInput, TextInput
from places.models import Place, UserProfile

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        exclude = ['submitter', 'pub_date', 'published', 'hits',]

        widgets = {
            'latitude': HiddenInput(attrs={'value': ''}), 
            'longitude': HiddenInput(attrs={'value': ''}), 
        }
