import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from places.widgets import *

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True, help_text='Optional')
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ Create slug from category name while saving. """
        
        if not self.slug:
            from django.template.defaultfilters import slugify
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Place(models.Model):
    address = models.CharField(max_length=50, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City')
    country = models.CharField(max_length=50, default='Greece', verbose_name='Country')
    category = models.ForeignKey(Category, verbose_name="Category")
    price = models.IntegerField(verbose_name="Price in Euros")
    area = models.IntegerField(verbose_name="Area in square meters")
    year = models.IntegerField(verbose_name="Construction year")

    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    #image = models.FileField(upload_to="uploads")
    #hits = models.IntegerField()
    #latitude = models.DecimalField(max_digits=8, decimal_places=6)
    #longitude = models.DecimalField(max_digits=8, decimal_places=6)
    #location = LocationField(blank=True, max_length=255)
    published = models.BooleanField()

    class Meta:
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return '%s, %s, %s' % (self.address, self.city, self.country)
