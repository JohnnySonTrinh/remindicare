# views.py in medications app
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from medications.models import Day, IntakeSchedule, Medication, Prescription

@login_required
def prescription_list(request):
    prescription_list = Prescription.objects.all()
    schedules_list = IntakeSchedule.objects.all()

    context = {
        'prescriptions': prescription_list,
        'schedules': schedules_list,
    }
    
    return render(request, 'medications/prescription_list.html', context)
