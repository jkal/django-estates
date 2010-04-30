from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True,help_text='Optional')

class (models.Model):
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True)
    price = models.FloatField()
    area = models.FloatField()
    year = models.DecimalField(max_digits=4, decimal_places=0)
     
    def __str__(self):
        # Note use of django.utils.encoding.smart_str() here because
        # first_name and last_name will be unicode strings.
        return smart_str('%s' % self.address)
