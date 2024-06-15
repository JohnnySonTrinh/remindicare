from allauth.account.forms import SignupForm
from django import forms
from .models import Patient, Caregiver

class CustomSignupForm(SignupForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    contact_phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    is_caregiver = forms.BooleanField(required=False, label="Sign up as a caregiver")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        if self.cleaned_data["is_caregiver"]:
            Caregiver.objects.create(
                user=user,
                date_of_birth=self.cleaned_data["date_of_birth"],
                contact_phone=self.cleaned_data["contact_phone"],
                address=self.cleaned_data["address"]
            )
        else:
            Patient.objects.create(
                user=user,
                date_of_birth=self.cleaned_data["date_of_birth"],
                contact_phone=self.cleaned_data["contact_phone"],
                address=self.cleaned_data["address"]
            )
        return user
