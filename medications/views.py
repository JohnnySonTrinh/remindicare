from django.shortcuts import render

# Create your views here.
def user_meds(request):
    return render(request, 'medications/meds.html')