# patients/forms.py

from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['id_patient', 'name', 'age', 'gender', 'education_level', 'occupation']
