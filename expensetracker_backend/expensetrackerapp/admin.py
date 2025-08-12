from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'location', 'land_size_acres', 'asking_price', 'created_at')
    list_filter = ('property_type', 'created_at')
    search_fields = ('location', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        ('Property Details', {
            'fields': ('property_type', 'location', 'land_size_acres', 'asking_price')
        }),
        ('Additional Information', {
            'fields': ('description',)
        }),
    )
