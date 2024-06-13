from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile, extending the base User model with additional information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_caregiver = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    contact_phone = models.CharField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user.username if self.user else ''
    