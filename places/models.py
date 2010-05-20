import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    home_address = models.TextField()
    phone_numer = models.CharField(max_length=12)
    user = models.ForeignKey(User, unique=True)

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
    
    # location
    address = models.CharField(max_length=50, verbose_name='Address')
    zipcode = models.IntegerField(verbose_name='Zip Code')
    city = models.CharField(max_length=50, verbose_name='City')
    country = models.CharField(max_length=50, default='Greece', verbose_name='Country')
    
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)

    # estate info 
    # type = Diamerisma, Monokatoikia, Garsoniera, 
    # bedrooms = 3
    price = models.IntegerField(verbose_name='Price in Euros')
    area = models.IntegerField(verbose_name='Area in square meters')
    year = models.IntegerField(verbose_name='Construction year')
    description = models.TextField()
    #image = models.FileField(upload_to="uploads")

    # submission related
    submitter = models.ForeignKey(User, verbose_name='Submitter')
    category = models.ForeignKey(Category, null=False, verbose_name='Category', help_text="Category")
    pub_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    hits = models.IntegerField(default=0)

    class Meta:
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return '%s, %s, %s' % (self.address, self.city, self.country)
