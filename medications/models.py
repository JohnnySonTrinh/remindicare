from django.db import models
from profiles.models import Profile

class UserPrescription(models.Model):
    """
    Represents the intake record of a user, indicating whether it's a medication or supplement,
    and includes dosage and timing information.
    """
    DOSAGE_UNITS = [
        ('mg', 'mg'),
        ('µg', 'µg'),
        ('g', 'g'),
        ('ml', 'ml'),
        ('l', 'l'),
        ('IU', 'IU')
    ]

    DOSAGE_TYPES = [
        ('pill', 'Pill'),
        ('liquid', 'Liquid'),
        ('injection', 'Injection'),
        ('capsule', 'Capsule'),
        ('tablet', 'Tablet'),
        ('ointment', 'Ointment'),
        ('powder', 'Powder'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20, choices=[('medication', 'Medication'), ('supplement', 'Supplement')])
    product_name = models.CharField(max_length=200)
    dosage_unit = models.CharField(max_length=50, choices=DOSAGE_UNITS)
    dosage_type = models.CharField(max_length=50, choices=DOSAGE_TYPES)
    dosage_amount = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - {self.product_type} {self.product_name} - {self.dosage_amount}"


class IntakeTime(models.Model):
    """
    Represents the specific times for a scheduled intake.
    """
    time = models.TimeField()

    def __str__(self):
        return f"{self.time}"


class IntakeSchedule(models.Model):
    """
    Represents the schedule for a user's intake, specifying the days of the week.
    """
    userprescription = models.ForeignKey(UserPrescription, on_delete=models.CASCADE)
    days_of_week = models.CharField(max_length=50)  # e.g., "Monday, Wednesday, Friday"
    times = models.ManyToManyField('IntakeTime', related_name='intake_schedule')

    def __str__(self):
        return f"{self.userprescription.profile.user.username}'s {self.userprescription.product_type} schedule on {self.days_of_week} at {', '.join([str(time) for time in self.times.all()])}"


class DoseLog(models.Model):
    """
    Logs the status of each dose taken, missed, or skipped, along with the time it was recorded.
    """
    intake_schedule = models.ForeignKey(IntakeSchedule, on_delete=models.CASCADE)
    intake_time = models.ForeignKey(IntakeTime, on_delete=models.CASCADE)
    taken_at = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('taken', 'Taken'), ('missed', 'Missed'), ('skipped', 'Skipped')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        intake_item = self.intake_time.intake_schedule.user_intake.medication or self.intake_time.intake_schedule.user_intake.supplement
        return f"{intake_item.name if intake_item else 'N/A'} {self.status} at {self.taken_at}"


class Notification(models.Model):
    """
    Represents a notification for a scheduled intake, with status tracking for sent, snoozed, or dismissed notifications.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    intake_time = models.ForeignKey(IntakeTime, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('snoozed', 'Snoozed'), ('dismissed', 'Dismissed')])
    type = models.CharField(max_length=20, default='reminder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        intake_item = self.intake_time.intake_schedule.user_intake.medication or self.intake_time.intake_schedule.user_intake.supplement
        return f"Notification for {intake_item.name if intake_item else 'N/A'} at {self.scheduled_time}"
