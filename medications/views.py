# views.py in medications app
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import IntakeSchedule, Prescription
from .forms import PrescriptionForm
from .forms import MedicationForm


@login_required
def prescription_list(request):
    prescription_list = Prescription.objects.all()
    schedules_list = IntakeSchedule.objects.all()

    context = {
        'prescriptions': prescription_list,
        'schedules': schedules_list,
    }
    
    return render(request, 'medications/prescription_list.html', context)

@login_required
def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.user = request.user.patient
            prescription.save()
            form.save_m2m()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    
    return render(request, 'medications/add_prescription.html', {'form': form})

@login_required
def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = MedicationForm()
    return render(request, 'medications/add_medication.html', {'form': form})