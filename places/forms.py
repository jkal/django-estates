from django import forms

class PlaceForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField()
    year = forms.IntegerField()
