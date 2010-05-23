from django.forms import Form, ModelForm
from places.models import Place, UserProfile

#from registration.models import RegistrationProfile
#from registration.forms import RegistrationForm
#from django.utils.translation import ugettext_lazy as _

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        exclude = ['submitter', 'pub_date', 'published', 'hits',]

#attrs_dict = { 'class': 'required' }

#class RegistrationFormZ(RegistrationForm):
    #band = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
    
    #def save(self, profile_callback=None):
        #new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
        #password = self.cleaned_data['password1'],
        #email = self.cleaned_data['email'])
        #new_profile = ZProfile(user=new_user, favorite_band=self.cleaned_data['band'])
        #new_profile.save()
        #return new_user
