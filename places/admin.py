from django.contrib import admin
from places.models import Place, Category, UserProfile, Photo, Asset

class AssetAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass
    
class PhotoAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Asset, AssetAdmin)