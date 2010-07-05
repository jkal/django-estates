import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    firstname = models.CharField(max_length=30, verbose_name=_('first name'))
    lastname = models.CharField(max_length=30, verbose_name=_('last name'))
    home_address = models.CharField(max_length=30, verbose_name=_('home address'))
    phone_number = models.CharField(max_length=12, verbose_name=_('phone number'))
    user = models.OneToOneField(User, verbose_name=_('User'))
    public_profile_field = models.BooleanField(verbose_name=_('Public profile?'))
    
    class Meta:
        verbose_name_plural = _('User Profiles')
    
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(blank=True, help_text=_('Description (optional)'))
    
    def natural_key(self):
        return (self.name)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name=_('Asset name'))

    class Meta:
        verbose_name = _('Asset')
        verbose_name_plural = _('Assets')

    def __unicode__(self):
        return self.name

class Place(models.Model):
    
    ACTIONS = (
        ('S', _('For sale')), 
        ('R', _('For rent'))
    )

    # location
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    zipcode = models.IntegerField(verbose_name=_('Zip Code'))
    city = models.CharField(max_length=50, default=_('Patras'), verbose_name=_('City'))
    country = models.CharField(max_length=50, default=_('Greece'), verbose_name=_('Country'))
    latitude = models.FloatField(verbose_name=_('Latitude'))
    longitude = models.FloatField(verbose_name=_('Longitude'))

    # property info 
    action = models.CharField(max_length=1, blank=False, choices=ACTIONS, default="", verbose_name=_('Availability'))
    price = models.PositiveIntegerField(verbose_name=_('Price in Euros'))
    area = models.PositiveIntegerField(verbose_name=_('Area in square meters'))
    year = models.PositiveIntegerField(verbose_name=_('Construction year'))
    description = models.TextField(blank=True, verbose_name=_('Description/Other info'))

    # submission related
    submitter = models.ForeignKey(User, verbose_name=_('Submitter'))
    category = models.ForeignKey(Category, verbose_name=_('Category'), default="")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Publication date'))
    published = models.BooleanField(default=False, verbose_name=_('Is published?'))
    hits = models.IntegerField(default=0, verbose_name=_('Hits'))
    
    assets = models.ManyToManyField(Asset, blank=True, verbose_name=_('Assets'))

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return '%s @ %s, %s' % (self.category.name, self.address, self.city)

    def get_absolute_url(self):
        return '/places/%i/' % self.pk

class Favorite(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))
    place = models.ForeignKey(Place, verbose_name=_('Place'))

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')

    def __unicode__(self):
        return '%s likes %s' % (self.user.username, self.place)

class Photo(models.Model):
    place = models.ForeignKey(Place, verbose_name=_('Place'))
    pic = models.ImageField(upload_to="uploads/", blank=True, verbose_name=_('Photo'))
    
    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
    
    def __unicode__(self):
        return '%s for %s' % (self.pic.name, self.place)
