from django.contrib import admin
from places.models import Place, Category

class PlaceAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
