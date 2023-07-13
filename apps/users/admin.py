from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('photo', 'category', 'phone')
    list_display_links = ('phone',)
    # list_editable = ('category  ',)
    search_fields = ('category', 'id', 'phone')
    list_filter = ('category', 'id', 'phone')


admin.site.register(Profile, ProfileAdmin)
