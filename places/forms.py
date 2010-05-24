from django import forms
from django.forms import Form, ModelForm, HiddenInput, TextInput
from places.models import Place, UserProfile

#from registration.models import RegistrationProfile
#from registration.forms import RegistrationForm
#from django.utils.translation import ugettext_lazy as _

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        exclude = ['submitter', 'pub_date', 'published', 'hits',]

        widgets = {
            'latitude': HiddenInput(attrs={'value': ''}), 
            'longitude': HiddenInput(attrs={'value': ''}), 
        }

#attrs_dict = { 'class': 'required' }

#class RegistrationFormUserProfile(RegistrationForm):
    #home_address = forms.CharField(widget=TextInput(attrs=attrs_dict))
    #phone_number = forms.CharField(widget=TextInput(attrs=attrs_dict))
    
    #def save(self, profile_callback=None):
        #new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
        #password = self.cleaned_data['password1'],
        #email = self.cleaned_data['email'])
        #new_profile = UserProfile(user=new_user, home_address=self.cleaned_data['home_address'], phone_number=self.cleaned_data['phone_number'])
        #new_profile.save()
        #return new_user
