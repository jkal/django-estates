from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True,help_text='Optional')
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.template.defaultfilters import slugify
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Place(models.Model):
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True)
    price = models.FloatField()
    area = models.FloatField()
    year = models.DecimalField(max_digits=4, decimal_places=0)
    hits = models.IntegerField()

    def __str__(self):
        return self.address
