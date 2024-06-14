from django.contrib import admin
from .models import Patient, Caregiver

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'contact_phone', 'address', 'is_active', 'caregiver')
    search_fields = ('user__username', 'contact_phone', 'address')
    list_filter = ('is_active', 'caregiver')

class CaregiverAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'contact_phone', 'address', 'is_verified', 'is_active')
    search_fields = ('user__username', 'contact_phone', 'address')
    list_filter = ('is_verified', 'is_active')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Caregiver, CaregiverAdmin)
