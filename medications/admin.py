# from django.contrib import admin
# from .models import UserPrescription, DoseLog, IntakeSchedule, IntakeTime, Notification, Day

# class UserPrescriptionAdmin(admin.ModelAdmin):
#     list_display = ['profile', 'product_name', 'product_type', 'dosage_amount', 'dosage_unit']
#     search_fields = ['profile__user__username', 'product_name', 'product_type']
#     list_filter = ['product_type', 'dosage_unit']

# class DoseLogAdmin(admin.ModelAdmin):
#     list_display = ['userprescription', 'intake_time', 'intake_date', 'taken_at']
#     search_fields = ['userprescription__profile__user__username', 'intake_time']
#     list_filter = ['intake_date']

# class DayAdmin(admin.ModelAdmin):
#     list_display = ['name', 'times_list']

#     def times_list(self, obj):
#         return ', '.join([str(time) for time in obj.times.all()])
#     times_list.short_description = 'Times'
# class IntakeScheduleAdmin(admin.ModelAdmin):
#     list_display = ['userprescription', 'days']
#     search_fields = ['userprescription__profile__user__username', 'days']
#     list_filter = ['days']


# class IntakeTimeAdmin(admin.ModelAdmin):
#     list_display = ['time']
#     search_fields = ['time']

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ['intake_schedule', 'scheduled_time', 'day', 'sent_at', 'status', 'type', 'created_at']
#     search_fields = ['intake_schedule__userprescription__profile__user__username', 'scheduled_time', 'day']
#     list_filter = ['status', 'type']



# admin.site.register(UserPrescription, UserPrescriptionAdmin)
# admin.site.register(DoseLog, DoseLogAdmin)
# admin.site.register(IntakeSchedule, IntakeScheduleAdmin)
# admin.site.register(IntakeTime, IntakeTimeAdmin)
# admin.site.register(Day, DayAdmin)
# admin.site.register(Notification, NotificationAdmin)
