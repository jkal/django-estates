from django.contrib import admin
from places.models import Place, Category, UserProfile, Photo, Asset, Favorite
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# unregister User model to add the inline
admin.site.unregister(User)

class AssetAdmin(admin.ModelAdmin):
    pass

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserAdmin(UserAdmin):
    inlines = [
        UserProfileInline
    ]

class PhotoAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    actions = ['make_published']
    
    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = _('Mark selected places as published.')
    

class CategoryAdmin(admin.ModelAdmin):
    pass

class FavoriteAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin) 
admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Favorite, FavoriteAdmin)
# not needed
# admin.site.register(UserProfile, UserProfileInline)
