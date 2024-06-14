from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile
from medications.models import UserPrescription 

# Create your views here.
class Profiles(LoginRequiredMixin, TemplateView):
    """User Profile Page"""

    model = Profile
    template_name = 'profiles/user_profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = {
            'profile': None,
            'prescriptions': None,
        }

        user = self.request.user
        profile = None

        try:
            profile = Profile.objects.get(user=user)
            context['profile'] = profile
        except Profile.DoesNotExist:
            context['profile'] = None

        try:
            context['prescriptions'] = UserPrescription.objects.filter(profile=profile)
        except UserPrescription.DoesNotExist:
            context['prescriptions'] = None
       
        return context


def caregiver_user(request):
    return render(request, 'profiles/caretaker_user.html')
