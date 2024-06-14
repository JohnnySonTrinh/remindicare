from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile
from medications.models import UserPrescription 

# Create your views here.
class Profiles(TemplateView):
    """User Profile Page"""

    template_name = "profiles/user_site.html"    

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        medications = UserPrescription.objects.filter(profile=profile)
        context = {
             "profile": profile,
             "prescriptions": medications,
         }

        return context
    
    
def caregiver_user(request):
    return render(request, 'profiles/caretaker_user.html')
