from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Represents a user profile, extending the base User model with additional information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_caregiver = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username if self.user else ''
    
    @property
    def is_caregiver(self):
        return hasattr(self, 'caregiver')

    @property
    def is_patient(self):
        return hasattr(self, 'patient')

class Patient(Profile):
    """
    Represents a patient profile, extending the base Profile model with additional information.
    """
    is_active = models.BooleanField(default=True)
    caregiver = models.ForeignKey('Caregiver', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else ''


class Caregiver(Profile):
    """
    Represents a caregiver profile, extending the base Profile model with additional information.
    """
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username if self.user else ''
