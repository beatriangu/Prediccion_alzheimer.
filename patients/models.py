from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    EDUCATION_CHOICES = [
        ('primaria', 'Educación Primaria'),
        ('secundaria', 'Educación Secundaria'),
        ('universidad', 'Educación Universitaria'),
        ('postgrado', 'Postgrado'),
    ]
    
    id_patient = models.CharField(max_length=20, primary_key=True, verbose_name="ID Paciente (DNI/TIS)")
    name = models.CharField(max_length=100, verbose_name="Nombre completo")
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)], verbose_name="Edad")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sexo")
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, verbose_name="Nivel educativo")
    occupation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ocupación")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.id_patient})"

class ClinicalData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='clinical_data')
    data_type = models.CharField(max_length=50, verbose_name="Tipo de dato")
    value = models.CharField(max_length=255, verbose_name="Valor")
    date_recorded = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    
    class Meta:
        unique_together = ('patient', 'data_type', 'date_recorded')
    
    def __str__(self):
        return f"{self.patient.name} - {self.data_type}: {self.value}"
