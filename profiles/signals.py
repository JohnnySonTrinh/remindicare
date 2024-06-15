# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Patient, Caregiver

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_caregiver:
#             Caregiver.objects.create(user=instance)
#         else:
#             Patient.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if hasattr(instance, 'patient'):
#         instance.patient.save()
#     elif hasattr(instance, 'caregiver'):
#         instance.caregiver.save()
