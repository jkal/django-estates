from django.contrib import admin
from places.models import Place, Category, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
