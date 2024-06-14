from django.db import models
from profiles.models import Patient, Caregiver

class Medication(models.Model):
    """
    Represents a medication or supplement with dosage information.
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

    product_type = models.CharField(max_length=20, choices=[('medication', 'Medication'), ('supplement', 'Supplement')])
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dosage_unit = models.CharField(max_length=50, choices=DOSAGE_UNITS)
    dosage_type = models.CharField(max_length=50, choices=DOSAGE_TYPES)
    dosage_amount = models.CharField(max_length=50)
    dosage_frequency = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/images/', default='', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.dosage_unit}"


class Prescription(models.Model):
    """
    Represents a prescription for a user, possibly managed by a caregiver.
    """
    user = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    caregiver = models.ForeignKey(Caregiver, null=True, blank=True, on_delete=models.CASCADE, related_name='prescriptions')
    description = models.TextField(null=True, blank=True)
    medications = models.ManyToManyField(Medication, related_name='prescriptions')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_on_going = models.BooleanField(default=False)
    valid_until = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Prescription for: {self.user.user.username}"


class IntakeSchedule(models.Model):
    """
    Represents the intake schedule for a prescription, specifying the days of the week and times.
    """
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='schedules')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='schedules')
    days = models.ManyToManyField('Day', related_name='days')
    times = models.ManyToManyField('IntakeTime', related_name='times')

    def __str__(self):
        return f"{self.prescription.user.user.username}'s schedule - {self.medication.name}"


class IntakeTime(models.Model):
    """
    Represents specific intake times for a prescription.
    """
    time = models.TimeField()

    def __str__(self):
        return f"{self.time}"


class Day(models.Model):
    """
    Represents a day of the week for scheduling purposes.
    """
    WEEKDAYS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    name = models.CharField(max_length=9, choices=WEEKDAYS)

    def __str__(self):
        return f"{self.name}"


class Notification(models.Model):
    """
    Represents a notification for a scheduled intake, with status tracking.
    """
    intake_time = models.ForeignKey(IntakeTime, on_delete=models.CASCADE, related_name='notifications')
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('snoozed', 'Snoozed'), ('dismissed', 'Dismissed')])
    type = models.CharField(max_length=20, default='reminder')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.intake_time.schedule.prescription.user.user.username}"


class DoseLog(models.Model):
    """
    Logs the status of each dose taken, missed, or skipped.
    """
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT, related_name='dose_logs')
    user = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='dose_logs')
    taken_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('taken', 'Taken'), ('missed', 'Missed'), ('skipped', 'Skipped')], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification.intake_time.schedule.prescription.user.user.username} {self.status} at {self.taken_at}"
