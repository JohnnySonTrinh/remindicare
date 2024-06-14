from django import forms
from .models import Profile

class Sign_up_user(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'is_caregiver', 'date_of_birth', 'contact_phone', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # 'contact_phone': forms.IntegerField(attrs={'type': 'tel'}),
        }
