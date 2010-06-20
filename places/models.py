# -*- coding: utf8 -*-

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    home_address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    user = models.OneToOneField(User)
    public_profile_field = models.BooleanField(verbose_name="Public profile?")
    
    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    
    get_absolute_url = models.permalink(get_absolute_url)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text='Optional')
    
    class Meta:
        verbose_name_plural = 'Κατηγορίες'

    def __unicode__(self):
        return self.name


class Place(models.Model):
    
    ACTIONS = (('S', 'For sale'), ('R', 'For rent'))

    # location
    address = models.CharField(max_length=50, verbose_name='Address')
    zipcode = models.IntegerField(verbose_name='Zip Code')
    city = models.CharField(max_length=50, verbose_name='City')
    country = models.CharField(max_length=50, default='Greece', verbose_name='Country')
    latitude = models.FloatField()
    longitude = models.FloatField()

    # property info 
    action = models.CharField(max_length=1, blank=False, choices=ACTIONS, default="")
    price = models.IntegerField(verbose_name='Price in Euros')
    area = models.IntegerField(verbose_name='Area in square meters')
    year = models.IntegerField(verbose_name='Construction year')
    description = models.TextField()

    # submission related
    submitter = models.ForeignKey(User, verbose_name='Submitter')
    category = models.ForeignKey(Category, blank=False, verbose_name='Category', default="")
    pub_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    hits = models.IntegerField(default=0)

    class Meta:
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return '%s @ %s, %s' % (self.category.name, self.address, self.city)

    def get_absolute_url(self):
        return '/places/%i/' % self.pk

class Favorite(models.Model):
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return '%s likes %s' % (self.user.username, self.place)

class Photo(models.Model):
    place = models.ForeignKey(Place)
    pic = models.ImageField(upload_to="uploads/", blank=True)
    
    def __unicode__(self):
        return '%s for %s' % (self.pic.name, self.place)
    
class Asset(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    def __unicode__(self):
        return self.name

class PlaceAssets(models.Model):
    place = models.ForeignKey(Place)
    asset = models.ForeignKey(Asset)
    value = models.BooleanField(blank=False)
