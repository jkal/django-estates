from django.contrib import admin
from places.models import Place, Category, UserProfile, Photo, Asset, Favorite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# unregister User model to add the inline
admin.site.unregister(User)
admin.site.unregister(Group)

class AssetAdmin(admin.ModelAdmin):
    pass

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]

class PhotoAdmin(admin.ModelAdmin):
    pass

class PhotoInline(admin.TabularInline):
    model = Photo

class PlaceAdmin(admin.ModelAdmin):
    
    inlines = [
        PhotoInline
    ]
    
    list_display   = ('pk', 'address', 'city', 'category', 'submitter', 'published')
    list_filter    = ('published', 'category', 'action')
    ordering       = ('-pub_date',)
    search_fields  = ('address',)
    list_per_page  = 25
    
    #filter_horizontal

    actions = ['make_published']
    
    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = _('Mark selected places as published.')

class CategoryAdmin(admin.ModelAdmin):
    pass

class FavoriteAdmin(admin.ModelAdmin):
    # this is pretty cool actually
    raw_id_fields = ('user', 'place')

admin.site.register(User, UserAdmin) 
admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
# we don't need this since it's inlined to the PlaceAdmi
# admin.site.register(Photo, PhotoAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Favorite, FavoriteAdmin)
