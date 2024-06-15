# forms.py
from django import forms
from .models import Prescription, Medication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class PrescriptionForm(forms.ModelForm):
    medications = forms.ModelMultipleChoiceField(
        queryset=Medication.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
        required=True
    )

    class Meta:
        model = Prescription
        fields = ['description', 'medications', 'start_date', 'end_date', 'is_on_going', 'valid_until', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'valid_until': forms.DateInput(attrs={'type': 'date'}),
        }

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'product_type',
            'name',
            'description',
            'unit',
            'type',
            Div('strength', css_id='strength-container', css_class='d-none'),
            'dosage_amount',
            'dosage_frequency',
            'image',
        )

        # Determine initial visibility based on data
        if 'type' in self.data and 'unit' in self.data:
            type = self.data.get('type')
            unit = self.data.get('unit')
            self.update_strength_visibility(type, unit)
        elif self.instance:
            type = self.instance.type
            unit = self.instance.unit
            self.update_strength_visibility(type, unit)

    def update_strength_visibility(self, type, unit):
        if (type in ['pill', 'capsule', 'tablet']) or (unit in ['mg', 'µg', 'g']):
            self.helper.layout[5].css_class = ''
        else:
            self.helper.layout[5].css_class = 'd-none'