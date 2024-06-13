from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_caregiver', 'date_of_birth', 'contact_information', 'address']

admin.site.register(Profile, ProfileAdmin)