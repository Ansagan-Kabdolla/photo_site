from django.contrib import admin
from .models import Services, Subservices, Example_photos


class SubservicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'basic_service')
    list_display_links = ('name', 'description')
    search_fields = ('description',)
    list_filter = ('basic_service',)


class Example_photosAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'basic_subservice')
    list_display_links = ('name', 'description')
    search_fields = ('description',)
    list_filter = ('basic_subservice',)

admin.site.register(Services)
admin.site.register(Subservices, SubservicesAdmin)
admin.site.register(Example_photos, Example_photosAdmin)
