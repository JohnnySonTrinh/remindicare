from django.contrib import admin
from .models import Medication, Prescription, IntakeSchedule, IntakeTime, Day, Notification, DoseLog

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'type', 'strength', 'unit', 'dosage_amount', 'dosage_frequency')
    search_fields = ('name', 'product_type')
    list_filter = ('product_type', 'unit', 'type', 'strength')

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'caregiver', 'start_date', 'end_date', 'is_on_going')
    search_fields = ('user__user__username', 'caregiver__user__username')
    list_filter = ('is_on_going', 'start_date', 'end_date')

class IntakeScheduleAdmin(admin.ModelAdmin):
    list_display = ('prescription',)
    search_fields = ('prescription__user__user__username',)

class IntakeTimeAdmin(admin.ModelAdmin):
    list_display = ('time',)
    search_fields = ('time',)

class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('intake_time', 'sent_at', 'status', 'type', 'created_at')
    search_fields = ('intake_time__schedule__prescription__user__user__username',)
    list_filter = ('status', 'type', 'created_at')

class DoseLogAdmin(admin.ModelAdmin):
    list_display = ('notification', 'user', 'taken_at', 'status', 'created_at')
    search_fields = ('notification__intake_time__schedule__prescription__user__user__username', 'user__user__username')
    list_filter = ('status', 'created_at')

admin.site.register(Medication, MedicationAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(IntakeSchedule, IntakeScheduleAdmin)
admin.site.register(IntakeTime, IntakeTimeAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(DoseLog, DoseLogAdmin)
