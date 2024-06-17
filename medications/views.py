from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.core.exceptions import ObjectDoesNotExist

from profiles.models import Caregiver, Patient
from .models import IntakeSchedule, Prescription, Medication, IntakeTime, Day
from .forms import PrescriptionForm, MedicationForm, IntakeScheduleForm, IntakeTimeFormSet, DayFormSet


@login_required
def prescription_list(request):
    try:
        patient = request.user.patient
        prescription_list = Prescription.objects.filter(user=patient)
    except ObjectDoesNotExist:
        prescription_list = Prescription.objects.none()

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


@login_required
def add_intake_schedule(request, prescription_id, medication_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    medication = get_object_or_404(Medication, id=medication_id)

    if request.method == 'POST':
        form = IntakeScheduleForm(request.POST)
        intake_time_formset = IntakeTimeFormSet(request.POST, prefix='times')
        day_formset = DayFormSet(request.POST, prefix='days')

        if form.is_valid() and intake_time_formset.is_valid() and day_formset.is_valid():
            intake_schedule = form.save(commit=False)
            intake_schedule.prescription = prescription
            intake_schedule.medication = medication
            intake_schedule.save()
            form.save_m2m()  # Save the many-to-many relationships

            for time_form in intake_time_formset:
                if time_form.cleaned_data:
                    time = time_form.save(commit=False)
                    time.save()
                    intake_schedule.times.add(time)

            for day_form in day_formset:
                if day_form.cleaned_data:
                    day = day_form.save(commit=False)
                    day.save()
                    intake_schedule.days.add(day)

            return redirect('schedule_list')
    else:
        form = IntakeScheduleForm()
        intake_time_formset = IntakeTimeFormSet(queryset=IntakeTime.objects.none(), prefix='times')
        day_formset = DayFormSet(queryset=Day.objects.none(), prefix='days')

    return render(request, 'medications/add_intake_schedule.html', {
        'form': form,
        'intake_time_formset': intake_time_formset,
        'day_formset': day_formset,
        'prescription': prescription,
        'medication': medication,
    })

@login_required
def schedule_list(request):
    try:
        profile = Patient.objects.get(user=request.user)
        schedules = IntakeSchedule.objects.filter(prescription__user=profile)
    except Patient.DoesNotExist:
        try:
            profile = Caregiver.objects.get(user=request.user)
            schedules = IntakeSchedule.objects.filter(prescription__caregiver=profile)
        except Caregiver.DoesNotExist:
            schedules = IntakeSchedule.objects.none()

    return render(request, 'medications/schedule_list.html', {'schedules': schedules})