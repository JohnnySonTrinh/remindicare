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
    image = models.ImageField(upload_to='static/images/', default='', blank=True)
    start_date = models.DateField()
    is_on_going = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    presc_valid_until = models.DateField(null=True, blank=True) # prescription valid until so a reminder can be sent to renew
    notes = models.TextField(null=True, blank=True) # Notes to caregiver

    def __str__(self):
        # pylint: disable=no-member
        return f"{self.profile.user.username} - {self.product_type} {self.product_name} - {self.dosage_amount}"

class IntakeSchedule(models.Model):
    """
    Represents the schedule for a user's intake, specifying the days of the week.
    """
    userprescription = models.ForeignKey(UserPrescription, on_delete=models.CASCADE)
    days = models.ManyToManyField('Day', related_name="weekdays")  # e.g., "Monday, Wednesday, Friday"
    

    def __str__(self):
        # pylint: disable=no-member
        return f"{self.userprescription.profile.user.username}'s {self.userprescription.product_type} schedule on {self.days} at {', '.join([str(time) for time in self.times.all()])}"

class IntakeTime(models.Model):
    """
    Represents the specific times for a scheduled intake.
    """
    intake_schedule = models.ForeignKey(IntakeSchedule, on_delete=models.CASCADE)
    time = models.TimeField()


    def __str__(self):
        return f"{self.time}"
class Day(models.Model):
    WEEKDAYS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    intake_schedule = models.ForeignKey(IntakeSchedule, on_delete=models.CASCADE)
    name = models.CharField(max_length=9, choices=WEEKDAYS)  # Maximum length is 9 for "Wednesday"
    times = models.ManyToManyField('IntakeTime', related_name='dose_times')

    def __str__(self):
        return f"{self.name} - {self.times}"

class Notification(models.Model):
    """
    Represents a notification for a scheduled intake, with status tracking for sent, snoozed, or dismissed notifications.
    """
    intake_schedule = models.ForeignKey(IntakeSchedule, on_delete=models.CASCADE)
    scheduled_time = models.ForeignKey(IntakeTime, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('snoozed', 'Snoozed'), ('dismissed', 'Dismissed')])
    type = models.CharField(max_length=20, default='reminder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.intake_schedule.userprescription.product_name}"


class DoseLog(models.Model):
    """
    Logs the status of each dose taken, missed, or skipped, along with the time it was recorded.
    """
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
    user = models.ForeignKey(Profile, on_delete=models.PROTECT) 
    taken_at = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('taken', 'Taken'), ('missed', 'Missed'), ('skipped', 'Skipped')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # pylint: disable=no-member
        return f"{self.intake_schedule.userprescription.product_name} {self.status} at {self.taken_at}"