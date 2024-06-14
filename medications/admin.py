# from django.contrib import admin
# from .models import UserPrescription, DoseLog, IntakeSchedule, IntakeTime, Notification, Day

# class UserPrescriptionAdmin(admin.ModelAdmin):
#     list_display = ['profile', 'product_type', 'product_name', 'dosage_amount', 'dosage_unit', 'start_date', 'end_date', 'is_on_going']
#     search_fields = ['profile__user__username', 'product_name']
#     list_filter = ['product_type', 'dosage_unit', 'is_on_going']

# class DoseLogAdmin(admin.ModelAdmin):
#     list_display = ['notification', 'user', 'taken_at', 'status', 'created_at']
#     search_fields = ['notification__intake_schedule__userprescription__profile__user__username', 'taken_at', 'status']
#     list_filter = ['status']

# class DayAdmin(admin.ModelAdmin):
#     list_display = ['name', 'times_list']

#     def times_list(self, obj):
#         return ', '.join([str(time) for time in obj.times.all()])
#     times_list.short_description = 'Times'

# class IntakeScheduleAdmin(admin.ModelAdmin):
#     list_display = ['userprescription', 'days_list']

#     def days_list(self, obj):
#         return ', '.join([str(day) for day in obj.days.all()])
#     days_list.short_description = 'Days'


# class IntakeTimeAdmin(admin.ModelAdmin):
#     list_display = ['time']
#     search_fields = ['time']

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ['intake_schedule', 'scheduled_time', 'day', 'status']
#     search_fields = ['intake_schedule__userprescription__profile__user__username', 'scheduled_time', 'day']
#     list_filter = ['status']


# admin.site.register(UserPrescription, UserPrescriptionAdmin)
# admin.site.register(DoseLog, DoseLogAdmin)
# admin.site.register(IntakeSchedule, IntakeScheduleAdmin)
# admin.site.register(IntakeTime, IntakeTimeAdmin)
# admin.site.register(Day, DayAdmin)
# admin.site.register(Notification, NotificationAdmin)
