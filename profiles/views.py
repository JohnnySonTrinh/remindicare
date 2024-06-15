from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from allauth.account.views import SignupView
from .models import Patient, Caregiver
from .forms import CustomSignupForm
class CustomSignupView(SignupView):
    form_class = CustomSignupForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/user_profile.html'  # Specify your template name here

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    
        user = self.request.user
        profile = None

        context = {
            "profile": None,
            "title": None,
            "patients": None,
        }

        if hasattr(user, 'patient'):
            profile = get_object_or_404(Patient, user=user)
            context['profile'] = profile
            context['title'] = 'User'
        elif hasattr(user, 'caregiver'):
            profile = get_object_or_404(Caregiver, user=user)
            context['profile'] = profile
            context['title'] = 'Caregiver'
            context['patients'] = Patient.objects.filter(caregiver=profile)

        return context


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
