from django.contrib import admin
from .models import UserPrescription, DoseLog, IntakeSchedule, IntakeTime, Notification

class UserPrescriptionAdmin(admin.ModelAdmin):
    list_display = ['profile', 'product_type', 'product_name', 'dosage_amount', 'start_date', 'end_date', 'notes']
    search_fields = ['profile__user__username', 'product_name', 'dosage_amount']
    list_filter = ['product_type', 'start_date', 'end_date']

class DoseLogAdmin(admin.ModelAdmin):
    list_display = ['intake_schedule', 'intake_time', 'taken_at', 'status', 'created_at']
    search_fields = ['intake_schedule__userprescription__profile__user__username', 'intake_time__time', 'status']
    list_filter = ['status', 'created_at']

class IntakeScheduleAdmin(admin.ModelAdmin):
    list_display = ['userprescription', 'days_of_week', 'times_list']
    search_fields = ['userprescription__profile__user__username', 'days_of_week']
    list_filter = ['days_of_week']

    def times_list(self, obj):
        return ', '.join([str(time) for time in obj.times.all()])
    times_list.short_description = 'Times'

class IntakeTimeAdmin(admin.ModelAdmin):
    list_display = ['time']
    search_fields = ['time']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['profile', 'intake_schedule', 'scheduled_time', 'sent_at']
    search_fields = ['profile__user__username', 'intake_schedule__userprescription__product_name']
    list_filter = ['sent_at']



admin.site.register(UserPrescription, UserPrescriptionAdmin)
admin.site.register(DoseLog, DoseLogAdmin)
admin.site.register(IntakeSchedule, IntakeScheduleAdmin)
admin.site.register(IntakeTime, IntakeTimeAdmin)
admin.site.register(Notification, NotificationAdmin)
