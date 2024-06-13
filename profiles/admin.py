from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_caregiver', 'date_of_birth', 'contact_phone', 'address']
    search_fields = ['user__username', 'contact_phone', 'address']
    list_filter = ['is_caregiver']

admin.site.register(Profile, ProfileAdmin)