from django.shortcuts import render

# Create your views here.
def user_profile(request):
    return render(request, 'profiles/user_site.html')

def caregiver_user(request):
    return render(request, 'profiles/caretaker_user.html')
