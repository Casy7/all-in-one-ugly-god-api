from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Location, Army, Character

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # fields to display in the list view
    list_display = ('id', 'name', 'description', 'preview_image')
    # search functionality by name
    search_fields = ('name',)
    # readonly field to render image safely
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        # generate html thumbnail if photo exists
        if obj.last_recorded_photo:
            return mark_safe(f'<img src="{obj.last_recorded_photo.url}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />')
        return "No Photo"
    
    # set column name in admin panel
    preview_image.short_description = 'Photo Preview'

@admin.register(Army)
class ArmyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'size', 'last_known_location', 'preview_image')
    # filter sidebar by faction and location
    list_filter = ('faction', 'last_known_location')
    search_fields = ('name',)
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.last_recorded_photo:
            return mark_safe(f'<img src="{obj.last_recorded_photo.url}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />')
        return "No Photo"
    
    preview_image.short_description = 'Photo Preview'

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'race', 'is_dangerous', 'last_known_location', 'preview_image')
    list_filter = ('race', 'is_dangerous', 'last_known_location')
    search_fields = ('name', 'race')
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.last_recorded_photo:
            return mark_safe(f'<img src="{obj.last_recorded_photo.url}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />')
        return "No Photo"
    
    preview_image.short_description = 'Photo Preview'